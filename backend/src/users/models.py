from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from database import Base

DATABASE_URL = settings.POSTGRES_URL_asyncpg

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


# Причина почему так: https://habr.com/ru/companies/amvera/articles/849836/
class User(Base, SQLAlchemyBaseUserTable[int]):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # name: Mapped[str | None]
    # email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    # is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    # is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
    

class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):

    __tablename__ = 'accesstokens'

    user_id: Mapped[int] = mapped_column(Integer, 
                                         ForeignKey(column="users.id", ondelete='cascade'),
                                         nullable=False)
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
