# -*- coding: utf-8 -*-
from contextlib import contextmanager
from math import ceil
from time import sleep
import psycopg2
from psycopg2._psycopg import IntegrityError
from psycopg2.extras import RealDictCursor
from config import LoggerLoader
from database.base import DaoBase

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class PostgresDataBase(DaoBase):
    """
        Database class, responsible for manage the inserts, query and deletes.
    :type settings: dict or str or Any
    :raise Exception:
    """

    def __init__(self, connection):
        self.db = connection

    @contextmanager
    def get_cursor(self):
        """
            Get a cursor from a pool. Allowing to make thread inserts.

        """
        got_connection = False
        while not got_connection:
            try:
                con = self.db.getconn()
                yield con.cursor(cursor_factory=RealDictCursor)
                got_connection = True

            except psycopg2.OperationalError, op:
                logger.error('OperationalError %s' % op)
                sleep(2)
                got_connection = False
            except AttributeError, ae:
                logger.error('ae %s' % ae)
                logger.error(ae)
                sleep(2)
                got_connection = False
            except Exception, e:
                logger.error(e)
                sleep(2)
                got_connection = False

            finally:
                try:
                    if con:
                        con.commit()
                        con.close()
                        self.db.putconn(con)
                except:
                    pass
            #     #self.db.putconn(con)



    def insert(self, insert_str, value_str):
        """
            Insert in the databased based on the insert_str the values. The values must be a tuple.
        :type insert_str: str
        :type value_str: tuple or list
        """
        with self.get_cursor() as cur:
            try:
                cur.execute(insert_str, value_str)
            except IntegrityError, i:
                logger.error('Duplicated data. {i}'.format(i=i))
            except Exception, e:
                logger.error(e)

    def insert_many(self, insert_str, values=[]):
        """
            Insert in the database a large numbers of values. It manages a list bigger than a 1000 values, avoiding
            overflows at database level.
        :type insert_str: str
        :type values: list or set
        """
        with self.get_cursor() as cur:
            for i in range(0, int(ceil(len(values) / 1000.0))):
                logger.debug('Storing ' + insert_str[12:30])
                try:
                    cur.executemany(insert_str, values[i * 1000:(i + 1) * 1000])
                except IntegrityError, i:
                    logger.error('Duplicated data. {i}'.format(i=i))
                    for value in values:
                        self.insert(insert_str, value)
                except Exception, e:
                    logger.error(e)

    def fetchall(self, query):
        """
            Recovery all data, based on a query.
        :type query: str
        :return: Cursor result
        """
        with self.get_cursor() as cur:
            result = None
            try:
                cur.execute(query)
                result = cur.fetchall()
            except Exception, e:
                logger.error(e)
            finally:
                return result