"""JSON log formatting."""

from __future__ import annotations

import json
import logging

from foundation_python_project_layout.logging import JsonFormatter


def _record(**extra: object) -> logging.LogRecord:
    record = logging.LogRecord(
        name="test", level=logging.INFO, pathname=__file__, lineno=1, msg="hello %s", args=("world",), exc_info=None
    )
    for key, value in extra.items():
        setattr(record, key, value)
    return record


def test_formats_core_fields() -> None:
    payload = json.loads(JsonFormatter().format(_record()))
    assert payload["level"] == "INFO"
    assert payload["logger"] == "test"
    assert payload["message"] == "hello world"
    assert payload["timestamp"]


def test_includes_extra_fields_and_drops_reserved() -> None:
    payload = json.loads(JsonFormatter().format(_record(environment="local")))
    assert payload["environment"] == "local"
    assert "pathname" not in payload
    assert "lineno" not in payload
