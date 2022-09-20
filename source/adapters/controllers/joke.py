import json
from uuid import UUID
from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from source.services.joke import JokeService
from source.adapters.repositories.joke.elasticsearch import JokeESRepository
from source.adapters.requests.joke import JokeGetRequest
from source.adapters.models.joke import JokeModel

joke_router = APIRouter()
    
@joke_router.post(
    '/',
    responses={
        201: {
            "description": "Save a joke",
            "content": {
                "application/json": {
                    "example": {"id": "aBckWYMBaE7BXjiRkH5A", "value": "joketext"}
                }
            },
        },
    },
)
async def save(joke: JokeModel) -> JSONResponse:
    """this function save jokes"""

    joke_service = JokeService(JokeESRepository)

    joke = joke_service.save(
        value=joke.value
    )

    return JSONResponse(joke, status_code=201)

@joke_router.get(
    '/',
    responses={
        200: {
            "description": "get a random joke",
            "content": {
                "application/json": {
                    "example": {"id": "aBckWYMBaE7BXjiRkH5A", "value": "joketext"}
                }
            },
        },
    },
)
async def get() -> JSONResponse:
    """gets one random joke"""
    
    joke_service = JokeService(JokeESRepository)

    joke_list = joke_service.get()

    return JSONResponse(joke_list, status_code=200)

@joke_router.get(
    '/{id}',
    responses={
        200: {
            "description": "get a joke from an external api",
            "content": {
                "application/json": {
                    "example": {"id": "aBckWYMBaE7BXjiRkH5A", "value": "joketext"}
                }
            },
        },
    },
)
async def find(id: str) -> JSONResponse:
    """find one joke"""
    
    joke_service = JokeService(JokeESRepository, JokeGetRequest)

    joke = joke_service.find(id)

    return JSONResponse(joke, status_code=200)

@joke_router.put(
    '/{id}',
    responses={
        200: {
            "description": "update a joke by an id",
            "content": {
                "application/json": {
                    "example": {"id": "aBckWYMBaE7BXjiRkH5A", "value": "jokeupdated"}
                }
            },
        },
    },
)
async def update(id: str, joke: JokeModel) -> JSONResponse:
    """update a joke"""
    
    joke_service = JokeService(JokeESRepository)

    joke = joke_service.update(
        id=id,
        value=joke.value
    )

    return JSONResponse(joke, status_code=200)

@joke_router.delete(
    '/{id}',
    responses={
        204: {
            "description": "delete a joke",
            "content": {
                "application/json": {
                    "example": {}
                }
            },
        },
    },
)
def delete(id: str)-> JSONResponse:
    """ delete a joke"""

    joke_service = JokeService(JokeESRepository)

    joke_service.delete(id)

    return JSONResponse(None, status_code=204)

search_router = APIRouter()
@search_router.get(
    '/jokes',
    responses={
        200: {
            "description": "search jokes by text",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "value": "joke text",
                            "id": "0hciWYMBaE7BXjiR7n2j"
                        },
                        {
                            "value": "joke text",
                            "id": "94glWYMBFco5Igbw518J"
                        }
                    ]
                }
            },
        },
    },
)
async def search(search: str) -> JSONResponse:
    " fulltext search to find jokes"
    
    joke_service = JokeService(JokeESRepository)

    jokes = joke_service.search(
        search=search
    )
    
    return JSONResponse(jokes, status_code=200)