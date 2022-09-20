## How to run the application
1. Spin up the containers
```bash
docker-compose up -d --build
```
2. Check the API docs on http://localhost:8700/docs

## Run the test
1. Install dependencies with poetry
```bash
poetry install
```
2. Run the test
```bash
poetry run make test
```

## ¿Por que se eligio elasticsearch como repositorio?
Yo elegi elasticsearch porque al ser una api basada en guardar chistes 
decidi que era necesario tener una busqueda de texto mas completa 
para poder buscar realizar busquedas de chistes de una manera avanzada

