from dataclasses import dataclass
from fastapi import HTTPException
from httpx import Response
from source.infraestructure.request import DAD, CHUCK
from source.domain.entities.joke import Joke
from source.ports.request import JokeRequest

@dataclass
class JokeFakeRequest(JokeRequest):
    
    def __post_init__(self):
        if self.value != 'Chuck' and self.value != 'Dad':
            raise HTTPException(status_code=404, detail="Joke not found")

        if self.value == 'Chuck':
            self.url = CHUCK
        else:
            self.url = DAD
        
    def get(self):
        joke = Joke(
            value="value",
            id=5
        )
        
        return joke