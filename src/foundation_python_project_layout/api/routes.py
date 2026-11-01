"""Service routers.

Probes (``/health``, ``/ready``) are what containers and orchestrators call.
The ``/api/v1`` subtree is where domain endpoints belong — add a new module per
bounded context and include its router in :func:`foundation_python_project_layout.main.create_app`.
"""

from __future__ import annotations

from fastapi import APIRouter

from foundation_python_project_layout import __version__
from foundation_python_project_layout.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health", summary="Liveness probe")
async def health() -> dict[str, str]:
    """Report that the process is up."""
    return {"status": "ok"}


@router.get("/ready", summary="Readiness probe")
async def ready() -> dict[str, str]:
    """Report that the service is ready to receive traffic."""
    return {"status": "ready"}


@router.get("/api/v1/ping", tags=["ping"], summary="Ping")
async def ping() -> dict[str, str]:
    """Echo basic service identity — handy for smoke tests."""
    settings = get_settings()
    return {
        "pong": settings.name,
        "version": __version__,
        "environment": settings.environment,
    }
