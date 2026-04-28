from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expense import Expense


class ExpenseCategory(TimestampMixin, Base):
    __tablename__ = "expense_categories"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[str] = mapped_column(String(255), nullable=False, index=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True, index=False)

    expenses: Mapped[list["Expense"]] = relationship(
        "Expense",
        back_populates="category",
    )
