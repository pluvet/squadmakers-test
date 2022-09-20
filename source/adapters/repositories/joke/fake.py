from source.ports.joke import JokeRepository
from source.domain.entities.joke import Joke

class JokeFakeRepository(JokeRepository):
     
    @staticmethod
    def save(joke: Joke) -> None:
        return None
    
    @staticmethod
    def get() -> Joke:
        return Joke(
            value='random joke',
            id=5
        )

    @staticmethod
    def find(id: str) -> Joke:
        return Joke(
            value='random joke',
            id=id
        )

    @staticmethod
    def update(joke: Joke) -> None:
        return None
    
    @staticmethod
    def delete(joke: Joke) -> None:
        return None

    @staticmethod
    def search(search: str) -> Joke:
        return [Joke(value='find joke',id='1')]
        