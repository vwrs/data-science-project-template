FROM python:3.10.10-bullseye

WORKDIR /app
# poetry
ENV POETRY_HOME $HOME/.poetry
ENV PATH $PATH:$POETRY_HOME/bin

COPY pyproject.toml poetry.lock ./
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN $POETRY_HOME/bin/poetry config virtualenvs.create false && \
    $POETRY_HOME/bin/poetry install --no-interaction --no-ansi --no-root
