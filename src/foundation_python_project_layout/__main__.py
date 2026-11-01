"""Run the API server: ``python -m foundation_python_project_layout``."""

from __future__ import annotations

import uvicorn

from foundation_python_project_layout.config import get_settings


def main() -> None:
    """Start uvicorn with settings-driven host and port."""
    settings = get_settings()
    uvicorn.run(
        "foundation_python_project_layout.main:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower(),
    )


if __name__ == "__main__":
    main()
