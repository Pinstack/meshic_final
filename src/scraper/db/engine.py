import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/meshic"
)


def get_async_db_engine():
    return create_async_engine(DATABASE_URL, echo=False, future=True)


def get_async_session(engine):
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)()
