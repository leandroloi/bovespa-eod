# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import psycopg2
import psycopg2.pool
from config import LoggerLoader


__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()


class DaoBase(object):
    """

    :type database_name: str
    :type settings: dict or str or Any
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        from database import DatabaseLoader
        self.db = DatabaseLoader().get_database()

    @abstractmethod
    def get_cursor(self): pass

    @abstractmethod
    def insert(self, insert_str, value_str): pass

    @abstractmethod
    def insert_many(self, insert_str, values=[]): pass
