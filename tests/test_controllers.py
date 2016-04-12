# -*- coding: utf-8 -*-
import unittest
import os
from controllers.update import Update
from scrappers.parsers import bovespa_parser
from tests import DatabaseTest
from datetime import datetime as dt
from datetime import timedelta as td
from utils.tools import uncompress_zipfile
import fakeredis

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DownloadTestCase(DatabaseTest):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update(self):
        self.update = Update(self.db)
        last_update_str = self.cache.get('bov-eod-scrapper:last_update')
        if not last_update_str:
            last_update_str = '1995-01-01'
        last_update = dt.strptime(last_update_str, '%Y-%m-%d %H:%M:%S')
        from_date = last_update + td(days=1)
        end_date = dt.now()
        self.update.update_daily_data(from_date, end_date)
        self.cache.set('bov-eod-scrapper:last_update', end_date)
