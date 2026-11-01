"""Shared pytest fixtures."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from foundation_python_project_layout.config import Settings
from foundation_python_project_layout.main import create_app


@pytest.fixture
def settings() -> Settings:
    return Settings(environment="local", log_json=True)


@pytest.fixture
def client(settings: Settings) -> TestClient:
    return TestClient(create_app(settings))
