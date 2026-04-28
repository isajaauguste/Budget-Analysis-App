from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import IncomeCategoryOut
from services import IncomeCategoryService

router = APIRouter(
    prefix="/incomecategories",
    tags=["Income Categories"],
)


@router.get("", response_model=list[IncomeCategoryOut])
async def list_income_categories(
    db: AsyncSession = Depends(get_db),
):
    return await IncomeCategoryService.list_income_categories(db)
