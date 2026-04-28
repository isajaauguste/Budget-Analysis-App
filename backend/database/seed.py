import asyncio

from sqlalchemy import select
from datetime import date

from database.session import AsyncSessionLocal
from models import Expense, ExpenseCategory, Income, IncomeCategory


async def seed_data() -> None:
    async with AsyncSessionLocal() as session:

        # =====================
        # EXPENSE CATEGORIES
        # =====================
        expense_categories_data = [
            {"category": "Food", "description": "Food and groceries"},
            {"category": "Transport", "description": "Public transport, fuel"},
            {"category": "Entertainment", "description": "Movies, games, fun"},
        ]

        expense_category_objects = {}

        for cat_data in expense_categories_data:
            result = await session.execute(
                select(ExpenseCategory).where(
                    ExpenseCategory.category == cat_data["category"]
                )
            )
            category = result.scalar_one_or_none()

            if category is None:
                category = ExpenseCategory(
                    category=cat_data["category"],
                    description=cat_data["description"],
                )
                session.add(category)
                await session.flush()

            expense_category_objects[cat_data["category"]] = category

        # =====================
        # INCOME CATEGORIES
        # =====================
        income_categories_data = [
            {"category": "Salary", "description": "Monthly salary"},
            {"category": "Freelance", "description": "Freelance income"},
            {"category": "Investments", "description": "Dividends, stocks"},
        ]

        income_category_objects = {}

        for cat_data in income_categories_data:
            result = await session.execute(
                select(IncomeCategory).where(
                    IncomeCategory.category == cat_data["category"]
                )
            )
            category = result.scalar_one_or_none()

            if category is None:
                category = IncomeCategory(
                    category=cat_data["category"],
                    description=cat_data["description"],
                )
                session.add(category)
                await session.flush()

            income_category_objects[cat_data["category"]] = category

        # =====================
        # EXPENSES
        # =====================
        expenses_data = [
            {"name": "Lunch", "amount": 15.0, "category": "Food"},
            {"name": "Bus Ticket", "amount": 2.5, "category": "Transport"},
            {"name": "Cinema", "amount": 12.0, "category": "Entertainment"},
        ]

        for exp_data in expenses_data:
            result = await session.execute(
                select(Expense).where(Expense.name == exp_data["name"])
            )
            expense = result.scalar_one_or_none()

            category = expense_category_objects[exp_data["category"]]

            if expense is None:
                expense = Expense(
                    name=exp_data["name"],
                    amount=exp_data["amount"],
                    date=date.today(),
                    category_id=category.category_id,
                    user_id=None
                )
                session.add(expense)
            else:
                expense.category_id = category.category_id

        # =====================
        # INCOME
        # =====================
        incomes_data = [
            {"name": "Main Job Salary", "amount": 2500.0, "category": "Salary"},
            {
                "name": "Side Freelance Project",
                "amount": 800.0,
                "category": "Freelance",
            },
            {"name": "Stock Dividends", "amount": 200.0, "category": "Investments"},
        ]

        for inc_data in incomes_data:
            result = await session.execute(
                select(Income).where(Income.name == inc_data["name"])
            )
            income = result.scalar_one_or_none()

            category = income_category_objects[inc_data["category"]]

            if income is None:
                income = Income(
                    name=inc_data["name"],
                    amount=inc_data["amount"],
                    date=date.today(),
                    category_id=category.category_id,
                    user_id=None,  # jei modelyje yra
                )
                session.add(income)
            else:
                income.category_id = category.category_id

        await session.commit()
        print("Seed data inserted successfully.")


if __name__ == "__main__":
    asyncio.run(seed_data())
