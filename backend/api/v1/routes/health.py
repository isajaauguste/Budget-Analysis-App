from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from core.status_codes import StatusCode
from dependencies import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", status_code=StatusCode.OK)
async def health_check():
    return {
        "status": "ok",
        "service": "api",
    }


@router.get("/db", status_code=StatusCode.OK)
async def database_health_check(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {
        "status": "ok",
        "service": "database",
    }
