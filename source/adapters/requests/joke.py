from dataclasses import dataclass
import httpx
from fastapi import HTTPException
from source.infraestructure.request import DAD, CHUCK
from source.domain.entities.joke import Joke
from source.ports.request import JokeRequest

@dataclass
class JokeGetRequest(JokeRequest):
    
    def __post_init__(self):
        if self.value != 'Chuck' and self.value != 'Dad':
            raise HTTPException(status_code=404, detail="Joke not found")

        if self.value == 'Chuck':
            self.url = CHUCK
        else:
            self.url = DAD
        
    def get(self):
        response = httpx.get(self.url, headers={'Accept': 'application/json'})
        
        json = response.json()
        
        if self.value == 'Chuck':
            value = json['value']
        else:
            value = json['joke']
        
        joke = Joke(
            value=value,
            id=json['id']
        )
        
        return joke
