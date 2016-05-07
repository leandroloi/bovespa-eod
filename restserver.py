# -*- coding: utf-8 -*-
from database import initialize_database

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

from config import LoggerLoader, ProductionConfig
from bottle import default_app
import os

app = default_app()

from controllers.infra import app as infra
from controllers.stock import app as stock

logger = LoggerLoader(__name__).get_logger()


DEBUG_PORT = "8085"
SERVER_PORT = os.environ.get("PORT", DEBUG_PORT)
SERVER_HOST = os.environ.get("HOST", '0.0.0.0')

BASE_URI = 'api/v1'


app.mount(BASE_URI + '/infra', infra)
app.mount(BASE_URI + '/stock', stock)


if __name__ == '__main__':
    logger.info('Starting server...')
    config = ProductionConfig()
    logger.info('Start update database...')
    logger.info('Config type: {type}'.format(type=config.CONFIG_TYPE))
    settings = config.get_database_from_url(config.DATABASE_URL)
    initialize_database(settings)

    if int(SERVER_PORT) == int(DEBUG_PORT):  # debugging
        app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
    else:
        app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False)
