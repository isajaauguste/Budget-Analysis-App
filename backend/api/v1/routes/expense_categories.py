from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import ExpenseCategoryOut
from services import ExpenseCategoryService

router = APIRouter(
    prefix="/expensecategories",
    tags=["Expense Categories"],
)


@router.get("", response_model=list[ExpenseCategoryOut])
async def list_expense_categories(
    db: AsyncSession = Depends(get_db),
):
    return await ExpenseCategoryService.list_expense_categories(db)
