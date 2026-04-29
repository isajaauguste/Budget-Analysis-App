from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from repositories import UserRepository
from schemas import UserLogin
from utils.hash_utils import verify_password
from utils.jwt import create_access_token


class AuthService:
    @staticmethod
    async def login_user(db: AsyncSession, payload: UserLogin) -> str:
        user = await UserRepository.get_by_username_or_email(db, payload.login)

        if not user or not user.credential:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        is_valid = verify_password(
            payload.password,
            user.credential.password_hash,
        )

        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        token = create_access_token(
            {
                "sub": str(user.user_id),
                "username": user.username,
                "email": user.email,
            }
        )

        return token
