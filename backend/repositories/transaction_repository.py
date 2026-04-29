from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Transaction, Category, TransactionType
from sqlalchemy.orm import selectinload


class TransactionRepository:

    @staticmethod
    async def create(db: AsyncSession, data: dict):
        transaction = Transaction(**data)
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)
        return transaction

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Transaction))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db: AsyncSession, transaction_id: int) -> Transaction | None:
        result = await db.execute(
            select(Transaction).where(Transaction.transaction_id == transaction_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_filtered(
        db: AsyncSession,
        user_id: int | None = None,
        category_type: str = "all"
    ):
        query = (
            select(Transaction)
            .options(selectinload(Transaction.category))
            .join(Transaction.category)
        )

        if user_id:
            query = query.where(Transaction.user_id == user_id)

        if category_type != "all":
            query = query.where(Category.type == category_type)

        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def delete(db: AsyncSession, transaction_id: int):
        transaction = await db.get(Transaction, transaction_id)

        if not transaction:
            return None

        await db.delete(transaction)
        await db.commit()
        return transaction
