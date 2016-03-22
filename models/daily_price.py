# -*- coding: utf-8 -*-
import logging

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, BigInteger, String
from sqlalchemy.orm import relationship

from models import Base, save_obj, save_bulk_objs

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


class DailyPriceMgr(object):
    @staticmethod
    def store(**kwargs):
        obj = DailyPrice(**kwargs)
        save_obj(obj)

    @staticmethod
    def bulk_store(daily_price_list=[]):
        save_bulk_objs(daily_price_list)


class DailyPrice(Base):
    __tablename__ = 'daily_price'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price_date = Column(DateTime, nullable=False)
    created_date = Column(DateTime, nullable=False)
    last_updated_date = Column(DateTime, nullable=False)
    open_price = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    high_price = Column(Numeric(precision=19, scle=4, asdecimal=True), nullable=True)
    low_price = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    close_price = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    avg_price = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    adj_close_price = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    volume = Column(BigInteger, nullable=True)

    # specific to bovespa
    cod_dbi = Column(Integer, nullable=True)  # ForeignKey
    especi = Column(String(10), nullable=True)
    ptoexec = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    preofv = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    prazot = Column(Integer, nullable=True)
    preexe = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    preofc = Column(Numeric(precision=19, scale=4, asdecimal=True), nullable=True)
    tpmerc = Column(Integer, nullable=True)
    codisi = Column(String(12), nullable=True)
    datven = Column(DateTime, nullable=True)
    indopc = Column(Integer, nullable=True)
    dismes = Column(Integer, nullable=True)
    fatcot = Column(Integer, nullable=True)
    totneg = Column(Integer, nullable=True)
    quatot = Column(Integer, nullable=True)

    symbol_id = Column(Integer, ForeignKey("symbol.id"))
    data_vendor = relationship('DataVendor')

