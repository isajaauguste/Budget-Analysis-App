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
    from .income_category import IncomeCategory


class Income(TimestampMixin, Base):
    __tablename__ = "income"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    income_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="RESTRICT"), nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("income_categories.category_id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    category: Mapped[list["IncomeCategory"]] = relationship(
        "IncomeCategory", back_populates="incomes"
    )
