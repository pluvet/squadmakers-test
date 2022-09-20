from http.client import responses
from typing import List
from fastapi import HTTPException
from source.infraestructure.elasticsearch import es, exceptions
from source.ports.joke import JokeRepository
from source.domain.entities.joke import Joke

class JokeESRepository(JokeRepository):
     
    @staticmethod
    def save(joke: Joke) -> str:
        '''save the document and returns an id'''
        response = es.index(
            index="joke",
            body=joke.__dict__
        )

        id = response['_id']

        return id
    
    @staticmethod
    def get() -> Joke:
        '''get a random joke in the DB'''
        response = es.search(
            index='joke',
            body={            
                "size": 1,
                "query": {
                    "function_score": {
                        "functions": [
                            {
                            "random_score": {
                                "seed": "1477072619038"
                            }
                            }
                        ]
                    }
                }  
            }
        )

        joke_dict = response['hits']['hits'][0]

        joke = Joke(
            value=joke_dict['_source']['value'],
            id=joke_dict['_id']
        )
        
        return joke

    @staticmethod
    def find(id: str) -> Joke:
        try:
            response = es.get(
                index='joke',
                id = id
            )
        except exceptions.NotFoundError as exc:
            raise HTTPException(status_code=404, detail="Joke not found")
        
        if not response['found']:
            return None

        joke = Joke(value=response['_source']['value'], id=response['_id'])
        
        return joke

    @staticmethod
    def update(joke: Joke) -> None:
        es.update(
            index='joke',
            id=joke.id,
            doc=joke.__dict__
        )
    
    @staticmethod
    def delete(joke: Joke) -> None:
        es.delete(
            index='joke',
            id=joke.id
            )

    @staticmethod
    def search(search: str) -> List[dict]:
        response = es.search(
            index='joke',
            doc_type="_doc",
            body={
                'size' : 100,
                'query': {
                    'match' : {
                        "value": search
                    }
                }
            }
        )
        print(response)

        jokes_response = response['hits']['hits']
        jokes_list = []

        for joke in jokes_response:
            jokes_list.append({
                "value": joke['_source']['value'],
                "id": joke['_id']
            })
            
        return jokes_list