from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime

class IncomeBase(BaseModel):
    user_id: Optional[int] = None
    amount: float = Field(..., gt=0)
    date: date
    name: str = Field(..., min_length=1, max_length=255)
    category_id: int

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )


class IncomeCreate(IncomeBase):
    pass


class IncomePut(IncomeBase):
    pass


class IncomeOut(BaseModel):
    income_id: int
    user_id: Optional[int]
    date: date
    amount: float
    name: str
    category_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

