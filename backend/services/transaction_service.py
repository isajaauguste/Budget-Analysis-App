from sqlalchemy.ext.asyncio import AsyncSession
from schemas import TransactionCreate, TransactionPut, TransactionOut
from repositories import TransactionRepository, CategoryRepository
from models import Category


class TransactionService:
    
    @staticmethod
    async def create_transaction(db: AsyncSession, payload: TransactionCreate, current_user_id: int) -> TransactionOut:

            category = await CategoryRepository.get_by_id(db, payload.category_id)
            if not category:
                raise ValueError("Category not found")
            
            data = payload.model_dump()
            data["user_id"] = current_user_id

            transaction = await TransactionRepository.create(db, data)

            return TransactionOut(
                transaction_id=transaction.transaction_id,
                user_id=transaction.user_id,
                date=transaction.date,
                amount=transaction.amount,
                name=transaction.name,
                category_id=transaction.category_id,
                category_name=category.category,
                category_type=category.type.value,
                created_at=transaction.created_at,
                updated_at=transaction.updated_at,
            )


    @staticmethod
    async def update_transaction(
        db: AsyncSession,
        transaction_id: int,
        payload: TransactionPut,
        current_user_id: int,
    ):
        try:
            transaction = await TransactionRepository.get_by_id(db, transaction_id)

            if not transaction:
                raise ValueError("Transaction not found")
            
            if transaction.user_id != current_user_id:
                raise PermissionError("Not your transaction")

            update_data = payload.model_dump(exclude_unset=True)


            if "category_id" in update_data:
                category = await db.get(Category, update_data["category_id"])
                if not category:
                    raise ValueError("Category not found")

            for key, value in update_data.items():
                setattr(transaction, key, value)

            await db.commit()
            await db.refresh(transaction)

            return TransactionOut(
                transaction_id=transaction.transaction_id,
                user_id=transaction.user_id,
                date=transaction.date,
                amount=transaction.amount,
                name=transaction.name,
                category_id=transaction.category_id,
                category_name=transaction.category.category,
                category_type=transaction.category.type.value,
                created_at=transaction.created_at,
                updated_at=transaction.updated_at,
            )

        except Exception:
            await db.rollback()
            raise

    @staticmethod
    async def delete_transaction(db: AsyncSession, transaction_id: int, current_user_id: int,):
        try:
            transaction = await TransactionRepository.get_by_id(db, transaction_id)

            if not transaction:
                raise ValueError("Transaction not found")
            
            if transaction.user_id != current_user_id:
                raise PermissionError("Not your transaction")

            await TransactionRepository.delete(db, transaction_id)
            return {"message": "Transaction deleted successfully"}

        except Exception:
            await db.rollback()
            raise



    @staticmethod
    async def get_filtered(
        db: AsyncSession,
        current_user_id: int,
        category_type=None,
    ):
        transactions = await TransactionRepository.get_filtered(
            db, current_user_id, category_type
        )
        result = []
        for t in transactions:
            print(t)
            result.append(TransactionOut(
                transaction_id=t.transaction_id,
                user_id=t.user_id,
                date=t.date,
                amount=t.amount,
                name=t.name,
                category_id=t.category_id,
                category_name=t.category.category,
                category_type=t.category.type.value,
                created_at=t.created_at,
                updated_at=t.updated_at,
            ))

        return result





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
