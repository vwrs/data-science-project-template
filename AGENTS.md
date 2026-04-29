# Repository Guidelines

## Project Structure & Module Organization

This is a compact Python data science template. The runnable entry point is `main.py`, which loads Hydra configuration from `conf/config.yaml` and delegates training to `predict.py`. Model-specific configuration lives under `conf/model/`, currently `conf/model/linear.yaml`. Keep raw or local datasets under `data/`; the directory is tracked with `.gitkeep` but data files should generally stay out of git. Put exploratory notebooks in `notebooks/` or use the existing root notebook only for experiments. MLflow outputs are written to `mlruns/` and Hydra multirun outputs to `multirun/`.

## Build, Test, and Development Commands

- `uv sync`: install the Python environment from `pyproject.toml` and `uv.lock`.
- `uv run python main.py`: run the default training workflow.
- `uv run python main.py model=linear model.alpha=0.5`: run with Hydra overrides.
- `uv run python main.py --multirun model.alpha=0,0.5,1 model.l1_ratio=0,0.5,1`: launch a parameter sweep.
- `uv run mlflow ui`: inspect local MLflow runs at `http://127.0.0.1:5000`.
- `docker build -t data-project .`: build the container image; verify the Dockerfile before relying on it because it still references Poetry-era files.

## Coding Style & Naming Conventions

Use Python 3.14 as declared in `.python-version` and `pyproject.toml`. Follow PEP 8 with 4-space indentation, `snake_case` for functions and variables, and `PascalCase` for classes such as `Predictor`. Prefer small functions that separate data loading, training, evaluation, and logging. Keep Hydra keys lowercase and descriptive, and add new model configs as `conf/model/<model_name>.yaml`.

## Testing Guidelines

There is no test suite yet. Add tests under `tests/` when changing training logic, config handling, or metric calculations. Use `pytest` conventions: files named `test_*.py`, functions named `test_*`, and focused fixtures for sample data. Until tests exist, verify changes with `uv run python main.py` and, for config changes, at least one Hydra override run.

## Commit & Pull Request Guidelines

Recent history uses short messages, with some Conventional Commit prefixes such as `style:` and `fix:`. Prefer `type: imperative summary`, for example `fix: handle missing training data` or `docs: update mlflow instructions`. Pull requests should include the purpose of the change, commands run, any Hydra parameters used for validation, and screenshots only when MLflow UI or notebook output changes.

## Security & Configuration Tips

Do not commit private datasets, credentials, MLflow artifacts, or large generated outputs. Keep secrets in local environment variables or ignored files. When adding remote data sources, document the URL, expected schema, and failure behavior near the loader or in the README.
