Data Science Project Template
===

This project uses:
- Docker
  - [hadolint](https://github.com/hadolint/hadolint)
- Python (3.10)
  - Poetry
  - Jupyter Lab
  - hydra
  - mlflow

## Usages
- Docker build
```
$ docker build -t data-project .
```

- Run
```
$ docker run --rm data-project -v $PWD:/app poetry run python main.py [model=linear] [model.alpha=1] ...
```
- Multi-run
```
$ docker run --rm data-project -v $PWD:/app poetry run python main.py --multirun [model=linear] [model.alpha=1] ...
```

- mlflow
```
$ docker run --rm data-project -v $PWD:/app poetry run mlflow ui
```
