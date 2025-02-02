from datetime import datetime
import enum
from src.database import Base
from sqlalchemy import Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List, Optional


class GenderEnum(str, enum.Enum):
    MALE = "мужчина"
    FEMALE = "женщина"
    OTHER = "other"


# Причина почему так: https://habr.com/ru/companies/amvera/articles/849836/
class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str | None]
    surname: Mapped[str | None]
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[Optional[GenderEnum]]
    age: Mapped[int | None]
    interests: Mapped[List[str] | None] = mapped_column(ARRAY(String))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
