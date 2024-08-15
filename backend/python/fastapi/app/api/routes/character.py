from fastapi import APIRouter, HTTPException
from schemas.character import CharacterCreate, CharacterOut

router = APIRouter(
    prefix="/character",
    tags=["character"]
)

@router.post("/", response_model=CharacterOut)
def create_new_character(character: CharacterCreate):
    return create_character(character)

@router.get("/{character_id}", response_model=CharacterOut)
def get_character(Character_id: int):
    character = get_character_by_id(character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

