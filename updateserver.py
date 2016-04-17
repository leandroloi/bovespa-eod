# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as td
import logging
from config import TestingConfig
from controllers.update import Update
from models import initialize_database
from database.redis_cache import RedisCache

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


def update_database():
    """
        Method called to update the database.

    """
    logger.info('Start update database...')
    logger.info('Config type: {type}'.format(type=TestingConfig.CONFIG_TYPE))
    settings = TestingConfig.get_database_from_url(TestingConfig.DATABASE_URL)
    db = initialize_database(settings)
    cache = RedisCache(TestingConfig.REDIS_URL)
    update = Update(db)
    last_update_str = cache.get('bov-eod-scrapper:last_update')
    if not last_update_str:
        last_update_str = '2016-01-01 0:0:0'
    last_update = dt.strptime(last_update_str, '%Y-%m-%d %H:%M:%S')
    from_date = last_update + td(days=1)
    end_date = dt.now()
    update.update_daily_data(from_date, end_date)
    cache.add('bov-eod-scrapper:last_update', dt.strftime(end_date, '%Y-%m-%d %H:%M:%S'))
    logger.info('Database EOD has been updated.')

update_database()