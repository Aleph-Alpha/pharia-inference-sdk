# Quick Start

This guide will help you get started with the Pharia Inference SDK quickly.

## Installation
The SDK is published on [PyPI](https://pypi.org/project/pharia-inference-sdk/).

To add the SDK as a dependency to an existing project managed, run
```bash
pip install pharia-inference-sdk
```

## Usage

```python
from pharia_inference_sdk.core.tracer import InMemoryTracer
from pharia_inference_sdk.core.model import Llama3InstructModel, Prompt, CompleteInput
from aleph_alpha_client import Client

client=Client(token="<token>", host="<inference-api-url>")
model = Llama3InstructModel(client=client)
tracer = InMemoryTracer()

prompt = Prompt.from_text(text="What is the most common fish in swedish lakes?")
model.complete(CompleteInput(prompt=prompt, maximum_tokens=32), tracer)

# see trace in rich format
tracer._rich_render_()
```

## Next Steps

- Explore the complete [API Reference](references) for detailed documentation
- Check out the [GitHub Repository](https://github.com/Aleph-Alpha/pharia-inference-sdk) for examples
- Visit the [PyPI Package](https://pypi.org/project/pharia-inference-sdk/) page for more information 