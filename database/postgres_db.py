# -*- coding: utf-8 -*-
from contextlib import contextmanager
import logging
from math import ceil
from time import sleep

import psycopg2
from psycopg2._psycopg import IntegrityError
from psycopg2.extras import RealDictCursor

from database.base import DaoBase

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)
logging.basicConfig()


class PostgresDataBase(DaoBase):
    def __init__(self, settings):
        if settings:
            super(PostgresDataBase, self).__init__('Postgres', settings)
            self.database_url = settings.get('database_url')
        else:
            raise Exception('Settings is none')

    @contextmanager
    def get_cursor(self):
        got_connection = False
        while not got_connection:
            try:
                con = self.db.getconn()
                yield con.cursor(cursor_factory=RealDictCursor)
                got_connection = True
            except psycopg2.OperationalError, op:
                logger.debug(op)
                sleep(1)
            except AttributeError, ae:
                logger.debug(ae)
                sleep(1)
            except Exception, e:
                logger.error(e)
                con.rollback()
                break
            finally:
                con.commit()
                self.db.putconn(con)

    def insert(self, insert_str, value_str):
        with self.get_cursor() as cur:
            try:
                cur.execute(insert_str, value_str)
            except IntegrityError, i:
                logger.error('Duplicated data. {i}'.format(i=i))
            except Exception,e:
                logger.error(e)

    def insert_many(self, insert_str, values=[]):
        with self.get_cursor() as cur:
            for i in range(0, int(ceil(len(values) / 1000.0))):
                try:
                    cur.executemany(insert_str, values[i * 1000:(i + 1) * 1000])
                except IntegrityError, i:
                    logger.error('Duplicated data. {i}'.format(i=i))
                    for value in values:
                        self.insert(insert_str, value)
                except Exception, e:
                    logger.error(e)

    def fetchall(self, query):
        with self.get_cursor() as cur:
            result = None
            try:
                cur.execute(query)
                result = cur.fetchall()
            except Exception, e:
                logger.error(e)
            finally:
                return result

    # def load(self, query):
    #     with self.get_cursor() as cur:
    #         cur.execute(query)
    #         result = cur.fetchall()
    #
    #     column_names = [desc[0] for desc in cur.description]
    #
    #     #result = psql.read_sql_query(query, con=self.db_single, index_col='price_date')
    #     pd_result = DataFrame(result)
    #     print pd_result.tail()
    #     return result
