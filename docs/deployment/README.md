## 📜 Deployment Guide

### Container image

The `Dockerfile` is a multi-stage build:

1. **builder** — resolves dependencies with `uv sync --frozen` into `/app/.venv`
   (dependency layer is cached separately from `src/`), then installs the project.
2. **runtime** — copies the virtualenv into a clean `python:3.13-slim` image and
   runs as the non-root `appuser`.

```bash
docker build -t iqkv/foundation-python-project-layout:latest .

docker run --rm -p 8080:8080 \
  -e APP_ENVIRONMENT=prd \
  -e APP_LOG_JSON=true \
  iqkv/foundation-python-project-layout:latest
```

### Docker Compose

```bash
cp .env.example .env     # optional overrides
docker compose up --build
```

`compose.yaml` builds the `runtime` target and publishes port `8080`.

### Configuration in deployed environments

Inject configuration as environment variables (`APP_` prefix). Recommended
defaults per environment:

| Variable          | prd    |
| ----------------- | ------ |
| `APP_ENVIRONMENT` | `prd`  |
| `APP_LOG_JSON`    | `true` |
| `APP_LOG_LEVEL`   | `INFO` |

Never bake secrets or environment-specific values into the image.

### Health probes

| Probe     | Path      | Use                                  |
| --------- | --------- | ------------------------------------ |
| Liveness  | `/health` | Restart the container if failing     |
| Readiness | `/ready`  | Remove from load balancer if failing |

The image also declares a `HEALTHCHECK` that polls `/health`.

### CI/CD

`.github/workflows/build-python-project.yml` runs on pushes to `dev`/`wip` and on
pull requests to `dev`:

- **quality** — `uv sync --locked`, `ruff format --check`, `ruff check`, `mypy`
- **test** — `pytest` with coverage (uploaded as an artifact)
- **docker** — builds the image to verify the container still builds

Extend the `docker` job with a registry login and `push: true` to publish images
on release tags.
