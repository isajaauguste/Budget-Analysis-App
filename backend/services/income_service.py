from sqlalchemy.ext.asyncio import AsyncSession

from repositories import IncomeCategoryRepository, IncomeRepository
from schemas import IncomeCreate, IncomePut, ListParams, PaginatedResponse


class IncomeService:
    @staticmethod
    async def create_income(db: AsyncSession, payload: IncomeCreate):
        if payload.category_id is not None:
            category = await IncomeCategoryRepository.get_by_id(db, payload.category_id)
            if not category:
                raise ValueError("Category not found")

        return await IncomeRepository.create(db=db, data=payload.model_dump())

    @staticmethod
    async def update_income(
        db: AsyncSession,
        income_id: int,
        payload: IncomePut,
    ):
        try:
            income = await IncomeRepository.get_by_id(db, income_id)

            if not income:
                raise ValueError("Income not found")

            update_data = payload.model_dump(exclude_unset=True)

            for field in ["amount", "name", "category_id", "date"]:
                if field in update_data:
                    setattr(income, field, update_data[field])

            await db.commit()
            await db.refresh(income)

            return income

        except Exception:
            await db.rollback()
            raise

    @staticmethod
    async def delete_income(db: AsyncSession, income_id: int):
        try:
            income = await IncomeRepository.get_by_id(db, income_id)

            if not income:
                raise ValueError("Income not found")

            await IncomeRepository.delete(db, income)

        except Exception:
            await db.rollback()
            raise

    @staticmethod
    async def get_income(db: AsyncSession):
        return await IncomeRepository.get_all(db)    
    

    # @staticmethod
    # async def list_incomes(
    #     db: AsyncSession,
    #     params: ListParams,
    # ) -> PaginatedResponse:
    #     incomes, total = await IncomeRepository.get_list(db, params)

    #     return PaginatedResponse.create(
    #         data=incomes,
    #         total=total,
    #         limit=params.limit,
    #         offset=params.offset,
    #     )
