from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import CategoryOut
from services import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get("", response_model=list[CategoryOut])
async def list_categories(
    db: AsyncSession = Depends(get_db),
):
    return await CategoryService.list_categories(db)