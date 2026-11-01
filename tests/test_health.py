"""HTTP probe endpoints."""

from __future__ import annotations

from fastapi.testclient import TestClient

from foundation_python_project_layout import __version__


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready(client: TestClient) -> None:
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_ping(client: TestClient) -> None:
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    assert response.json() == {
        "pong": "foundation-python-project-layout",
        "version": __version__,
        "environment": "local",
    }
