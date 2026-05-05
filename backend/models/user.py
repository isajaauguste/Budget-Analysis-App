from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Enum as SqlEnum
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

from .mixins import TimestampMixin
from .enums import UserRole

if TYPE_CHECKING:
    from .credential import Credential


class User(TimestampMixin, Base):
    __tablename__ = "users"
    # __table_args__ defines additional table-level configuration
    # __table_args__ = (
    #     # CheckConstraint is fully defined by us: we write the condition and optionally give it a name
    #     CheckConstraint("pages > 0", name="check_book_pages_positive"),
    #     CheckConstraint("price >= 0", name="check_book_price_non_negative"),
    # )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole, name="user_role"), nullable=False, default=UserRole.USER)
    email: Mapped[str] = mapped_column(String(255), nullable=True, index=False)
    username: Mapped[str] = mapped_column(String(255), nullable=True, index=False)
    credential: Mapped["Credential"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )

    # categories: Mapped[list["Category"]] = relationship(
    #     secondary=book_category,
    #     back_populates="books",
    # )
