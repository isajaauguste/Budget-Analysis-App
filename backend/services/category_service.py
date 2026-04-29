from sqlalchemy.ext.asyncio import AsyncSession

from repositories import CategoryRepository


class CategoryService:

    @staticmethod
    async def list_categories(db: AsyncSession):
        return await CategoryRepository.get_all(db)