from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transaction import Transaction


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[str] = mapped_column(String(255), nullable=False, index=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True, index=False)

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="category"
    )