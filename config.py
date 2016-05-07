# -*- coding: utf-8 -*-
import logging
import logging.config
import os
import urlparse
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class LoggerLoader(object):
    """Singleton"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(LoggerLoader, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False

        return cls._instance

    def __init__(self, name):
        if not self.__initialized:
            logging_conf_file = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/logging.ini'
            # create logger
            logging.config.fileConfig(logging_conf_file)
            self.logger = logging.getLogger(name)
            self.__initialized = True

    def get_logger(self, level=None):
        if level is not None:
            self.logger.setLevel(level)

        return self.logger


class Config(object):
    DEBUG = False
    TESTING = False
    @staticmethod
    def get_database_from_url(url, netloc='postgres'):
        urlparse.uses_netloc.append(netloc)
        url = urlparse.urlparse(url)
        return dict(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port,
            database_url=url
        )


class ProductionConfig(Config):
    CONFIG_TYPE = 'PRODUCTION'
    DEBUG = False
    CACHE = True
    REDIS_URL = os.environ.get('REDIS_URL')
    DATABASE_URL = os.environ.get('DATABASE_URL')



class StagingConfig(Config):
    CONFIG_TYPE = 'STAGING'
    DEBUG = True
    CACHE = True
    REDIS_URL = os.environ.get('REDIS_URL')
    DATABASE_URL = os.environ.get('DATABASE_URL')



class DevelopmentConfig(Config):
    CONFIG_TYPE = 'DEVELOPMENT'
    DEBUG = True
    CACHE = True
    REDIS_URL = os.environ.get('REDIS_URL')
    DATABASE_URL = os.environ.get('DATABASE_URL')



class TestingConfig(Config):
    CONFIG_TYPE = 'TEST'
    DEBUG = True
    CACHE = True
    REDIS_URL = os.environ.get('REDIS_URL')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://leandroloi:1q2w3e4r5t@localhost:5432/bovespa_test')

