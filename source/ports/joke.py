from typing import List
from source.domain.entities.joke import Joke

class JokeRepository():
    
    @staticmethod
    def save(joke: Joke) -> None:
        raise NotImplementedError('method not implemented, please use an adapter child class')
    
    @staticmethod
    def get() -> Joke:
        raise NotImplementedError('method not implemented, please use an adapter child class')
    
    @staticmethod
    def find(id: str) -> Joke:
        raise NotImplementedError('method not implemented, please use an adapter child class')
    
    @staticmethod
    def update(joke: Joke) -> None:
        raise NotImplementedError('method not implemented, please use an adapter child class')
    
    @staticmethod
    def delete(joke: Joke) -> None:
        raise NotImplementedError('method not implemented, please use an adapter child class')

    @staticmethod
    def search(search: str) -> List[Joke]:
        raise NotImplementedError('method not implemented, please use an adapter child class')
    