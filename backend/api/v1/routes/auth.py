from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import UserLogin
from services import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    payload: UserLogin,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    token, user = await AuthService.login_user(db, payload)

    response.set_cookie(
        key="access_token",
        value=token,
        max_age=60 * 60,
        secure=False,
        httponly=True,
        samesite="lax",
    )

    return {
        "status": "success",
        "message": "Login successful",
        "data": user
        }


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout_user(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logout successful"}
