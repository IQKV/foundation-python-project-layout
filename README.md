# Project Name 🚀

<!-- TEMPLATE: Copy parts of this file into your real README.md and replace the placeholders. -->

<details>
  <summary><strong>How to use this template (click to expand)</strong></summary>

1. Rename the title above to your project name and optionally add a logo below it.
2. Add badges (CI, tests, coverage, license) under the title.
3. Fill each section below with your actual project content.
4. Replace placeholder commands and code blocks with real ones.
5. Remove this guidance block when you are done.

</details>

> **One-line value proposition** — what problem does this solve and who is it for?

[![CI](https://github.com/IQKV/foundation-python-project-layout/actions/workflows/build-python-project.yml/badge.svg)](https://github.com/IQKV/foundation-python-project-layout/actions/workflows/build-python-project.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)

---

## 🎯 What Is This?

Two or three sentences describing the project:

- **🎯 Purpose**: what it does (not how)
- **💡 Key benefit**: why someone should care
- **✅ Status**: production-ready, experimental, or in development
- **🔧 Use case**: when to use it

## ⚡ Quick Start

```bash
git clone https://github.com/IQKV/foundation-python-project-layout.git
cd foundation-python-project-layout

uv sync
cp .env.example .env
uv run python -m foundation_python_project_layout
```

## 📖 Usage

Show the simplest useful example, then common scenarios.

```python
from foundation_python_project_layout.config import get_settings

settings = get_settings()
```

## 🏗️ Architecture

Briefly describe the components and how a request flows through them. See
[docs/architecture/README.md](docs/architecture/README.md) for detail.

## 🔧 Configuration

Document every environment variable (all use the `APP_` prefix) and any config files.

## 🧪 Development

```bash
uv run ruff format .
uv run ruff check .
uv run mypy
uv run pytest --cov
```

## 📜 License

Apache License 2.0 — see [LICENSE](LICENSE).
