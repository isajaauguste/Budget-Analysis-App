from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Expense

from schemas import ListParams


class ExpenseRepository:
    @staticmethod
    async def create(
        db: AsyncSession,
        data: dict,
    ) -> Expense:
        expense = Expense(**data)
        db.add(expense)
        await db.commit()
        await db.refresh(expense)
        return expense

    @staticmethod
    async def get_by_id(db: AsyncSession, expense_id: int) -> Expense | None:
        result = await db.execute(
            select(Expense).where(Expense.expense_id == expense_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_category(db: AsyncSession, category_id: int) -> list[Expense]:
        result = await db.execute(
            select(Expense).where(Expense.category_id == category_id)
        )
        return result.scalars().all()
    

    @staticmethod
    async def get_all(db: AsyncSession) -> list[Expense]:
        result = await db.execute(select(Expense).options(selectinload(Expense.category)))
        return result.scalars().all()
    




    # @staticmethod
    # async def get_list(db: AsyncSession):
    #     statement = select(Expense)
    #     print(statement)
    #     # sorted_statement = ExpenseRepository._apply_sorting(statement, params)

    #     # count_stmt = select(func.count()).select_from(sorted_statement.subquery())
    #     # total = (await db.execute(count_stmt)).scalar()

    #     # statement = sorted_statement.offset(params.offset).limit(params.limit)
    #     result = await db.execute(statement)
    #     # items = result.scalars().all()
    #     return result
    

    # @staticmethod
    # def _apply_sorting(statement, params: ListParams):

    #     if params.sort_by == "amount":
    #         sort_column = Expense.amount
    #     elif params.sort_by == "date":
    #         sort_column = Expense.date
    #     else:
    #         sort_column = Expense.expense_id

    #     statement = statement.order_by(
    #         sort_column.desc()
    #         if params.sort_order == "desc"
    #         else sort_column.asc()
    #     )

    #     return statement