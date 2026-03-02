# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NVIDIA AI Workbench Onboarding Tutorial — an interactive Streamlit app (Python 3.10) that runs inside an AI Workbench container and teaches users how to use Workbench through hands-on exercises.

## Common Commands

All commands run from `code/tutorial_app/` inside the container.

```bash
# Run the tutorial app
export PROXY_PREFIX=""
streamlit run streamlit_app.py --server.baseUrlPath=$PROXY_PREFIX
# App runs on port 8501

# Install dependencies
pip install -r requirements.txt

# Lint
pylint <module>
flake8 <module>
mypy <module>

# Run a single test file (no pytest — tests are standalone scripts)
python pages/basic_01_tests.py
python pages/overview_tests.py

# Scaffold a new tutorial page from templates
ansible-playbook new_page.run
```

## Code Style

- **Black** formatter, line length 120
- **isort** with `--profile black`
- **pylint**, **flake8**, **mypy** — configured in `pyproject.toml`
- `print()` and `input()` are flagged as bad builtins by pylint
- All Python files must start with the Apache 2.0 SPDX license header (copyright NVIDIA CORPORATION & AFFILIATES)

## Architecture

### Three-File Page Pattern

Every tutorial page is a triad in `code/tutorial_app/pages/`:

| File | Purpose |
|------|---------|
| `<page>.py` | Streamlit UI — loads messages, iterates tasks, runs tests, renders nav |
| `<page>.en_US.yaml` | All user-visible text, task definitions, error message keys (i18n-ready) |
| `<page>_tests.py` | Validation functions that poll Workbench state via GraphQL |

Page files follow a near-identical template (see `pages_templates/*.j2`). The `.py` file loads its YAML via `localization.load_messages(__file__)`, which resolves the locale-suffixed YAML file (falling back to `en_US`).

### Test-as-Validator System

Tests are **not** pytest tests. They are validator functions that check live Workbench environment state:
- On success: return normally (result is cached in Streamlit session state by `testing.run_test()`)
- On failure: raise `testing.TestFail("message_key")` where the key maps to a localized string in the page's YAML
- The Streamlit UI auto-refreshes every 2.5s, re-running validators until they pass

Helper functions in `common/testing.py` provide reusable checks: `ensure_build_state()`, `ensure_run_state()`, `ensure_app_state()`, `ensure_package()`, `get_file()`, `get_folder()`, `ensure_gpu_count()`, etc.

### Workbench Service Client (`common/wb_svc_client.py`)

Communicates with the Workbench daemon via raw GraphQL queries over:
- Unix socket at `/wb-svc-ro.socket` (production, inside container)
- HTTP API at `$NVWB_API` (development, outside container)

### Theme Context Manager (`common/theme.py`)

Every page wraps content in `with theme.Theme():` which handles:
- Loading persisted progress from `/project/data/scratch/tutorial_state.json`
- Setting up 2.5s auto-refresh polling
- Rendering the sidebar
- Saving session state on exit

### Navigation (`pages/sidebar.yaml` + `common/sidebar.py`)

`sidebar.yaml` defines the nav tree (sections, pages, external links, progress indicators). Parsed by the `Sidebar` Pydantic model in `common/sidebar.py`.

## Project Layout

- `code/` — git-tracked source code
- `data/` — gitignored runtime data (includes persisted tutorial state)
- `models/` — git-lfs tracked (currently empty)
- `.project/spec.yaml` — Workbench project spec (container image, apps, ports, resources)
- `apt.txt` — system packages installed at container build time
- `preBuild.bash` / `postBuild.bash` — container build hooks

## Naming Conventions

- Pages: `basic_01`, `advanced_02` (snake_case + numeric suffix)
- Tests: `<page>_tests.py` (not `test_<page>.py`)
- Content: `<page>.en_US.yaml`
- Test functions: descriptive verbs like `check_folder_exists`, `wait_for_jupyterlab_start`
