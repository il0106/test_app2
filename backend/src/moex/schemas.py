from enum import Enum
from pydantic import BaseModel, field_validator

from datetime import datetime

from fastapi import Form


class EngineEnum(Enum):
    stock = 'stock'
    currency = 'currency'
    futures = 'futures'
    options = 'options'

class MarketEnum(Enum):
    shares = "shares"
    bonds = "bonds"
    selt = "selt"
    forts = "forts"

class BoardEnum(Enum):
    TQBR = "TQBR"
    TQCB = "TQCB"
    RFUD = "RFUD"

class IntervalEnum(Enum):
    _1 = 1
    _10 = 10
    _60 = 60
    _24 = 24
    _7 = 7
    _31 = 31
    _4 = 4

class SMOEX(BaseModel):
    engine: EngineEnum
    market: MarketEnum
    board: BoardEnum
    seccode: str
    start: datetime = "2001-01-01 00:00:00"
    end: datetime = "2100-01-01 00:00:00"
    interval: IntervalEnum

    @classmethod
    def as_form(cls,
                engine: str = Form(...), 
                market: str = Form(...), 
                board: str = Form(...),
                seccode: str = Form(...),
                start: str = Form(...),
                end: str = Form(...),
                interval: int = Form(...)):
        return cls(engine=engine, 
                   market=market, 
                   board=board, 
                   seccode=seccode, 
                   start=start, 
                   end=end, 
                   interval=interval)
    
    @field_validator("market")
    def check_valid_market(cls, market, values):
        engine = values.data['engine'].name
        market_ = market.name
        if engine == 'stock' and market_ != 'bonds' and market_ != 'shares':
            raise ValueError(f"For engine {engine}: market equals only shares or bonds, not {market_}")
        return market

    class Config:
        json_encoders = {datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')}