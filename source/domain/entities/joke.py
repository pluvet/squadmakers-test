from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Joke():
    value: str
    id: str = ''
