from pydantic import BaseModel, ConfigDict, Field


class ExpenseCategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )


class ExpenseCategoryCreate(ExpenseCategoryBase):
    pass


class ExpenseCategoryOut(BaseModel):
    category_id: int
    description: str

    model_config = ConfigDict(from_attributes=True)
