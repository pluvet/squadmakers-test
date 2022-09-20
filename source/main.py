from fastapi import FastAPI
from source.adapters.controllers.joke import joke_router, search_router
from source.adapters.controllers.math import math_router

app = FastAPI()

app.include_router(joke_router, prefix='/jokes')
app.include_router(search_router, prefix='/search')
app.include_router(math_router, prefix='/maths')