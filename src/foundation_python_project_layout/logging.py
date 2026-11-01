"""Structured logging setup.

Console output by default; single-line JSON when ``APP_LOG_JSON=true`` so logs
can be shipped to a collector unchanged.
"""

from __future__ import annotations

import json
import logging
import sys
from datetime import UTC, datetime

from foundation_python_project_layout.config import Settings

# Attributes every LogRecord carries; excluded from the JSON payload so only
# caller-supplied `extra=` fields are emitted alongside the core fields.
_RESERVED: frozenset[str] = frozenset(
    logging.LogRecord(name="", level=0, pathname="", lineno=0, msg="", args=(), exc_info=None).__dict__
) | {"message", "asctime", "taskName"}


class JsonFormatter(logging.Formatter):
    """Render log records as single-line JSON."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        payload.update(
            {key: value for key, value in record.__dict__.items() if key not in _RESERVED and not key.startswith("_")}
        )
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, default=str)


def configure_logging(settings: Settings) -> None:
    """Configure root logging once for the running process."""
    handler = logging.StreamHandler(sys.stdout)
    if settings.log_json:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)s: %(message)s"))

    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(settings.log_level.upper())
