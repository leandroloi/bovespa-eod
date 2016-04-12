# -*- coding: utf-8 -*-
import logging
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


class Symbol(object):
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
