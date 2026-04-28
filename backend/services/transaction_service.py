from sqlalchemy.ext.asyncio import AsyncSession
from schemas import TransactionCreate, TransactionType, TransactionPut
from repositories import TransactionRepository


class TransactionService:

    @staticmethod
    async def create(db: AsyncSession, data: TransactionCreate):

        payload = data.model_dump()

        # normalize amount
        if data.type == TransactionType.EXPENSE:
            payload["amount"] = -abs(payload["amount"])
        else:
            payload["amount"] = abs(payload["amount"])

        # enum → string DB
        payload["type"] = data.type.value

        return await TransactionRepository.create(db, payload)
    

    @staticmethod
    async def update_transaction(
        db: AsyncSession,
        transaction_id: int,
        payload: TransactionPut,
    ):
        try:
            transaction = await TransactionRepository.get_by_id(db, transaction_id)

            if not transaction:
                raise ValueError("Transaction not found")

            update_data = payload.model_dump(exclude_unset=True)

            for field in ["amount", "name", "category_id", "date"]:
                if field in update_data:
                    setattr(transaction, field, update_data[field])

            await db.commit()
            await db.refresh(transaction)

            return transaction

        except Exception:
            await db.rollback()
            raise
    

    @staticmethod
    async def delete_transaction(db: AsyncSession, transaction_id: int):
        try:
            transaction = await TransactionRepository.get_by_id(db, transaction_id)

            if not transaction:
                raise ValueError("Transaction not found")

            await TransactionRepository.delete(db, transaction)

        except Exception:
            await db.rollback()
            raise

    @staticmethod
    async def get_transactions(db: AsyncSession, type: str = "all"):
        return await TransactionRepository.get_filtered(db, type)


# class TransactionService:

#     @staticmethod
#     async def get_transactions(
#         db: AsyncSession,
#         transaction_type: str = "all",
#         sort_by: str = "date",
#         page: int = 1,
#         page_size: int = 10,
#     ):
#         query, total = await TransactionRepository.get_filtered_query(
#             db=db,
#             transaction_type=transaction_type,
#             sort_by=sort_by,
#             page=page,
#             page_size=page_size,
#         )

#         result = await db.execute(query)
#         transactions = result.scalars().all()

#         return {
#             "total": total,
#             "page": page,
#             "page_size": page_size,
#             "data": transactions,
#         }
#         }


# class TransactionService:
#     @staticmethod
#     async def get_transactions(db: AsyncSession, transaction_type: str = "all", sort_by: str = "date", page: int = 1,
#         page_size: int = 10,):

#         incomes = await IncomeRepository.get_all(db)
#         expenses = await ExpenseRepository.get_all(db)

#         transactions = []

#         for income in incomes:
#             transactions.append({
#                 "id": income.income_id,
#                 "type": "income",
#                 "amount": income.amount,
#                 "date": income.date,
#                 "name": income.name,
#                 "category_id": income.category_id,
#                 "category_name": income.category.category if income.category else None,
#                 "created_at": income.created_at,
#                 "updated_at": income.updated_at,
#             })

#         for expense in expenses:
#             transactions.append({
#                 "id": expense.expense_id,
#                 "type": "expense",
#                 "amount": expense.amount,
#                 "date": expense.date,
#                 "name": expense.name,
#                 "category_id": expense.category_id,
#                 "category_name": expense.category.category if expense.category else None,
#                 "created_at": expense.created_at,
#                 "updated_at": expense.updated_at,
#             })


#         if transaction_type != "all":
#             transactions = [t for t in transactions if t["type"] == transaction_type]

#         if sort_by in ["date", "amount"]:
#             transactions.sort(key=lambda x: x[sort_by], reverse=True)

#         start = (page - 1) * page_size
#         end = start + page_size

#         paginated = transactions[start:end]

#         return {
#             "total": len(transactions),
#             "page": page,
#             "page_size": page_size,
#             "data": paginated,
#         }