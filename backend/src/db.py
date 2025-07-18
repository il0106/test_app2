from typing import AsyncGenerator
import logging

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Boolean, DateTime, text
from sqlalchemy.exc import OperationalError, ProgrammingError
from datetime import datetime

from config import settings


DATABASE_URL = settings["DATABASE_URL"]
Base: DeclarativeMeta = declarative_base()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(SQLAlchemyBaseUserTableUUID, Base):
    is_verified = Column(Boolean, default=False, nullable=False)
    verified_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    """
    Создает базу данных, если её нет, или создает таблицы, если база данных существует, но таблиц в ней нет.
    """
    try:
        # Пытаемся подключиться к базе данных
        async with engine.begin() as conn:
            # Проверяем, существует ли база данных, пытаясь выполнить простой запрос
            try:
                await conn.execute(text("SELECT 1"))
                logger.info("База данных существует, проверяем наличие таблиц...")
                
                # Проверяем, есть ли таблицы в базе данных
                result = await conn.execute(text("""SELECT COUNT(*) FROM sqlite_master WHERE type='table'""")) # Там должна быть user
                table_count = result.scalar()
                
                if table_count == 0:
                    logger.info("База данных пуста, создаем таблицы...")
                    await conn.run_sync(Base.metadata.create_all)
                    logger.info("Таблицы успешно созданы")
                else:
                    logger.info(f"В базе данных найдено {table_count} таблиц")
                    
            except (OperationalError, ProgrammingError) as e:
                logger.warning(f"Ошибка при подключении к базе данных: {e}")
                logger.info("Пытаемся создать базу данных...")
                
                # Если база данных не существует, создаем её
                # Для этого нужно подключиться к postgres (системной БД)
                db_name = DATABASE_URL.split('/')[-1]
                db_url_without_db = '/'.join(DATABASE_URL.split('/')[:-1]) + '/test.db'
                
                temp_engine = create_async_engine(db_url_without_db)
                async with temp_engine.begin() as temp_conn:
                    # Создаем базу данных
                    await temp_conn.execute(text(f"CREATE DATABASE {db_name}"))
                    logger.info(f"База данных '{db_name}' создана")
                
                await temp_engine.dispose()
                
                # Теперь подключаемся к созданной базе данных и создаем таблицы
                async with engine.begin() as new_conn:
                    await new_conn.run_sync(Base.metadata.create_all)
                    logger.info("Таблицы успешно созданы")
                    
    except Exception as e:
        logger.error(f"Ошибка при создании базы данных или таблиц: {e}")
        raise


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
