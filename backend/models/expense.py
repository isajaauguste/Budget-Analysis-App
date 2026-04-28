from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date
from datetime import date

from .mixins import TimestampMixin
from database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expense_category import ExpenseCategory


class Expense(TimestampMixin, Base):
    __tablename__ = "expenses"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    expense_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="RESTRICT"), nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("expense_categories.category_id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    category: Mapped[list["ExpenseCategory"]] = relationship(
        "ExpenseCategory",
        back_populates="expenses"
    )
