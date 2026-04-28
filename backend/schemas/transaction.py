from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import date, datetime
from enum import Enum


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionBase(BaseModel):
    amount: float
    date: date
    name: str
    category_id: int | None = None
    type: TransactionType

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

class TransactionCreate(TransactionBase):
    pass


class TransactionPut(TransactionBase):
    pass


class TransactionOut(BaseModel):
    transaction_id: int
    type: TransactionType
    date: date
    amount: float
    name: str
    category_id: int  | None = None
    category_name: str  | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    data: list[TransactionOut]