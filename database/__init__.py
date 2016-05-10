# -*- coding: utf-8 -*-
from __future__ import with_statement
import psycopg2
from psycopg2 import pool
from config import LoggerLoader
from database.postgres_db import PostgresDataBase

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class DatabaseLoader(object):
    """Singleton"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(DatabaseLoader, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False

        return cls._instance

    def __init__(self, settings=None):
        if not self.__initialized:
            connection = self.config(settings)
            self.db = PostgresDataBase(connection)
            self.__initialized = True

    def get_database(self):
        return self.db

    def config(self, settings):
        """Called by the app on startup to setup bindings to the DB
        :param settings: Database settings, like database,port, user, password
        """
        try:
            conn = psycopg2.pool.SimpleConnectionPool(1, 10, database=settings.get('database'), user=settings.get('user'),
                                                        password=settings.get('password'), host=settings.get('host'),
                                                        port=settings.get('port'))

            return conn

        except Exception, e:
            logger.error('The system is having problem to connect. Exception {exception}'.format(exception=e))
            raise e


def initialize_database(settings):
    """

    :type settings: dict
    :return:
    :raise e:
    """
    try:
        return DatabaseLoader(settings).get_database()
    except Exception, e:
        raise e
