import pytest
from source.services.joke import JokeService
from source.adapters.joke import FakeJokeRepository

@pytest.mark.asyncio
async def test_save():
    repo = FakeJokeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = await service.save(joke)

    assert isinstance(output, dict)
    
@pytest.mark.asyncio
async def test_get():
    repo = FakeJokeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = await service.get(joke)

    assert isinstance(output, dict)
    
@pytest.mark.asyncio
async def test_find():
    repo = FakeJokeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = await service.find(joke)

    assert isinstance(output, dict)
    
@pytest.mark.asyncio
async def test_update():
    repo = FakeJokeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = await service.update(joke)

    assert isinstance(output, dict)

async def test_delete():
    repo = FakeJokeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = await service.delete(joke)

    assert not output
    

