from pydantic import BaseModel

class JokeModel(BaseModel):
    value: str