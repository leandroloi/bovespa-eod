# -*- coding: utf-8 -*-

from database.postgres_db import PostgresDataBase
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


def initialize_database(settings):
    try:
        return PostgresDataBase(settings)
    except Exception, e:
        raise e