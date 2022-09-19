import pytest
from source.ports.joke import JokeRepository
from source.domain.entities.joke import Joke

@pytest.mark.asyncio
async def test_create():
    joke = Joke(
        joke="Vampires travel by night because Chuck Norris travels by day."
    )
    
    repo = JokeRepository(joke)

    assert repo.joke
    
    