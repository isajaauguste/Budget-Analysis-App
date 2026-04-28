from fastapi import APIRouter

from .routes import (
    expense_categories_router,
    expense_router,
    health_router,
    income_categories_router,
    income_router,
    transactions_router,
    users_router,
    auth_router
)

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(income_router)
api_router.include_router(expense_router)
api_router.include_router(income_categories_router)
api_router.include_router(expense_categories_router)
api_router.include_router(transactions_router)
api_router.include_router(users_router)
api_router.include_router(auth_router)
