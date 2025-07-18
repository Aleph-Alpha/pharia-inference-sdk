import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from time import sleep
from typing import cast

import pytest
from aleph_alpha_client import BusyError, CompletionRequest, CompletionResponse, Prompt
from pytest import fixture

from pharia_inference_sdk.connectors.limited_concurrency_client import (
    AlephAlphaClientProtocol,
    LimitedConcurrencyClient,
)


class ConcurrencyCountingClient:
    max_concurrency_counter: int = 0
    concurrency_counter: int = 0

    def __init__(self) -> None:
        self.lock = Lock()

    def complete(self, request: CompletionRequest, model: str) -> CompletionResponse:
        with self.lock:
            self.concurrency_counter += 1
            self.max_concurrency_counter = max(
                self.max_concurrency_counter, self.concurrency_counter
            )
        sleep(0.01)
        with self.lock:
            self.concurrency_counter -= 1
        return CompletionResponse(
            model_version="model-version",
            completions=[],
            optimized_prompt=None,
            num_tokens_generated=0,
            num_tokens_prompt_total=0,
        )


class BusyClient:
    def __init__(
        self, return_value: CompletionResponse | Exception, wait_time: int | None = None
    ) -> None:
        self.number_of_retries: int = 0
        self.return_value = return_value
        self.wait_time = wait_time

    def complete(self, request: CompletionRequest, model: str) -> CompletionResponse:
        self.number_of_retries += 1
        if self.wait_time:
            time.sleep(self.wait_time)
        if self.number_of_retries < 2:
            raise BusyError(503)
        else:
            if isinstance(self.return_value, Exception):
                raise self.return_value
            else:
                return self.return_value


TEST_MAX_CONCURRENCY = 3


@fixture
def concurrency_counting_client() -> ConcurrencyCountingClient:
    return ConcurrencyCountingClient()


@fixture
def limited_concurrency_client(
    concurrency_counting_client: ConcurrencyCountingClient,
) -> LimitedConcurrencyClient:
    return LimitedConcurrencyClient(
        cast(AlephAlphaClientProtocol, concurrency_counting_client),
        TEST_MAX_CONCURRENCY,
    )


def test_methods_concurrency_is_limited(
    limited_concurrency_client: LimitedConcurrencyClient,
    concurrency_counting_client: ConcurrencyCountingClient,
) -> None:
    with ThreadPoolExecutor(max_workers=TEST_MAX_CONCURRENCY * 10) as executor:
        executor.map(
            limited_concurrency_client.complete,
            [CompletionRequest(prompt=Prompt(""))] * TEST_MAX_CONCURRENCY * 10,
            ["model"] * TEST_MAX_CONCURRENCY * 10,
        )
    assert concurrency_counting_client.max_concurrency_counter == TEST_MAX_CONCURRENCY


def test_limited_concurrency_client_retries() -> None:
    expected_completion = CompletionResponse(
        model_version="model-version",
        completions=[],
        optimized_prompt=None,
        num_tokens_generated=0,
        num_tokens_prompt_total=0,
    )
    busy_client = BusyClient(return_value=expected_completion)
    limited_concurrency_client = LimitedConcurrencyClient(
        cast(AlephAlphaClientProtocol, busy_client)
    )
    completion = limited_concurrency_client.complete(
        CompletionRequest(prompt=Prompt("")), "model"
    )
    assert completion == expected_completion


def test_limited_concurrency_client_stops_retrying_after_max_retry() -> None:
    expected_completion = CompletionResponse(
        model_version="model-version",
        completions=[],
        optimized_prompt=None,
        num_tokens_generated=0,
        num_tokens_prompt_total=0,
    )
    busy_client = BusyClient(return_value=expected_completion)
    limited_concurrency_client = LimitedConcurrencyClient(
        cast(AlephAlphaClientProtocol, busy_client), max_retry_time=1
    )
    with pytest.raises(BusyError):
        limited_concurrency_client.complete(
            CompletionRequest(prompt=Prompt("")), "model"
        )


def test_limited_concurrency_client_handles_long_running_functions_properly() -> None:
    expected_completion = CompletionResponse(
        model_version="model-version",
        completions=[],
        optimized_prompt=None,
        num_tokens_generated=0,
        num_tokens_prompt_total=0,
    )
    busy_client = BusyClient(return_value=expected_completion, wait_time=1)
    limited_concurrency_client = LimitedConcurrencyClient(
        cast(AlephAlphaClientProtocol, busy_client), max_retry_time=1
    )
    with pytest.raises(BusyError):
        limited_concurrency_client.complete(
            CompletionRequest(prompt=Prompt("")), "model"
        )


def test_limited_concurrency_client_throws_exception() -> None:
    expected_exception = Exception(404)
    busy_client = BusyClient(return_value=expected_exception)
    limited_concurrency_client = LimitedConcurrencyClient(
        cast(AlephAlphaClientProtocol, busy_client)
    )
    with pytest.raises(Exception) as exception_info:
        limited_concurrency_client.complete(
            CompletionRequest(prompt=Prompt("")), "model"
        )
    assert exception_info.value == expected_exception
