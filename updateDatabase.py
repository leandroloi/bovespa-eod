# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as td
import os

from config import ProductionConfig, LoggerLoader
from controllers.update import Update
from database import initialize_database


__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()
filename = open(os.path.dirname(__file__) + '/lastupdate.txt', 'rw')
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def load_last_update():
    try:
        last_update_str = filename.readline()
        filename.close()
        last_date = dt.strptime(last_update_str, DATE_FORMAT)
    except:
        last_date = dt.strptime(ProductionConfig.START_DATE, DATE_FORMAT)

    return last_date


def store_last_update(end_date):
    last_update = dt.strftime(end_date, DATE_FORMAT)
    filename.write(last_update)
    filename.flush()
    filename.close()


def update_database():
    """
        Method called to update the database.
    """
    update = Update()
    last_update = load_last_update()
    from_date = last_update + td(days=1)
    end_date = dt.now()
    update.update_daily_data(from_date, end_date)
    store_last_update(end_date)
    logger.info('Database EOD has been updated.')


if __name__ == '__main__':
    config = ProductionConfig()
    logger.info('Start update database...')
    logger.info('Config type: {type}'.format(type=config.CONFIG_TYPE))
    logger.info('Database URL : {url}'.format(url=config.DATABASE_URL))
    settings = config.get_database_from_url(config.DATABASE_URL)
    initialize_database(settings)

    update_database()
