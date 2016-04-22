# -*- coding: utf-8 -*-
from config import LoggerLoader

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class DailyPrice(object):
    """
        Daily price model.
    :type db: database.postgres_db.PostgresDataBase
    """

    def __init__(self, db):
        self.db = db
        self.schema = 'historic.'

    def __store_prices(self, table, values=[]):
        # Create the insert strings
        column_str = "price_date, cod_dbi, ticker, tpmerc, especi, prazot, open_price, high_price, low_price, " \
                     "avg_price, close_price, preofc, preofv, totneg, quatot, volume, preexe, indopc, datven, fatcot," \
                     "ptoexec, codisi, dismes"
        insert_str = ("%s, " * 23)[:-2]
        final_str = "INSERT INTO %s (%s) VALUES (%s)" % (table, column_str, insert_str)

        self.db.insert_many(final_str, values)

    def store_spot_prices(self, values=[]):
        """

        :type values: list
        """
        self.__store_prices(self.schema + 'spot', values)

    def store_option_prices(self, values=[]):
        self.__store_prices(self.schema + 'option', values)

    def store_auction_prices(self, values=[]):
        self.__store_prices(self.schema + 'auction', values)

    def store_fractionary_prices(self, values=[]):
        self.__store_prices(self.schema + 'fractionary', values)

    def store_term_prices(self, values=[]):
        self.__store_prices(self.schema + 'term', values)

    def store_future_prices(self, values=[]):
        self.__store_prices(self.schema + 'future', values)

    def load_price(self, symbols, type, start_date, end_date):
        results = []
        column_str = "price_date, cod_dbi, ticker, tpmerc, especi, prazot, open_price, high_price, low_price, " \
                     "avg_price, close_price, preofc, preofv, totneg, quatot, volume, preexe, indopc, datven, fatcot," \
                     "ptoexec, codisi, dismes"
        tickers = tuple(symbols)
        # st_date = start_date.date().strftime('%Y-%m-%d ')
        # e_date = end_date.date().strftime('%Y-%m-%d')
        final_query = 'SELECT {col} from {tab} WHERE ticker IN {ticker} AND ' \
                      'price_date BETWEEN \'{start_date}\' AND \'{end_date}\''.format(col=column_str, ticker=tickers,
                                                                                      tab=self.schema + type,
                                                                                      start_date=start_date,
                                                                                      end_date=end_date)
        print final_query
        resp = self.db.fetchall(final_query)
        return resp

        # def load_prices(self):
        #     sql = """SELECT dp.price_date, dp.adj_close_price
        #      FROM securities.symbol AS sym
        #      INNER JOIN securities.daily_price AS dp
        #      ON dp.symbol_id = sym.id
        #
        #      ORDER BY dp.price_date ASC;"""
        #     return self.db.load(sql)
