import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://raedmundjennings@localhost:5432/meshic_final",
)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)


def get_async_db_engine():
    return engine


def get_async_session(engine):
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)()
