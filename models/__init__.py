# -*- coding: utf-8 -*-
from database.postgres_db import PostgresDataBase

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"


def initialize_database(settings):
    """

    :type settings: dict
    :return:
    :raise e:
    """
    try:
        return PostgresDataBase(settings)
    except Exception, e:
        raise e