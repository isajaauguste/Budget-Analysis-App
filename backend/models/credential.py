from typing import TYPE_CHECKING
from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import TimestampMixin

from database import Base

if TYPE_CHECKING:
    from .user import User


class Credential(TimestampMixin, Base):
    __tablename__ = "credentials"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    credential_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=True, index=False)
    user_id: Mapped [str] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    user: Mapped["User"] = relationship(back_populates="credential")

    # categories: Mapped[list["Category"]] = relationship(
    #     secondary=book_category,
    #     back_populates="books",
    # )
