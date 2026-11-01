"""FastAPI application factory and ASGI entrypoint."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from foundation_python_project_layout import __version__
from foundation_python_project_layout.api.routes import router
from foundation_python_project_layout.config import Settings, get_settings
from foundation_python_project_layout.logging import configure_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage startup and shutdown."""
    logger.info("Application started", extra={"environment": app.state.settings.environment})
    yield
    logger.info("Application stopped")


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build and configure the FastAPI application."""
    settings = settings or get_settings()
    configure_logging(settings)

    app = FastAPI(
        title=settings.name,
        version=__version__,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )
    app.state.settings = settings
    app.include_router(router)
    return app


app = create_app()
