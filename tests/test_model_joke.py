from uuid import UUID
import pytest
from source.domain.entities.joke import Joke

@pytest.mark.asyncio
async def test_generate_uuid():
    joke = Joke(
        joke="Vampires travel by night because Chuck Norris travels by day."
    )

    assert isinstance(joke.id, UUID)

