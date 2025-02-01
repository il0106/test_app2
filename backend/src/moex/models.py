from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Float

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import metadata


correlation = Table(
    'correlation',
    metadata,
    Column("SECID", String, primary_key=True),
    Column("FXSECID", String, primary_key=True),
    Column("TRADEDATE", TIMESTAMP),
    Column("COEFF_CORRELATION", Float, nullable=False),
    Column("COEFF_BETA", Float, nullable=False)
)

quote = Table(
    'quote',
    metadata,
    Column("SECID", String, nullable=False),
    Column("begin", TIMESTAMP, nullable=False),
    Column("end", TIMESTAMP, nullable=False),
    Column("open", Float, nullable=False),
    Column("close", Float, nullable=False),
    Column("high", Float, nullable=False),
    Column("low", Float, nullable=False),
    Column("value", Float),
    Column("volume", Integer)
)



