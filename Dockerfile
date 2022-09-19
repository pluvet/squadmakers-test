FROM python:3.8.13
LABEL maintainer="Pedro Ochoa"

RUN pip install poetry
RUN mkdir -p /app

WORKDIR /app

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry install

COPY . .