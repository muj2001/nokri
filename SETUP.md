# Setup

Nokri is still a scaffold. The job ingestion pipeline and Cloudflare R2 integration are not implemented yet.

## Prerequisites

- Python 3.13
- `uv`

## Prepare a local environment

From the repository root:

```sh
uv python install 3.13
uv sync
```

This installs the `nokri` package and the default dev dependency group, which currently includes `python-dotenv`. Run `uv run nokri` to check the current placeholder command.

The Greenhouse playground script reads `GREENHOUSE_BOARD_TOKEN` from the environment; for local use, set it in a root `.env` file (ignored by Git). R2 credentials and ingestion instructions will be documented when the pipeline is implemented.
