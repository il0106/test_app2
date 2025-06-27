from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from config import settings

# Create async SQLite engine
engine = create_async_engine(
    "sqlite+aiosqlite:///../data/sql_app.db",
    echo=True,
)

# Create async session maker
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Base class for all models
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Dependency to get async session
async def get_async_session():
    async with async_session_maker() as session:
        yield session

