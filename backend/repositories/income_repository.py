from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Income

from schemas import ListParams


class IncomeRepository:
    @staticmethod
    async def create(db: AsyncSession, data: dict) -> Income:
        income = Income(**data)
        db.add(income)
        await db.commit()
        await db.refresh(income)
        return income

    @staticmethod
    async def delete(db: AsyncSession, income: Income):
        await db.delete(income)
        await db.commit()
        return

    @staticmethod
    async def get_by_id(db: AsyncSession, income_id: int) -> Income | None:
        result = await db.execute(select(Income).where(Income.income_id == income_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_category(db: AsyncSession, category_id: int) -> list[Income]:
        result = await db.execute(
            select(Income).where(Income.category_id == category_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Income]:
        result = await db.execute(select(Income).options(selectinload(Income.category)))
        return result.scalars().all()



    # @staticmethod
    # async def get_list(db: AsyncSession, params: ListParams):
    #     statement = select(Income)
    #     sorted_statement = IncomeRepository._apply_sorting(statement, params)
    #     count_stmt = select(func.count()).select_from(sorted_statement.subquery())
    #     total = (await db.execute(count_stmt)).scalar()
    #     print(type(total))
    #     statement = sorted_statement.offset(params.offset).limit(params.limit)

    #     result = await db.execute(statement)
    #     items = result.scalars().all()

    #     return total, items
    

    # @staticmethod
    # def _apply_sorting(statement, params: ListParams):

    #     if params.sort_by == "amount":
    #         sort_column = Income.amount
    #     elif params.sort_by == "date":
    #         sort_column = Income.date
    #     else:
    #         sort_column = Income.income_id

    #     statement = statement.order_by(
    #         sort_column.desc()
    #         if params.sort_order == "desc"
    #         else sort_column.asc()
    #     )

    #     return statement