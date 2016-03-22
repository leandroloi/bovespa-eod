# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.base import DaoBase

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class PostgresDataBase(DaoBase):

    def __init__(self, database_url):
        super(PostgresDataBase, self).__init__('Postgres', database_url)
        engine = create_engine(self.database_url)
        Base = declarative_base()
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()


    def get_connection(self):
        pass

    def store_eod_data(self, quote):
        pass