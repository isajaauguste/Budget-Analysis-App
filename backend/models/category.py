from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Enum as SqlEnum
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from database import Base
from .enum import TransactionType

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transaction import Transaction


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[str] = mapped_column(String(255), nullable=False, index=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True, index=False)

    type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType, name="transaction_type"),
        nullable=False,
        index=True
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )