from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import settings

postgres_sync_engine = create_engine(
    url=settings.POSTGRES_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

postgres_async_engine = create_async_engine(
    url=settings.POSTGRES_URL_asyncpg,
    echo=True,
)

session_factory = sessionmaker(postgres_sync_engine)
async_session_factory = async_sessionmaker(postgres_async_engine)

metadata = MetaData()

