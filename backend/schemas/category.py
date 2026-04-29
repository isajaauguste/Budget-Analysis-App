from models import TransactionType
from pydantic import BaseModel, ConfigDict
from typing import Optional

class CategoryBase(BaseModel):
    category: str
    description: Optional[str] = None
    type: TransactionType

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    category_id: int

    model_config = ConfigDict(from_attributes=True)