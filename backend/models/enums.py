from enum import Enum

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"