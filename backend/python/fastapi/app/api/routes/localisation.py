from fastapi import APIRouter, HTTPException
from schemas.localisation import LocalisationCreate, LocalisationOut

router = APIRouter(
    prefix="/localisation",
    tags=["localisation"]
)

@router.post("/", response_model=LocalisationOut)
def create_new_localisation(localisation: LocalisationCreate):
    return create_localisation(localisation)

@router.get("/{localisation_id}", response_model=LocalisationOut)
def get_localisation(localisation_id: int):
    localisation = get_localisation_by_id(localisation_id)
    if not localisation:
        raise HTTPException(status_code=404, detail="Localisation not found")
    return localisation