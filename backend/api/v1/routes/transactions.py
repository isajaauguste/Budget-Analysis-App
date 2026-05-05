from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db, get_current_user
from schemas import (
    TransactionCreate,
    TransactionOut,
    TransactionPut,
)
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
    payload: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return await TransactionService.create_transaction(
        db=db, current_user_id=current_user.user_id, payload=payload,
    )


@router.put(
    "/{transaction_id}",
    response_model=TransactionOut,
    status_code=status.HTTP_200_OK,
)
async def update_transaction(
    transaction_id: Annotated[int, Path(gt=0)],
    payload: TransactionPut,
    db: AsyncSession = Depends(get_db),
    current_user= Depends(get_current_user),
):
    return await TransactionService.update_transaction(
        db=db,
        transaction_id=transaction_id,
        payload=payload,
        current_user_id=current_user.user_id,
        )


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: Annotated[int, Path(gt=0)],
    db: AsyncSession = Depends(get_db),
    current_user= Depends(get_current_user)
):
    await TransactionService.delete_transaction(db, transaction_id, current_user.user_id)
    return {"message": "Transaction deleted successfully"}


@router.get("/")
async def get_filtered(
    db: AsyncSession = Depends(get_db),
    current_user= Depends(get_current_user),
    category_type: str | None = None,
):
    return await TransactionService.get_filtered(
        db=db,
        category_type=category_type,
        current_user_id=current_user.user_id,
    )
