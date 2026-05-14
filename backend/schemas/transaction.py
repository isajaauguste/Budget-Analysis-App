from datetime import date, datetime
from models import TransactionType

from pydantic import BaseModel, ConfigDict



class TransactionBase(BaseModel):
    # user_id: int
    amount: float
    date: date
    name: str
    category_id: int

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
    user_id: int
    date: date
    amount: float
    name: str
    category_id: int
    category_name: str
    category_type: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    data: list[TransactionOut]
