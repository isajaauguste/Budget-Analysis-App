from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(
    DATABASE_URL,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,  # Optional: async_sessionmaker uses AsyncSession by default; only needed if you want to customize
    autoflush=False,
    expire_on_commit=False,
)
