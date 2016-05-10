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


def load_last_update():
    try:
        filename = open(os.path.dirname(__file__) + '/lastupdate.txt', 'r')
        last_date = filename.readline()
        filename.close()
    except:
        return ProductionConfig.START_DATE
    return last_date


def store_last_update(last_update):
    filename = open("lastupdate.txt", "w")
    filename.write(last_update)
    filename.flush()
    filename.close()


def update_database():
    """
        Method called to update the database.
    """
    update = Update()
    last_update_str = load_last_update()
    last_update = dt.strptime(last_update_str, '%Y-%m-%d %H:%M:%S')
    from_date = last_update + td(days=1)
    end_date = dt.now()
    update.update_daily_data(from_date, end_date)
    store_last_update(dt.strftime(end_date, '%Y-%m-%d %H:%M:%S'))
    logger.info('Database EOD has been updated.')


if __name__ == '__main__':
    config = ProductionConfig()
    logger.info('Start update database...')
    logger.info('Config type: {type}'.format(type=config.CONFIG_TYPE))
    logger.info('Database URL : {url}'.format(url=config.DATABASE_URL))
    settings = config.get_database_from_url(config.DATABASE_URL)
    initialize_database(settings)

    update_database()
