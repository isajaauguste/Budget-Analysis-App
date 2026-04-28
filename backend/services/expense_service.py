from sqlalchemy.ext.asyncio import AsyncSession

from repositories import ExpenseCategoryRepository, ExpenseRepository
from schemas import ExpenseCreate, ExpensePut, ListParams, PaginatedResponse


class ExpenseService:
    @staticmethod
    async def create_expense(db: AsyncSession, payload: ExpenseCreate):
        if payload.category_id is not None:
            category = await ExpenseCategoryRepository.get_by_id(
                db, payload.category_id
            )
            if not category:
                raise ValueError("Category not found")

        return await ExpenseRepository.create(db=db, data=payload.model_dump())

    @staticmethod
    async def update_expense(
        db: AsyncSession,
        expense_id: int,
        payload: ExpensePut,
    ):
        try:
            expense = await ExpenseRepository.get_by_id(db, expense_id)

            if not expense:
                raise ValueError("Expense not found")

            update_data = payload.model_dump(exclude_unset=True)

            for field in ["amount", "name", "category_id", "date"]:
                if field in update_data:
                    setattr(expense, field, update_data[field])

            await db.commit()
            await db.refresh(expense)

            return expense

        except Exception:
            await db.rollback()
            raise

    @staticmethod
    async def delete_expense(
        db: AsyncSession,
        expense_id: int
    ):
        try:
            expense = await ExpenseRepository.get_by_id(db, expense_id)

            if not expense:
                raise ValueError("Expense not found")

            await ExpenseRepository.delete(db, expense)

        except Exception:
            await db.rollback()
            raise
            
    @staticmethod
    async def get_expense(db: AsyncSession):
        return await ExpenseRepository.get_all(db)
    







# class ExpenseService:
#     @staticmethod
#     async def create_expense(db: AsyncSession, payload: ExpenseCreate):
#         if payload.category_id is not None:
#             category = await ExpenseRepository.get_by_id(
#                 db, payload.category_id
#             )
#             print(category)

#             if category is None:
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="Category not found",
#                 )
#         return await ExpenseRepository.create(db=db, data=payload.model_dump())

#     @staticmethod
#     async def update_expense(
#         db: AsyncSession,
#         expense_id: int,
#         payload: ExpensePut,
#     ):
#         try:
#             expense = await ExpenseRepository.get_by_id(db, expense_id)

#             if not expense:
#                 raise ValueError("Expense not found")

#             update_data = payload.model_dump(exclude_unset=True)

#             for field in ["amount", "name", "category_id"]:
#                 if field in update_data:
#                     setattr(expense, field, update_data[field])

#             await db.commit()
#             await db.refresh(expense)

#             return expense

#         except Exception:
#             await db.rollback()
#             raise

# @staticmethod
# async def create_expense(db: AsyncSession, payload: ExpenseCreate):
#     if payload.amount is None:
#         raise HTTPException(status_code = 400, detail = "Amount is required")

#     if payload.amount <= 0:
#         raise HTTPException(status_code = 400, detail = "Amount must be greater than 0")

#     if not payload.name or not payload.strip():
#         raise HTTPException(status_code = 400, detail = "Name is required")

#     if len(payload.name) > 255:
#         raise HTTPException(status_code = 400, detail = "Name to long (max 255)")

#     if not payload.category_id:
#         raise HTTPException(status_code = 400, detail = "Category is required")

#     expense_data = payload.model_dump()

#     return await ExpenseRepository.create(
#         db,
#         expense_data
#         )
