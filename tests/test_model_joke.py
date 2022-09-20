from source.domain.entities.joke import Joke

def test_generate_uuid():
    joke = Joke(
        value="Vampires travel by night because Chuck Norris travels by day."
    )

    assert joke

