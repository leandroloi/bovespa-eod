# -*- coding: utf-8 -*-
import redis
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class RedisCache(object):

    def __init__(self, redis_url):
        self.r = redis.from_url(redis_url)

    def add(self, key, value):
        try:
            self.r.set(key, value)
        except Exception, e:
            print e

    def get(self, key):
        try:
            return self.r.get(key)
        except Exception, e:
            print(e)