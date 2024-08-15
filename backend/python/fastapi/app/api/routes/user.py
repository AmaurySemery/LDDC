from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserOut

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/", response_model=UserOut)
def create_new_user(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}", response_model=UserOut)
def get_user(User_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user