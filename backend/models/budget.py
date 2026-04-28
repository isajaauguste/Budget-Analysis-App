from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import TimestampMixin
from database import Base


class Budget(TimestampMixin, Base):
    __tablename__ = "budgets"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    budget_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="RESTRICT"), nullable=True, index=True
    )
    limit: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("expense_categories.category_id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    # categories: Mapped[list["Category"]] = relationship(
    #     secondary=book_category,
    #     back_populates="books",
    # )
