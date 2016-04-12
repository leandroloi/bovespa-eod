# -*- coding: utf-8 -*-
import os
import urlparse
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


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
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://postgres:1q2w3e4r5t@localhost:5432/bovespa2')


class TestingConfig(Config):
    CONFIG_TYPE = 'TEST'
    DEBUG = True
    CACHE = True
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://h:pfoinid3egvofn354utk8bvmij@ec2-107-22-209-183.compute-1.amazonaws.com:15059')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://postgres:1q2w3e4r5t@localhost:5432/bovespa2')
