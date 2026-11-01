# Scaffolding a New Service from This Template

Every token that must be replaced when creating a new service from
`foundation-python-project-layout`, and the files that reference it.

---

## Token Map

The example column uses a hypothetical **flight-alerts** service.

| Token                    | Kind                       | Example replacement       |
| ------------------------ | -------------------------- | ------------------------- |
| `foundation-python-project-layout`  | distribution / image name  | `flight-alerts`           |
| `foundation_python_project_layout`  | import package name        | `flight_alerts`           |
| `foundation-python-project-layout`  | console script name        | `flight-alerts`           |

---

## Step-by-Step

### 1. Copy and rename the repository

```bash
cp -r foundation-python-project-layout flight-alerts
cd flight-alerts
```

### 2. Rename the package directory

```bash
git mv src/foundation_python_project_layout src/flight_alerts
```

### 3. Global text replacement

Apply these **in order** — the import package name first, then the slug:

```
foundation_python_project_layout  →  flight_alerts
foundation-python-project-layout  →  flight-alerts
```

Common places: `pyproject.toml`, `src/**/*.py`, `tests/**/*.py`, `Dockerfile`,
`compose.yaml`, `.dockerignore`, `.devcontainer/devcontainer.json`, `README.md`,
`README.template.md`, `docs/**`, `.github/workflows/*.yml`.

### 4. Update `pyproject.toml`

| Field                      | Value                     |
| -------------------------- | ------------------------- |
| `[project].name`           | `flight-alerts`           |
| `[project].description`    | your service description  |
| `[project.scripts]`        | `flight-alerts = "flight_alerts.__main__:main"` |
| `[project.urls]`           | your repository URLs      |
| `[tool.hatch.build...]`    | `packages = ["src/flight_alerts"]` |

### 5. Regenerate the lockfile

```bash
uv lock
uv sync
```

### 6. Verify

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest
docker build -t flight-alerts:local .
```

### 7. Delete this file

```bash
git rm scaffolding.md
```

---

## Checklist

- [ ] Package directory renamed (`src/foundation_python_project_layout` → `src/flight_alerts`)
- [ ] All `foundation_python_project_layout` / `foundation-python-project-layout` occurrences replaced
- [ ] `pyproject.toml` name, description, script, URLs, and wheel package updated
- [ ] `Dockerfile`, `compose.yaml`, `.devcontainer` updated
- [ ] `uv lock` regenerated
- [ ] CI green (ruff, mypy, pytest, docker build)
- [ ] `README.md` rewritten from `README.template.md`
- [ ] `scaffolding.md` deleted
