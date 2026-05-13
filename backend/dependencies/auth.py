from typing import Annotated
from fastapi import Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from fastapi import HTTPException, status
from repositories import UserRepository
from utils.jwt import decode_access_token
from models import User, UserRole

async def get_current_user(
        db: AsyncSession = Depends(get_db),
        access_token: Annotated[str | None, Cookie()] = None,
):
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    
    try:
        payload = decode_access_token(access_token)
        user_id = int(payload["sub"])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
    user = await UserRepository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    return user


async def require_admin(
        current_user: User = Depends(get_current_user)
) -> User:
    if  current_user.role != UserRole.ADMIN:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    
    return current_user

async def get_current_optional_user(
        db: AsyncSession = Depends(get_db),
        access_token: Annotated[str | None, Cookie()] = None,
) -> User | None:
    if not  access_token:
        print("NO ACCESS TOKEN")
        return None
    
    try:
        payload = decode_access_token(access_token)
        print(f"auth_60: {payload}")
        user_id = int(payload["sub"])
        print(f"auth_62: {user_id}")
    except Exception as e:
        print("TOKEN ERROR", e)
        return None
     
    user = await UserRepository.get_by_id(db, user_id)

    if not user:
        print("USER NOT FOUND")
        return None

    print(f"auth_67 {user.user_id}")
    return user