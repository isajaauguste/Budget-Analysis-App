from .auth import router as auth_router
from .expense import router as expense_router
from .expense_categories import router as expense_categories_router
from .health import router as health_router
from .income import router as income_router
from .income_categories import router as income_categories_router
from .transactions import router as transactions_router
from .users import router as users_router

__all__ = [
    "health_router",
    "income_router",
    "expense_router",
    "income_categories_router",
    "expense_categories_router",
    "transactions_router",
    "users_router",
    "auth_router",
]
