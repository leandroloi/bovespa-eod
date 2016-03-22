# -*- coding: utf-8 -*-
import os

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
    DATABASE_URL = os.environ.get("DATABASE_URL")
    STAGING_DATABASE_URL = os.environ.get("STAGING_DATABASE_URL")
    DEVELOPMENT_DATABASE_URL = os.environ.get("DEVELOPMENT_DATABASE_URL", 'postgres://postgres:1q2w3e4r5t@localhost:5432/securities_master_test')




class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_CONFIG = {'sqlalchemy.url': Config.DATABASE_URL, 'sqlalchemy.echo': 'False', 'pool_size': 5}
    REDIS_URL = os.environ.get('REDIS_URL')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_CONFIG = {'sqlalchemy.url': Config.STAGING_DATABASE_URL, 'sqlalchemy.echo': 'False', 'pool_size': 5}
    REDIS_URL = os.environ.get('REDIS_URL')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_CONFIG = {'sqlalchemy.url': Config.DEVELOPMENT_DATABASE_URL, 'sqlalchemy.echo': 'True', 'pool_size': 5}
    REDIS_URL = os.environ.get('REDIS_URL')



class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_CONFIG = {'sqlalchemy.url': Config.DEVELOPMENT_DATABASE_URL, 'sqlalchemy.echo': 'False', 'pool_size': 5,
                         'convert_unicode': True}
    REDIS_URL = os.environ.get('REDIS_URL')
