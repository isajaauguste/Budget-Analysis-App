from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import ExpenseCategory


class ExpenseCategoryRepository:
    @staticmethod
    async def get_by_id(db: AsyncSession, category_id: int) -> ExpenseCategory | None:
        result = await db.execute(
            select(ExpenseCategory).where(ExpenseCategory.category_id == category_id)
        )
        print(result)

        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(db: AsyncSession) -> list[ExpenseCategory]:
        result = await db.execute(select(ExpenseCategory))
        return result.scalars().all()
