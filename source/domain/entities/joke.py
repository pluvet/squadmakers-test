from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Joke():
    joke: str
    id: UUID = field(default=UUID)

    def __post_init__(self):
        self.id = uuid4()
