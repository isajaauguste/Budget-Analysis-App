from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
