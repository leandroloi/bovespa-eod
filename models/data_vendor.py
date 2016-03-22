# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DataVendor(Base):
    __tablename__ = 'data_vendor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)
    website_url = Column(String(255), nullable=True)
    support_email = Column(String(255), nullable=True)
    created_date = Column(DateTime(), nullable=False)
    last_update_date = Column(DateTime, nullable=False)

    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    daily_price_id = Column(Integer, ForeignKey('daily_price.id'))