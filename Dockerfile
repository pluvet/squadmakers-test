FROM python:3.8.13
LABEL maintainer="Pedro Ochoa"

RUN mkdir -p /app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /app/

WORKDIR /app/

RUN poetry install --no-root

RUN mkdir -p /source

COPY ./source /app/source
