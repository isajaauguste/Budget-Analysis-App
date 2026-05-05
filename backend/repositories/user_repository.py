from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Credential, User


class UserRepository:

    @staticmethod
    async def create(db: AsyncSession, data: dict) -> User:
        user = User(username=data["username"], email=data["email"])
        user.credential = Credential(password_hash=data["password_hash"])

        db.add(user)
        await db.commit()
        await db.refresh(user)

        result = await db.execute(
            select(User)
            .options(selectinload(User.credential))
            .where(User.user_id == user.user_id)
        )

        return result.scalar_one()

    @staticmethod
    async def get_by_username_or_email(db: AsyncSession, login: str) -> User | None:
        result = await db.execute(
            select(User)
            .options(selectinload(User.credential))
            .where(or_(User.username == login, User.email == login))
        )

        return result.scalar_one_or_none()
    

    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> User | None:
        result = await db.execute(
             select(User)
             .options(selectinload(User.credential))
             .where(User.user_id == user_id)
        )

        return result.scalar_one_or_none()
