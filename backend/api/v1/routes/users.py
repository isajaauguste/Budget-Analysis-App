from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db, get_current_optional_user
from schemas import UserCreate, UserResponse, CurrentUserResponse
from services import UserService
from models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    return await UserService.create_user(db, payload)

# @router.get("/me", response_model=UserResponse | None)
# async def get_me(current_user: User | None = Depends(get_current_oprional_user)):
#     return current_user

@router.get("/me", response_model=CurrentUserResponse)
async def get_me(
    current_user: User | None = Depends(get_current_optional_user),
):
    if current_user is None:
        return {
            "status": "success",
            "data": None,
        }

    print(f"users_route_27: {current_user.user_id}")
    return {
        "status": "success",
        "data": current_user
    }