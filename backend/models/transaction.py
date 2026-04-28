from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import (
    Date,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .category import Category


class Transaction(TimestampMixin, Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="RESTRICT"), nullable=True, index=True
    )

    amount: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.category_id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    type: Mapped[str] = mapped_column(String(20))  # "income" arba "expense"

    category: Mapped["Category"] = relationship(
        "Category", back_populates="transactions"
    )
