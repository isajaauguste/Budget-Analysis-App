from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Category


class CategoryRepository:

    @staticmethod
    async def get_by_id(db: AsyncSession, category_id: int):
        return await db.get(Category, category_id)

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(
            select(Category).order_by(Category.category)
        )
        return result.scalars().all()