from typing import List
import pytest
from uuid import UUID
from source.domain.entities.joke import Joke
from source.adapters.repositories import JokeESRepository, es

@pytest.mark.asyncio
async def test_save(mocker):  
    
    mocker.patch('es.index', return_value=None)

    joke = Joke(
        joke ='Vampires travel by night because Chuck Norris travels by day.'
    )
    
    output = JokeESRepository.save(joke)
    
    assert not output

def test_find(mocker):
    
    mocker.patch('es.get', return_value={"id": "1", "joke": "Vampires travel by night because Chuck Norris travels by day"})

    joke = Joke(
        joke ='Vampires travel by night because Chuck Norris travels by day.'
    )
    
    output = JokeESRepository.find(id=1)

    assert isinstance(output, Joke)

def test_get(mocker):

    return_value = {"id": "1", "joke": "Vampires travel by night because Chuck Norris travels by day"}
    
    mocker.patch('es.get', return_value=return_value)

    output = JokeESRepository.get()
    
    assert isinstance(output, Joke)

def test_update(mocker, mocker2):
    
    mocker.patch('es.get', return_value={"id": "1", "joke": "Vampires travel by night because Chuck Norris travels by day"})
    
    joke = JokeESRepository.find(id=1)
    
    mocker2.patch('es.update', return_value=None)
    
    joke.joke = 'other joke'
    
    output = JokeESRepository.update(joke)
    
    assert not output
    assert joke.joke == 'other joke'

def test_delete (mocker, mocker2):
    
    mocker.patch('es.get', return_value={"id": "1", "joke": "Vampires travel by night because Chuck Norris travels by day"})
    
    joke = JokeESRepository.find(id=1)
    
    mocker2.patch('es.delete', return_value=None)

    output = JokeESRepository.delete(joke)

    assert not output
    