# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from models import Base

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class Symbol(Base):
    __tablename__ = 'symbol'

    id = Column(Integer, primary_key=True, autoincrement=True)

    ticker = Column(String(32), nullable=False, index=True)
    instrument = Column(String(64), nullable=True)
    name = Column(String(255), nullable=True)
    sector = Column(String(255), nullable=True)
    currency = Column(String(32), nullable=True)
    created_date = Column(DateTime, nullable=False)
    last_updated_date = Column(DateTime, nullable=False)

    # Relationships
    exchange_id = Column(Integer, ForeignKey("exchange.id"))
    exchange = relationship('Exchange', back_populates='symbol')
    daily_price = relationship('DailyPrice')
