# -*- coding: utf-8 -*-

from config import LoggerLoader

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class Symbol(object):
    """
        Symbol model.
    :type db: PostgresDataBase or connection
    """

    def __init__(self, db):
        self.db = db

    def store_symbols(self, symbols=[]):
        # Create the insert strings
        column_str = "exchange_id, ticker, instrument, name, sector, currency, created_date, last_updated_date"
        insert_str = ("%s, " * 8)[:-2]
        final_str = "INSERT INTO securities.symbol (%s) VALUES (%s)" % (column_str, insert_str)
        logger.debug(final_str, len(symbols))
        self.db.insert_many(final_str, symbols)

    def store_symbol(self, symbol):
        # Create the insert strings
        column_str = "exchange_id, ticker, instrument, name, sector, currency, created_date, last_updated_date"
        insert_str = ("%s, " * 8)[:-2]
        final_str = "INSERT INTO securities.symbol (%s) VALUES (%s) " % (column_str, insert_str)
        logger.debug(final_str, len(symbol))
        self.db.insert(final_str, symbol)
