# -*- coding: utf-8 -*-
from datetime import datetime as dt
from decimal import Decimal
from models import DBSession
from models.data_vendor import DataVendor

from models.exchange import ExchangeMgr, Exchange
from models.symbol import Symbol
from tests import DatabaseTest

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DatabaseTestCase(DatabaseTest):

    def test_exchange(self):
        symbol = Symbol(Exchange.id, ticker='AMBV4',instrument='', name='Ambev', sector='', currency='R$',
                created_date=dt.now(), last_update=dt.now()
                )
        exchange_dict = dict(abbrev='Bov', name='Bovespa', city='Sao Paulo', country='Brazil', currency='R$',
                            timezone_offset=dt.now(), created_date=dt.now(), last_update_date=dt.now(), symbol = symbol)
        exchange_to_test = Exchange(**exchange_dict)
        sess = DBSession()
        sess.add(exchange_to_test)
        sess.flush()
        exchange = sess.query(Exchange).filter_by(abbrev='Bov').first()
        self.assertEqual(exchange_to_test, exchange)

    def test_daily_price(self):
        data_vendor = DataVendor(name='Bovespa', website_url='http://www.bmfbovespa.com.br',
                                 support_email='', created_date=dt.now(), last_update_date=dt.now())
        exchange = Exchange(abbrev='BVMF', name='Bovespa', city='Sao Paulo', country='Brazil', currency='R$',
                            timezone_offset=dt.now(), created_date=dt.now(), last_update_date=dt.now())

        symbol = Symbol(Exchange.id, ticker='AMBV4',instrument='', name='Ambev', sector='', currency='R$',
                        created_date=dt.now(), last_update=dt.now()
                        )


        sess = DBSession()




        sess.flush()
        sess.commit()






    def test_symbol(self):
        pass

    def test_vendor(self):
        pass