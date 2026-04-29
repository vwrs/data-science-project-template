# Data Science Project Template

This project uses:
- Python (3.14)
  - uv
  - Jupyter Lab
  - hydra
  - mlflow
- Docker
  - [hadolint](https://github.com/hadolint/hadolint)

## Usages

- Install
```
$ uv sync
```

- Install with development tools
```
$ uv sync --group dev
```

- Run
```
$ uv run python main.py [model=linear] [model.alpha=1] ...
```

- Multi-run
```
$ uv run python main.py --multirun model.alpha=0,0.2,0.5,0.7,1 model.l1_ratio=0,0.2,0.5,0.7,1
```

- MLflow
```
$ uv run mlflow ui
Listening at: http://127.0.0.1:5000
```

## Lint & Format

This project uses [Ruff](https://docs.astral.sh/ruff/) for both linting and formatting. Ruff is installed through the `dev` dependency group and pinned in `pyproject.toml`.

- Check lint
```
$ uv run ruff check .
```

- Apply lint fixes
```
$ uv run ruff check . --fix
```

- Check formatting
```
$ uv run ruff format --check .
```

- Format files
```
$ uv run ruff format .
```

Notebook files are excluded from the default Ruff target because this repository keeps exploratory notebooks separate from the Python source workflow.

<img width="1156" alt="mlflow-demo" src="https://user-images.githubusercontent.com/12569381/226176330-a0ee5a95-8ba6-4532-8ca2-3b12c7ee9974.png">

### Run in Docker
- Build
```
$ docker build -t data-project .
```

- Run
```
$ docker run --rm -v $PWD:/app data-project uv run <command>
```
