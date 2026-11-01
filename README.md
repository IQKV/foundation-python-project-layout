# Foundation Python Project Layout 🚀

GitHub template for bootstrapping Python microservices on the iQ Key Value platform. Provides a standardized `src/` layout with a FastAPI app factory, `uv`-managed dependencies, typed multi-environment configuration, and all quality tooling pre-wired.

## About

This template gives you a production-ready starting point:

- **`src/` layout** — installable package (`foundation_python_project_layout`) with `pyproject.toml` and a committed `uv.lock`
- **FastAPI app factory** — `create_app()` with lifespan hooks; ASGI served by Uvicorn
- **Typed configuration** — `pydantic-settings` with an `APP_` env prefix and `.env` support; `local`, `sit`, `uat`, `prd` environments
- **Structured logging** — console format locally, single-line JSON in containers (`APP_LOG_JSON=true`)
- **Health probes** — `/health` (liveness) and `/ready` (readiness) endpoints out of the box
- **Dockerfile** — multi-stage build on `python:3.13-slim`, non-root `appuser`, urllib-based healthcheck
- **Docker Compose** — `compose.yaml` builds the `runtime` target and publishes port `8080`
- **Quality tools** — ruff (lint + format), mypy (strict), pytest + coverage, Husky git hooks, commitlint
- **CI** — GitHub Actions quality/test/docker jobs on `astral-sh/setup-uv`; Dependabot for uv, Docker, and Actions

## Template Usage

1. Click **[Use this template](https://github.com/IQKV/foundation-python-project-layout/generate)** to create your repository
2. Replace all `foundation-python-project-layout` / `foundation_python_project_layout` occurrences with your project name (see [`scaffolding.md`](scaffolding.md))
3. Update `pyproject.toml` — `name`, `description`, `keywords`, and the `[project.scripts]` entry
4. Rename the package under `src/` and update the imports
5. Update this `README.md` — see `README.template.md` for the target structure

## Quick Links

- [API Documentation](./docs/api/README.md)
- [Architecture Overview](./docs/architecture/README.md)
- [Deployment Guide](./docs/deployment/README.md)
- [Contributing Guidelines](.github/CONTRIBUTING.md)

## Tech Stack

- Python 3.13+ with `uv` for dependency management
- FastAPI + Uvicorn (ASGI)
- pydantic-settings for typed configuration
- ruff (lint + format), mypy (strict), pytest + pytest-cov
- Docker / Docker Compose

## Prerequisites

- Python 3.13+
- uv (dependency management)
- Node.js >= 22.13.0 & pnpm (git hooks)
- Docker & Docker Compose

## Quick Start

```bash
# Clone / use template
git clone https://github.com/IQKV/foundation-python-project-layout.git my-service
cd my-service

# Install dependencies
uv sync

# Install git hooks
pnpm install

# Copy environment variables
cp .env.example .env
# Edit .env — defaults work for local development

# Run the service
uv run python -m foundation_python_project_layout
# → API:      http://localhost:8080
# → Swagger:  http://localhost:8080/docs
# → Ping:     http://localhost:8080/api/v1/ping
```

## Environment Variables

| Variable          | Default                            | Description                      |
| ----------------- | ---------------------------------- | -------------------------------- |
| `APP_NAME`        | `foundation-python-project-layout` | Service name                     |
| `APP_VERSION`     | package version                    | Reported version                 |
| `APP_ENVIRONMENT` | `local`                            | One of `local`/`sit`/`uat`/`prd` |
| `APP_LOG_LEVEL`   | `INFO`                             | Root log level                   |
| `APP_LOG_JSON`    | `false`                            | Emit single-line JSON logs       |
| `APP_HOST`        | `0.0.0.0`                          | Bind host                        |
| `APP_PORT`        | `8080`                             | Bind port                        |

> Copy `.env.example` to `.env` and fill in values per environment.

## Commands

```bash
# Run the service
uv run python -m foundation_python_project_layout

# Dev server with autoreload
uv run uvicorn foundation_python_project_layout.main:app --reload

# Lint, format, type-check
uv run ruff format --check .
uv run ruff check .
uv run mypy

# Tests with coverage → coverage.xml + terminal report
uv run pytest --cov

# Build distribution (wheel + sdist) into dist/
uv build
```

## Docker

```bash
# Build image
docker build -t iqkv/foundation-python-project-layout:latest .

# Run full stack (service container)
docker compose up --build
```

## Endpoints

| Endpoint           | Description                   |
| ------------------ | ----------------------------- |
| `GET /health`      | Liveness probe                |
| `GET /ready`       | Readiness probe               |
| `GET /api/v1/ping` | Service identity / smoke test |
| `GET /docs`        | Swagger UI                    |

## Project Structure

```
.
├── src/foundation_python_project_layout/
│   ├── api/            # Routers — one module per bounded context
│   │   └── routes.py
│   ├── __main__.py     # `python -m foundation_python_project_layout`
│   ├── config.py       # Typed settings (pydantic-settings, APP_ prefix)
│   ├── logging.py      # Console / JSON logging setup
│   └── main.py         # FastAPI app factory + lifespan
├── tests/              # pytest suite (TestClient based)
├── docs/               # api / architecture / deployment guides
├── Dockerfile
├── compose.yaml
└── pyproject.toml
```

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Branch Strategy

> **Template note:** This is the default strategy shipped with the template. Replace it with whatever model fits your team (Gitflow, GitHub Flow, environment branches, etc.) — update branch names, CI triggers, and protection rules to match.

This template uses **scaled trunk-based development**:

- `dev` is the trunk — always stable and deployable
- Short-lived feature/bugfix branches merge into `dev` via pull request
- Releases are cut from `dev` as annotated tags (`v1.2.0`) — no separate release branch

```
dev  ← trunk
├── feature/*
├── bugfix/*
├── improvement/*
├── hotfix/*
└── rfc/*
```

## Contributing

Please read our [Contributing Guidelines](.github/CONTRIBUTING.md) and [Code of Conduct](.github/CODE_OF_CONDUCT.md).

---

## 🧩 Boilerplate Architecture

- **Application**: FastAPI app factory (`create_app`) with an async lifespan; Uvicorn as the ASGI server
- **Configuration**: `pydantic-settings` with an `APP_` env prefix and `.env` loading; nothing is hardcoded
- **Logging**: stdlib logging configured once at startup — console locally, single-line JSON in containers
- **Probes**: `/health` and `/ready` for container and orchestrator health checks
- **Packaging**: `src/` layout, hatchling build backend, committed `uv.lock`; wheel + sdist via `uv build`
- **Containers**: multi-stage Dockerfile on `python:3.13-slim` with a non-root runtime user
- **Quality Tools**: ruff, mypy (strict), pytest + coverage, commit convention enforcement

> See [AGENTS.md](AGENTS.md) for repository structure and agent guidelines.
