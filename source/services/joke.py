from dataclasses import dataclass
from fastapi import HTTPException
from typing import List
from source.domain.entities.joke import Joke
from source.ports.joke import JokeRepository
from source.ports.request import JokeRequest

@dataclass
class JokeService:
    """joke actions"""
    joke_repository: JokeRepository
    joke_request: JokeRequest = None

    def save(self, value: str)-> dict:
        """this function save jokes"""
        joke = Joke(value)
        
        joke.id = self.joke_repository.save(joke)
        
        joke_dict = joke.__dict__

        return joke_dict

    def get(self)-> dict:
        """get a random joke"""

        joke = self.joke_repository.get()
        
        joke_dict = joke.__dict__

        return joke_dict

    def find(self, id: str)-> dict:
        """find one joke"""
        
        joke_request = self.joke_request(id)
        
        joke = joke_request.get()

        joke_dict = joke.__dict__

        return joke_dict

    def update(self, id: str, value: str)-> dict:
        """update a joke"""
        
        joke = self.joke_repository.find(id)

        if not joke:
            raise HTTPException(status_code=404, detail="Joke not found")

        joke.value = value

        self.joke_repository.update(joke)
        
        joke_dict = joke.__dict__

        return joke_dict

    def delete(self, id: str) -> None:
        """ delete a joke"""
        
        joke = self.joke_repository.find(id)

        if not joke:
            raise HTTPException(status_code=404, detail="Joke not found")

        self.joke_repository.delete(joke)
        
        return None
    
    def search(self, search) -> List[Joke]:
        """ make a fulltextsearch to find joke"""
        
        joke = self.joke_repository.search(search)

        if not joke:
            raise HTTPException(status_code=404, detail="Jokes not found")

        return joke
