from unittest import TestCase

from config import TestingConfig
from models import initialize_database, DBSession

__author__ = 'leandroloi'


class DatabaseTest(TestCase):
    def setUp(self):
        settings = TestingConfig.SQLALCHEMY_CONFIG
        initialize_database(settings)

    def tearDown(self):
        DBSession.rollback()
