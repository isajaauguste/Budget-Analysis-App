from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Transaction


class TransactionRepository:

    @staticmethod
    async def create(db: AsyncSession, data: dict):
        obj = Transaction(**data)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

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
    async def get_filtered(db: AsyncSession, type: str):
        query = select(Transaction)

        if type != "all":
            query = query.where(Transaction.type == type)

        result = await db.execute(query)
        return result.scalars().all()

    @staticmethod
    async def delete(db: AsyncSession, obj: Transaction):
        await db.delete(obj)
        await db.commit()
