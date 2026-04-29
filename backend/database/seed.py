import asyncio
from datetime import date

from sqlalchemy import select

from database.session import AsyncSessionLocal
from models import Transaction, Category


async def seed_data():
    async with AsyncSessionLocal() as session:

        # =====================
        # CATEGORIES
        # =====================
        categories_data = [
            # EXPENSE
            {"category": "Food", "description": "Food and groceries", "type": "expense"},
            {"category": "Transport", "description": "Public transport, fuel", "type": "expense"},
            {"category": "Entertainment", "description": "Movies, games", "type": "expense"},

            # INCOME
            {"category": "Salary", "description": "Monthly salary", "type": "income"},
            {"category": "Freelance", "description": "Freelance work", "type": "income"},
            {"category": "Investments", "description": "Dividends", "type": "income"},
        ]

        category_map = {}

        for cat_data in categories_data:
            result = await session.execute(
                select(Category).where(
                    Category.category == cat_data["category"]
                )
            )
            category = result.scalar_one_or_none()

            if category is None:
                category = Category(
                    category=cat_data["category"],
                    description=cat_data["description"],
                    type=cat_data["type"],
                )
                session.add(category)
                await session.flush()

            category_map[cat_data["category"]] = category

        # =====================
        # TRANSACTIONS
        # =====================

        transactions_data = [
            {"name": "Lunch", "amount": 15.0, "category": "Food"},
            {"name": "Bus Ticket", "amount": 2.5, "category": "Transport"},
            {"name": "Cinema", "amount": 12.0, "category": "Entertainment"},

            {"name": "Main Salary", "amount": 2500.0, "category": "Salary"},
            {"name": "Freelance Project", "amount": 800.0, "category": "Freelance"},
            {"name": "Stock Dividends", "amount": 200.0, "category": "Investments"},
        ]

        for tx_data in transactions_data:
            result = await session.execute(
                select(Transaction).where(Transaction.name == tx_data["name"])
            )
            transaction = result.scalar_one_or_none()

            category = category_map[tx_data["category"]]

            if transaction is None:
                transaction = Transaction(
                    name=tx_data["name"],
                    amount=tx_data["amount"],
                    date=date.today(),
                    category_id=category.category_id,
                    user_id=None,
                )
                session.add(transaction)
            else:
                transaction.category_id = category.category_id

        await session.commit()
        print("Seed data inserted successfully.")


if __name__ == "__main__":
    asyncio.run(seed_data())