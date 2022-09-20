from dataclasses import dataclass


@dataclass
class JokeRequest():
    value: str
    url: str = ''
        
    def get(self):
        raise NotImplementedError('please use a child adapter')