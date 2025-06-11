# Contributing to pharia-inference-sdk

## Development Setup

### Prerequisites
- [uv](https://docs.astral.sh/uv/)
- Python 3.12

### Local Development Setup

```bash
git clone https://github.com/pharia-ai/pharia-inference-sdk.git
cd pharia-inference-sdk
```

####  Install dependencies
```bash
uv venv
uv sync
uv run pre-commit install
```

#### Setup environment variables

```bash
cp .env.example .env
```

### Running Tests

```bash
# make sure jaeger is running
docker compose up -d

# run tests
uv run pytest
```