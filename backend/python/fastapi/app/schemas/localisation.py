from pydantic import BaseModel
from typing import List

class Coordinates(BaseModel):
    long: float
    lat: float

class Places(BaseModel):
    name: str
    picture: str
    id: int
    description: str

class LocalisationCreate(BaseModel):
    world: str
    coordinates: Coordinates
    description: str
    places: List[Places]
    name: str

class LocalisationOut(LocalisationCreate):
    id: int