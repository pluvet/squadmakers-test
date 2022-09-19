import pytest
from source.domain.entities import Joke

@pytest.mark.asyncio
async def test_create_joke():
    joke = Joke(
        joke=joke
    )

    assert joke.joke
    
    
