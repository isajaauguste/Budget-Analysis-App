from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal, Generic, TypeVar
from math import ceil


# Generic type variable allows this response to work with any data type (Author, Book)
T = TypeVar("T")


class Meta(BaseModel):
    page: int
    pages: int
    total: int


class PaginatedResponse(BaseModel, Generic[T]):
    # Generic[T] makes the model reusable for different data types
    data: list[T] # List of items of type T (not fixed to a specific model)
    meta: Meta

    @staticmethod
    def create(data: list[T], total: int, limit: int, offset: int) -> "PaginatedResponse[T]":
        # Current page number (offset-based pagination convert to page index)
        page = (offset // limit) + 1
        # ceil rounds UP ensures we count partially filled pages as a full page
        pages = ceil(total / limit) if total > 0 else 1
        print(pages)
        return PaginatedResponse(
            data=data,
            meta=Meta(
                page=page,
                pages=pages,
                total=total,
            ),
        )

class ListParams(BaseModel):
    sort_by: Optional[Literal["date", "amount"]] = None
    sort_order: Literal["asc", "desc"] = "asc"

    limit: int = Field(10, gt=0, le=100)
    offset: int = Field(0, ge=0)

    model_config = ConfigDict(extra="forbid")