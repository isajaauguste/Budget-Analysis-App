from sqlalchemy.ext.asyncio import AsyncSession

from repositories import UserRepository
from schemas import UserCreate
from utils.hash_utils import hash_password


class UserService:
    @staticmethod
    async def create_user(db: AsyncSession, payload: UserCreate):
        password_hash = hash_password(payload.password)

        user = await UserRepository.create(
            db=db,
            data={
                "username": payload.username,
                "email": payload.email,
                "password_hash": password_hash,
            },
        )

        return user
