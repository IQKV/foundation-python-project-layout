"""Settings loading and environment overrides."""

from __future__ import annotations

from pytest import MonkeyPatch

from foundation_python_project_layout.config import Settings


def test_defaults() -> None:
    settings = Settings()
    assert settings.name == "foundation-python-project-layout"
    assert settings.environment == "local"
    assert settings.port == 8080
    assert settings.log_json is False


def test_env_prefix_overrides(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENVIRONMENT", "prd")
    monkeypatch.setenv("APP_PORT", "9999")
    monkeypatch.setenv("APP_LOG_JSON", "true")

    settings = Settings()
    assert settings.environment == "prd"
    assert settings.port == 9999
    assert settings.log_json is True
