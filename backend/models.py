# backend/models.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Trade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime
    etf: str
    action: int
    weight: float
    price: float
    pnl: float

class PnL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime
    equity: float 