import os
from os import getenv
from pathlib import Path
from typing import cast

from aleph_alpha_client import Client, Image
from dotenv import load_dotenv
from pytest import fixture

from pharia_inference_sdk.connectors.limited_concurrency_client import (
    AlephAlphaClientProtocol,
    LimitedConcurrencyClient,
)
from pharia_inference_sdk.core import (
    Llama3InstructModel,
    LuminousControlModel,
    NoOpTracer,
    Pharia1ChatModel,
)


@fixture(scope="session")
def token() -> str:
    load_dotenv()
    token = getenv("AA_TOKEN")
    assert isinstance(token, str)
    return token


@fixture(scope="session")
def inference_url() -> str:
    return os.environ["CLIENT_URL"]


@fixture(scope="session")
def client(token: str, inference_url: str) -> AlephAlphaClientProtocol:
    return LimitedConcurrencyClient(
        Client(token, host=inference_url),
        max_concurrency=10,
        max_retry_time=10,
    )


@fixture(scope="session")
def llama_control_model(client: AlephAlphaClientProtocol) -> Llama3InstructModel:
    return Llama3InstructModel("llama-3.1-8b-instruct", client)


@fixture(scope="session")
def luminous_control_model(client: AlephAlphaClientProtocol) -> LuminousControlModel:
    return LuminousControlModel("luminous-base-control", client)


@fixture(scope="session")
def pharia_1_chat_model(client: AlephAlphaClientProtocol) -> Pharia1ChatModel:
    return Pharia1ChatModel("pharia-1-llm-7b-control", client)


@fixture
def no_op_tracer() -> NoOpTracer:
    return NoOpTracer()


@fixture(scope="session")
def prompt_image() -> Image:
    image_source_path = Path(__file__).parent / "dog-and-cat-cover.jpg"
    return cast(Image, Image.from_file(image_source_path))  # from_file lacks type-hint
