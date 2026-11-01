## 📜 Architecture Overview

A single-service, containerized FastAPI application. The layout keeps transport,
configuration, and domain logic separate so a bounded context can grow without
touching the others.

```
                 ┌──────────────────────────────┐
  HTTP request ─▶│  FastAPI app (main.create_app)│
                 └───────────────┬──────────────┘
                                 │ includes
                 ┌───────────────▼──────────────┐
                 │  api/routes.py + domain routers│
                 └───────────────┬──────────────┘
                                 │ uses
                 ┌───────────────▼──────────────┐
                 │  config.Settings  │  logging  │
                 └──────────────────────────────┘
```

### Layers

- **`main.py`** — builds the FastAPI application, wires the lifespan and routers.
  Exposes `app` for `uvicorn foundation_python_project_layout.main:app`.
- **`api/`** — routers and Pydantic schemas. One module per bounded context,
  included from `create_app()`.
- **`config.py`** — typed settings via `pydantic-settings`. All values come from
  `APP_`-prefixed environment variables or `.env`; nothing is hardcoded.
- **`logging.py`** — configures root logging once at startup: console format
  locally, single-line JSON when `APP_LOG_JSON=true`.

### Configuration

Settings are read once (`get_settings()`, cached) and attached to `app.state`, so
handlers and lifespan code share a single frozen view of the environment.

### Logging

Use the stdlib logger with `extra=` for structured fields — they are emitted as
top-level JSON keys in container mode:

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Ticket checked", extra={"origin": "CAI", "destination": "JFK"})
```

### Extending

1. Create `src/foundation_python_project_layout/<context>/` with the domain logic.
2. Add a router under `api/` (or in the context package) and include it in
   `create_app()`.
3. Add tests under `tests/` mirroring the module path.

### Testing

- Unit tests use the FastAPI `TestClient` and plain `pytest` (no live server).
- Build the app with an explicit `Settings` instance in tests to avoid reading a
  developer's local `.env`.
