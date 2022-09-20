from source.ports.joke import JokeRepository

def test_create():
    
    repo = JokeRepository()

    assert repo
    
    