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
- Install
```
$ poetry install
```

- Run
```
$ docker run --rm -v $PWD:/app data-project poetry run python main.py [model=linear] [model.alpha=1] ...
```

- Multi-run
```
$ poetry run python main.py --multirun model.alpha=0,0.2,0.5,0.7,1 model.l1_ratio=0,0.2,0.5,0.7,1
```

- mlflow
```
$ poetry run mlflow ui
```

### Run in Docker
- Build
```
$ docker build -t data-project .
```

- Run
```
$ docker run --rm -v $PWD:/app data-project poetry run <command>
```

