from fastapi import APIRouter, Depends, Query, status, Path
from typing import Annotated, Optional, Literal
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from schemas import TransactionListResponse, TransactionCreate, TransactionOut, TransactionPut
from services import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# @router.get("", response_model=TransactionListResponse)
# async def get_transactions(
#     db: AsyncSession = Depends(get_db),
#     transaction_type: Annotated[Literal["all", "income", "expense"], Query()] = "all",
#     sort_by: Annotated[Optional[Literal["date", "amount"]], Query()] = "date",
#     limit: Annotated[int, Query(gt=0, le=100)] = 10,
#     offset: Annotated[int, Query(ge=0)] = 0,
# ):
#     return await TransactionService.get_transactions(
#         db=db,
#         transaction_type=transaction_type,
#         sort_by=sort_by,
#         page_size=limit,
#         page=(offset // limit) + 1,
#     )


@router.post("/")
async def create_transaction(
    data: TransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    return await TransactionService.create_transaction(db, data)


@router.put(
    "/{transaction_id}",
    response_model=TransactionOut,
    status_code=status.HTTP_200_OK,
)
async def update_transaction(
    transaction_id: Annotated[int, Path(gt=0)],
    payload: TransactionPut,
    db: AsyncSession = Depends(get_db),
):
    return await TransactionService.update_transaction(db, transaction_id, payload)


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: Annotated[int, Path(gt=0)],
    db: AsyncSession = Depends(get_db),
):
    await TransactionService.delete_transaction(db, transaction_id)
    return {"message": "Transaction deleted successfully"}


@router.get("/")
async def get_filtered(
    category_type: str = "all",
    db: AsyncSession = Depends(get_db)
):
    return await TransactionService.get_filtered(
        db=db,
        category_type=category_type
    )