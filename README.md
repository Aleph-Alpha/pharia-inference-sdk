# Core SDK
Formally the `intelligence_layer/core` package.

## Requirements
- [uv](https://docs.astral.sh/uv/)
- Python 3.12

## Setup

```bash
uv venv
uv sync
```

## Run tests

```bash
# make sure jaeger is running
docker compose up -d

# run tests
uv run pytest
```


## TODO list
- [x] Add ruff linting
- [ ] Add build step 
- [ ] add docs
- [ ] Figure out what to do with `LimitedConcurrencyClient`
- [ ] setup renovatebot 
- [ ] setup CI/CD 
   - [ ] Add release-please 