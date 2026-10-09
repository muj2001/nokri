# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

Nokri is a Python 3.13 project managed with `uv`. Its first milestone is to collect job postings from sources such as Greenhouse and Lever and preserve raw responses in Cloudflare R2. Enrichment and a database schema are later work. The ingestion pipeline and R2 integration are not implemented yet.

## Commands

- `uv sync` — create the local environment and install the project.
- `uv run nokri` — run the current placeholder CLI (prints a greeting; it does not ingest jobs).
- `uv build` — build the package via the configured `uv_build` backend.
- `uv run python -m unittest discover -s tests` — discover standard-library tests; `tests/` currently has no test cases. Once a `unittest` test exists, run one with `uv run python -m unittest tests.<module>.<TestClass>.<test_method>`.

No lint tool or test framework dependency is configured in `pyproject.toml` yet.

## Architecture and documentation

The installable package is `src/nokri`; `pyproject.toml` maps the `nokri` command to `nokri:main` in `src/nokri/__init__.py`. The CLI, ingestion orchestration, source adapters, and R2 storage modules are present as empty scaffolds. Do not describe them as working integrations.

`docs/sources/` records external API contracts only: endpoints, parameters, responses, authentication, and documented API constraints. Keep Nokri-specific collection choices and storage decisions out of those source references; project goals belong in `README.md`, while local environment instructions belong in `SETUP.md`.
