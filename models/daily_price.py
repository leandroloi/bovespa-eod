# -*- coding: utf-8 -*-
from config import LoggerLoader
from database import DatabaseLoader

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

    def __init__(self):
        self.db = DatabaseLoader().get_database()
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

    def load_price(self, symbols, type, start_date, end_date, columns=None):
        if not columns:
            columns = "ticker,price_date,cod_dbi,tpmerc,especi,prazot,open_price,high_price,low_price, " \
                         "avg_price,close_price,preofc,preofv,totneg,quatot,volume,preexe,indopc,datven,fatcot," \
                         "ptoexec,codisi,dismes"
        if not 'ticker' in columns:
            columns += ',ticker'
        tickers = tuple(symbols)
        # st_date = start_date.date().strftime('%Y-%m-%d ')
        # e_date = end_date.date().strftime('%Y-%m-%d')
        final_query = 'SELECT {col} from {tab} WHERE ticker IN {ticker} AND ' \
                      'price_date BETWEEN \'{start_date}\' AND \'{end_date}\' order by ticker, price_date DESC;'\
            .format(col=columns, ticker=tickers, tab=self.schema + type, start_date=start_date, end_date=end_date)

        logger.debug(final_query)
        resp = self.db.fetchall(final_query)

        return resp
