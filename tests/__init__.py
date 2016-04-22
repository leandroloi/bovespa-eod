from unittest import TestCase
import os
from config import TestingConfig
from models import initialize_database
#from database.redis_cache import RedisCache
import fakeredis
from datetime import datetime as dt

__author__ = 'leandroloi'


def run_sql_file(filename, db):
    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    with db.get_cursor() as cur:
        cur.execute(sql)



class DatabaseTest(TestCase):
    @classmethod
    def setUpClass(self):
        settings = TestingConfig.get_database_from_url(TestingConfig.DATABASE_URL)
        self.db = initialize_database(settings)
        self.cache = fakeredis.FakeStrictRedis()
        self.cache.set('bov-eod-scrapper:last_update', dt(2016, 04, 10))
        sql_file = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/setup_test_database.sql'
        run_sql_file(sql_file, self.db)

    @classmethod
    def tearDownClass(self):
        sql = 'drop schema historic cascade;'
        with self.db.get_cursor() as cur:
            cur.execute(sql)
        #pass
