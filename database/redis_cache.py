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

    """
        A class responsible for cache and to manage update values.
    :type redis_url: Any or str
    """

    def __init__(self, redis_url):
        self.r = redis.from_url(redis_url)

    def add(self, key, value):
        """
            Add the value in the cache.
        :type key: str
        :type value: datetime.datetime
        """
        try:
            self.r.set(key, value)
        except Exception, e:
            print e

    def get(self, key):
        """
            Recover the value from the key

        :type key: str
        :return: Value from the key
        """
        try:
            return self.r.get(key)
        except Exception, e:
            print(e)