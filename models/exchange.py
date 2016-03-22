# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Time, DateTime
from sqlalchemy.orm import relationship

from models import Base, save_obj

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class ExchangeMgr(object):

    @staticmethod
    def store(**kwargs):
        exchange = Exchange(**kwargs)
        save_obj(exchange)


class Exchange(Base):
    __tablename__ = 'exchange'

    id = Column(Integer, primary_key=True, autoincrement=True)
    abbrev = Column(String(32), unique=True, nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    city = Column(String(255), nullable=False)
    country = Column(String(255), nullable=True)
    currency = Column(String(64), nullable=True)
    timezone_offset = Column(Time(), nullable=True)
    created_date = Column(DateTime(), nullable=False)
    last_update_date = Column(DateTime, nullable=False)

    data_vendor = relationship("DataVendor")
    symbol = relationship("Symbol", uselist=False, back_populates="exchange")
