from source.services.joke import JokeService
from source.adapters.repositories.joke.fake import JokeFakeRepository
from source.adapters.requests.fake import JokeFakeRequest

def test_save():
    repo = JokeFakeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = service.save(joke)

    assert isinstance(output, dict)
    
def test_get():
    repo = JokeFakeRepository()

    service = JokeService(repo)

    output = service.get()

    assert isinstance(output, dict)
    
def test_find():
    repo = JokeFakeRepository()

    value = "Chuck"    

    service = JokeService(repo, JokeFakeRequest)

    output = service.find(id=value)

    assert isinstance(output, dict)
    
def test_update():
    repo = JokeFakeRepository()

    joke = "Vampires travel by night because Chuck Norris travels by day."

    service = JokeService(repo)

    output = service.update(id=1, value=joke)

    assert isinstance(output, dict)

def test_delete():
    repo = JokeFakeRepository()

    service = JokeService(repo)

    output = service.delete(id=1)
    
    assert not output
    
def test_search():
    repo = JokeFakeRepository()
    
    service = JokeService(repo)

    search = "Vampires travel by night because Chuck Norris travels by day."

    output = service.search(search)

    assert isinstance(output, list)

