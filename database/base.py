# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import urlparse
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DaoBase:
    __metaclass__ = ABCMeta

    def __init__(self, name, database_url):
        self.name = name
        self.database_url = database_url
        db = urlparse.urlparse(database_url)
        self.user = db.username
        self.password = db.password
        self.port = db.port
        self.database = db.path[:1]

    @abstractmethod
    def store(self, **kwargs): pass

    @abstractmethod
    def update(self, **kwargs): pass





