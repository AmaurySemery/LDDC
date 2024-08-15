from fastapi import APIRouter, HTTPException
from schemas.chronology import ChronologyCreate, ChronologyOut

router = APIRouter(
    prefix="/chronology",
    tags=["chronology"]
)

@router.post("/", response_model=ChronologyOut)
def create_new_chronology(chronology: ChronologyCreate):
    return create_chronology(chronology)

@router.get("/{chronology_id}", response_model=ChronologyOut)
def get_chronology(chronology_id: int):
    chronology = get_chronology_by_id(chronology_id)
    if not chronology:
        raise HTTPException(status_code=404, detail="Chronology not found")
    return chronology