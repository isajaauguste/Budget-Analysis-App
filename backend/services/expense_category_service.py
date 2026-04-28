from sqlalchemy.ext.asyncio import AsyncSession

from repositories import ExpenseCategoryRepository


class ExpenseCategoryService:

    @staticmethod
    async def list_expense_categories(db: AsyncSession):
        return await ExpenseCategoryRepository.get_all(db)
