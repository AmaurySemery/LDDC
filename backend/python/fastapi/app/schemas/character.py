from pydantic import BaseModel

class CharacterCreate(BaseModel):
    background: str
    picture: str
    race: str
    name: str

class CharacterOut(BaseModel):
    id: int
    name: str
    race: str
    background: str