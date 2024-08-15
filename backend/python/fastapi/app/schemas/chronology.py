from pydantic import BaseModel
from typing import List
from datetime import datetime

class Events(BaseModel):
    id: int
    date: datetime
    description: str

class ChronologyCreate(BaseModel):
    events: List[Events]
    plot: bool

class ChronologyOut(BaseModel):
    events: List[Events]
    plot: bool