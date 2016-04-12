# -*- coding: utf-8 -*-
from decimal import Decimal
from models.daily_price import DailyPrice
from tests import DatabaseTest
import datetime


__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


def convert_to_tuple(equity):
    return (equity.get('price_date'), equity.get('cod_dbi'), equity.get('ticker'), equity.get('tpmerc'),
            equity.get('especi'), equity.get('prazot'), equity.get('open_price'), equity.get('high_price'),
            equity.get('low_price'), equity.get('avg_price'), equity.get('close_price'), equity.get('preofc'),
            equity.get('preofv'), equity.get('totneg'), equity.get('quatot'), equity.get('volume'),
            equity.get('preexe'), equity.get('indopc'), equity.get('datven'), equity.get('fatcot'),
            equity.get('ptoexec'), equity.get('codisi'), equity.get('dismes'))


class DailyPriceTestCase(DatabaseTest):
    def setUp(self):
        self.daily_price = DailyPrice(self.db)

    def test_insert_spot_price(self):
        start_date = datetime.datetime(2016, 4, 4, 0, 0)
        end_date = datetime.datetime(2016, 4, 4, 0, 0)
        symbols = ['AAPL34','ABCB4']
        price1 = dict(low_price=Decimal('39.9000'), ptoexec=Decimal('0.0000'), prazot='', preexe=Decimal('0.0000'),
                      tpmerc=10L, ticker='AAPL34      ', quatot=55000L, datven=datetime.datetime(9999, 12, 31, 0, 0),
                      dismes=116L, high_price=Decimal('40.2800'), especi=None, preofv=Decimal('40.4000'), volume=22L,
                      open_price=Decimal('40.0000'), avg_price=Decimal('40.0500'), codisi='BRAAPLBDR004', fatcot=1L,
                      price_date=datetime.datetime(2016, 4, 4, 0, 0), totneg=8L, preofc=Decimal('39.5800'),
                      close_price=Decimal('40.2800'), indopc=0L, cod_dbi=2L)
        price2 = dict(low_price=Decimal('11.5300'), ptoexec=Decimal('0.0000'), prazot='', preexe=Decimal('0.0000'),
                      tpmerc=10L, ticker='ABCB4       ', quatot=209600L, datven=datetime.datetime(9999, 12, 31, 0, 0),
                      dismes=125L, high_price=Decimal('12.0000'), especi=None, preofv=Decimal('11.7000'), volume=25L,
                      open_price=Decimal('12.0000'), avg_price=Decimal('11.7100'), codisi='BRABCBACNPR4', fatcot=1L,
                      price_date=datetime.datetime(2016, 4, 4, 0, 0), totneg=913L, preofc=Decimal('11.6500'),
                      close_price=Decimal('11.6800'), indopc=0L, cod_dbi=2L)

        spot_prices = [convert_to_tuple(price1), convert_to_tuple(price2)]
        self.daily_price.store_spot_prices(spot_prices)
        result = self.daily_price.load_price(symbols, 'spot', start_date, end_date)
        self.assertListEqual([price1, price2], result)

    def test_insert_option_price(self):
        start_date = datetime.datetime(2016, 4, 4, 0, 0)
        end_date = datetime.datetime(2016, 4, 4, 0, 0)
        symbols = ['ABEVD18','ABCB4']
        price1 = {'low_price': Decimal('0.40'), 'ptoexec': '0000000000000', 'prazot': '000', 'preexe': Decimal('18.45'),
                  'tpmerc': 70, 'modref': 'R$  ', 'ticker': 'ABEVD18', 'quatot': 559000,
                  'datven': datetime.datetime(2016, 4, 18, 0, 0), 'tpreg': 1, 'dismes': 110,
                  'high_price': Decimal('0.54'), 'codisi': 'BRABEVACNOR1', 'preofv': Decimal('1.00'),
                  'volume': Decimal('2.76'), 'open_price': Decimal('0.54'), 'avg_price': Decimal('0.49'),
                  'preofc': Decimal('0.42'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 256, 'close_price': Decimal('0.45'), 'indopc': 0, 'cod_dbi': 78}
        price2 = {'low_price': Decimal('0.30'), 'ptoexec': '0000000000000', 'prazot': '000', 'preexe': Decimal('18.70'),
                  'tpmerc': 70, 'modref': 'R$  ', 'ticker': 'ABEVD19', 'quatot': 1300,
                  'datven': datetime.datetime(2016, 4, 18, 0, 0), 'tpreg': 1, 'dismes': 108,
                  'high_price': Decimal('0.30'), 'codisi': 'BRABEVACNOR1', 'preofv': Decimal('0.00'),
                  'volume': Decimal('0.00'), 'open_price': Decimal('0.30'), 'avg_price': Decimal('0.30'),
                  'preofc': Decimal('0.29'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 2, 'close_price': Decimal('0.30'), 'indopc': 0, 'cod_dbi': 78}

        option_prices = [convert_to_tuple(price1), convert_to_tuple(price2)]
        self.daily_price.store_spot_prices(option_prices)
        result = self.daily_price.load_price(symbols, 'spot', start_date, end_date)
        self.assertListEqual([price1, price2], result)

    def test_insert_auction_prices(self):
        pass

    def test_fractionary_prices(self):
        price1 = {'low_price': Decimal('39.95'), 'ptoexec': '0000000000000', 'prazot': '', 'preexe': Decimal('0.00'),
                  'tpmerc': 20, 'modref': 'R$  ', 'ticker': 'AAPL34F', 'quatot': 81,
                  'datven': datetime.datetime(9999, 12, 31, 0, 0), 'tpreg': 1, 'dismes': 116,
                  'high_price': Decimal('39.95'), 'codisi': 'BRAAPLBDR004', 'preofv': Decimal('0.00'),
                  'volume': Decimal('0.03'), 'open_price': Decimal('39.95'), 'avg_price': Decimal('39.95'),
                  'preofc': Decimal('0.00'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 2, 'close_price': Decimal('39.95'), 'indopc': 0, 'cod_dbi': 96}
        price2 = {'low_price': Decimal('11.57'), 'ptoexec': '0000000000000', 'prazot': '', 'preexe': Decimal('0.00'),
                  'tpmerc': 20, 'modref': 'R$  ', 'ticker': 'ABCB4F', 'quatot': 1131,
                  'datven': datetime.datetime(9999, 12, 31, 0, 0), 'tpreg': 1, 'dismes': 125,
                  'high_price': Decimal('12.00'), 'codisi': 'BRABCBACNPR4', 'preofv': Decimal('11.90'),
                  'volume': Decimal('0.13'), 'open_price': Decimal('12.00'), 'avg_price': Decimal('11.72'),
                  'preofc': Decimal('11.55'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 29, 'close_price': Decimal('11.90'), 'indopc': 0, 'cod_dbi': 96}
        pass

    def test_term_prices(self):
        price1 = {'low_price': Decimal('18.73'), 'ptoexec': '0000000000000', 'prazot': '030', 'preexe': Decimal('0.00'),
                  'tpmerc': 30, 'modref': 'R$  ', 'ticker': 'ABEV3T', 'quatot': 500,
                  'datven': datetime.datetime(9999, 12, 31, 0, 0), 'tpreg': 1, 'dismes': 112,
                  'high_price': Decimal('18.74'), 'codisi': 'BRABEVACNOR1', 'preofv': Decimal('0.00'),
                  'volume': Decimal('0.09'), 'open_price': Decimal('18.73'), 'avg_price': Decimal('18.73'),
                  'preofc': Decimal('0.00'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 2, 'close_price': Decimal('18.74'), 'indopc': 0, 'cod_dbi': 62}
        price2 = {'low_price': Decimal('18.87'), 'ptoexec': '0000000000000', 'prazot': '016', 'preexe': Decimal('0.00'),
                  'tpmerc': 30, 'modref': 'R$  ', 'ticker': 'BBAS3T', 'quatot': 7000,
                  'datven': datetime.datetime(9999, 12, 31, 0, 0), 'tpreg': 1, 'dismes': 259,
                  'high_price': Decimal('18.97'), 'codisi': 'BRBBASACNOR3', 'preofv': Decimal('0.00'),
                  'volume': Decimal('1.32'), 'open_price': Decimal('18.96'), 'avg_price': Decimal('18.88'),
                  'preofc': Decimal('0.00'), 'fatcot': 1, 'price_date': datetime.datetime(2016, 4, 4, 0, 0),
                  'totneg': 6, 'close_price': Decimal('18.88'), 'indopc': 0, 'cod_dbi': 62}

    def test_future_prices(self):
        pass
