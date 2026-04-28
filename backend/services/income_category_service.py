from sqlalchemy.ext.asyncio import AsyncSession

from repositories import IncomeCategoryRepository


class IncomeCategoryService:

    @staticmethod
    async def list_income_categories(db: AsyncSession):
        return await IncomeCategoryRepository.get_all(db)
