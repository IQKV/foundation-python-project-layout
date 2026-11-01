"""Application configuration, loaded from environment variables and ``.env``."""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from foundation_python_project_layout import __version__

Environment = Literal["local", "sit", "uat", "prd"]


class Settings(BaseSettings):
    """Runtime settings for the service.

    Every field maps to an ``APP_``-prefixed environment variable, e.g.
    ``APP_PORT`` overrides :attr:`port`.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )

    name: str = "foundation-python-project-layout"
    version: str = __version__
    environment: Environment = "local"
    log_level: str = "INFO"
    log_json: bool = False
    host: str = "0.0.0.0"
    port: int = Field(default=8080, ge=1, le=65535)


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide settings singleton."""
    return Settings()
