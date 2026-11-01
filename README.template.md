# Project Name 🚀

<!-- TEMPLATE: This README.template.md is a starter template. Copy parts into your real README.md and replace placeholders. -->

<details>
  <summary><strong>How to use this template (click to expand)</strong></summary>

1. Rename the title above to your project name and optionally add a logo right below it.
2. Add badges (build, tests, coverage, license) under the title.
3. Fill each section below with your actual project content (keep the section order if you like it).
4. Replace placeholder code blocks and bullet points with real commands and steps.
5. Keep the "Template Usage" links if you want quick access to template docs, or remove them in your final README.md.
6. Remove this guidance block after you finish customizing.

</details>

- Add your project logo.
- Write a short introduction to the project.
- If you are using badges, add them here.

<details>
  <summary><strong>Badge examples (optional)</strong></summary>

- Build: <code>![CI](https://img.shields.io/github/actions/workflow/status/ORG/REPO/ci.yml?label=CI)</code>
- Tests: <code>![Tests](https://img.shields.io/badge/tests-passing-brightgreen)</code>
- Coverage: <code>![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)</code>
- License: <code>![License](https://img.shields.io/github/license/ORG/REPO)</code>

</details>

## :beginner: About

Add a detailed introduction about the project here, everything you want the reader to know.

## 📚 Documentation

- [API Documentation](docs/api/README.md)
- [Architecture Overview](docs/architecture/README.md)
- [Deployment Guide](docs/deployment/README.md)
- [Contributing Guidelines](.github/CONTRIBUTING.md)

---

<details>
  <summary><strong>✅ Pre-publish checklist (remove in final README)</strong></summary>

- [ ] Title updated and logo added
- [ ] Badges added (CI, tests, coverage, license)
- [ ] About/Usage/Installation/Commands completed
- [ ] Development prerequisites and environment documented
- [ ] Architecture notes reflect your stack and modules
- [ ] Links verified (Getting Started, docs, external resources)

</details>

---

## 🧩 Boilerplate Architecture

- **Application**: FastAPI app factory (`create_app`) with an async lifespan; Uvicorn as the ASGI server
- **Configuration**: `pydantic-settings` with an `APP_` env prefix and `.env` loading; nothing is hardcoded
- **Logging**: stdlib logging configured once at startup — console locally, single-line JSON in containers
- **Probes**: `/health` and `/ready` for container and orchestrator health checks
- **Containers**: Multi-stage Dockerfile on `python:3.13-slim` with a non-root runtime user
- **Packaging**: `src/` layout with a committed `uv.lock`; wheel + sdist via `uv build`
- **Quality Tools**: ruff, mypy (strict), pytest + coverage, and conventional commits

> See [AGENTS.md](AGENTS.md) for detailed project structure and agent guidelines.
