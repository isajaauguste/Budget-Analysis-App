from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import IncomeCategory


class IncomeCategoryRepository:
    @staticmethod
    async def get_by_id(db: AsyncSession, category_id: int) -> IncomeCategory | None:
        result = await db.execute(
            select(IncomeCategory).where(IncomeCategory.category_id == category_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(db: AsyncSession) -> list[IncomeCategory]:
        result = await db.execute(select(IncomeCategory))
        return result.scalars().all()
