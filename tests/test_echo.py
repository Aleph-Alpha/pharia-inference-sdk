from collections.abc import Sequence
from typing import Literal

import tokenizers  # type: ignore
from aleph_alpha_client import CompletionResponse, Prompt, Text, Tokens
from aleph_alpha_client.completion import CompletionResult
from pytest import fixture

from pharia_inference_sdk.connectors.limited_concurrency_client import (
    AlephAlphaClientProtocol,
)
from pharia_inference_sdk.core import MAX_CONCURRENCY, NoOpTracer, Task, TaskSpan, Token
from pharia_inference_sdk.core.echo import Echo, EchoInput, TokenWithLogProb
from pharia_inference_sdk.core.model import (
    AlephAlphaModel,
    CompleteInput,
    CompleteOutput,
    ControlModel,
    LuminousControlModel,
)


@fixture
def echo_task(llama_control_model: ControlModel) -> Echo:
    return Echo(llama_control_model)


@fixture
def echo_input() -> EchoInput:
    return EchoInput(
        prompt=Prompt.from_text("The weather is"),
        expected_completion="good",
    )


class ExpectTextAndTokenItemPromptCompletion(Task[CompleteInput, CompleteOutput]):
    def __init__(self, tokenizer: tokenizers.Tokenizer) -> None:
        self._tokenizer = tokenizer

    def do_run(self, input: CompleteInput, task_span: TaskSpan) -> CompleteOutput:
        input_prompt_items = input.prompt.items
        assert len(input_prompt_items) == 2
        assert isinstance(input_prompt_items[0], Text) and isinstance(
            input_prompt_items[1], Tokens
        )
        log_probs = [
            {self._tokenizer.decode([token_id]): 0.5}
            for token_id in input_prompt_items[1].tokens
        ]
        return CompleteOutput.from_completion_response(
            CompletionResponse(
                "version",
                completions=[CompletionResult(log_probs=log_probs)],
                num_tokens_generated=0,
                num_tokens_prompt_total=0,
            )
        )


class FakeCompleteTaskModel(LuminousControlModel):
    def __init__(
        self,
        name: Literal[
            "luminous-base-control",
            "luminous-extended-control",
            "luminous-supreme-control",
            "luminous-base-control",
            "luminous-extended-control",
            "luminous-supreme-control",
        ],
        client: AlephAlphaClientProtocol,
    ) -> None:
        self.name = name
        self._client = client
        self._complete = ExpectTextAndTokenItemPromptCompletion(self.get_tokenizer())


def tokenize_completion(
    expected_output: str, aleph_alpha_model: AlephAlphaModel
) -> Sequence[Token]:
    tokenizer = aleph_alpha_model.get_tokenizer_no_whitespace_prefix()
    encoding: tokenizers.Encoding = tokenizer.encode(expected_output)
    return [
        Token(
            token=tokenizer.decode([token_id], skip_special_tokens=False),
            token_id=token_id,
        )
        for token_id in encoding.ids
    ]


def test_can_run_echo_task(echo_task: Echo, echo_input: EchoInput) -> None:
    result = echo_task.run(echo_input, tracer=NoOpTracer())

    tokens = tokenize_completion(echo_input.expected_completion, echo_task._model)
    assert len(tokens) == len(result.tokens_with_log_probs)
    assert all([isinstance(t, TokenWithLogProb) for t in result.tokens_with_log_probs])
    for token, result_token in zip(tokens, result.tokens_with_log_probs, strict=True):
        assert token == result_token.token


def test_echo_works_with_whitespaces_in_expected_completion(
    echo_task: Echo,
) -> None:
    expected_completion = " good."
    input = EchoInput(
        prompt=Prompt.from_text("The weather is"),
        expected_completion=expected_completion,
    )
    tokens = tokenize_completion(expected_completion, echo_task._model)

    result = echo_task.run(input, tracer=NoOpTracer())

    assert len(tokens) == len(result.tokens_with_log_probs)
    assert all([isinstance(t, TokenWithLogProb) for t in result.tokens_with_log_probs])
    for token, result_token in zip(tokens, result.tokens_with_log_probs, strict=True):
        assert token == result_token.token


def test_overlapping_tokens_generate_correct_tokens(echo_task: Echo) -> None:
    """This test checks if the echo task correctly tokenizes the expected completion separately.

    The two tokens when tokenized together will result in a combination of the end of the first token
    and the start of the second token. This is not the expected behaviour.

    Args:
        echo_task: Fixture used for this test
    """
    token1 = "ĠGastronomie"
    token2 = "Baby"

    prompt = Prompt.from_text(token1[0 : len(token1) // 2])
    expected_completion = token1[-len(token1) // 2 :] + token2
    input = EchoInput(
        prompt=prompt,
        expected_completion=expected_completion,
    )

    tokens = tokenize_completion(expected_completion, echo_task._model)
    result = echo_task.run(input, tracer=NoOpTracer())

    assert len(tokens) == len(result.tokens_with_log_probs)

    assert all([isinstance(t, TokenWithLogProb) for t in result.tokens_with_log_probs])
    for token, result_token in zip(tokens, result.tokens_with_log_probs, strict=True):
        assert token == result_token.token


def test_run_concurrently_produces_proper_completion_prompts(
    client: AlephAlphaClientProtocol, echo_input: EchoInput
) -> None:
    echo_task = Echo(FakeCompleteTaskModel("luminous-base-control", client))
    # if this test fails in CI you may need to increase the 50 to 1000 to reproduce this locally
    echo_task.run_concurrently([echo_input] * MAX_CONCURRENCY * 50, NoOpTracer())
