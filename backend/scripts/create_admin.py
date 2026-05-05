import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal
from models import User, UserRole
from models.credential import Credential
from utils.hash_utils import hash_password


async def create_admin():
    async with AsyncSessionLocal() as db:
        user = User(
            username="admin",
            email="admin@example.com",
            role=UserRole.ADMIN,
        )

        user.credential = Credential(
            hashed_password=hash_password("admin12345"),
        )

        db.add(user)
        await db.commit()


if __name__ == "__main__":
    asyncio.run(create_admin())