# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from sqlalchemy import *
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DaoBase:
    __metaclass__ = ABCMeta

    def __init__(self, name, conn, conn_port, user, password):
        self.name = name
        self.conn = conn
        self.conn_port = conn_port
        self.user = user
        self.password = password


    @abstractmethod
    def last_eod_updated(self): pass

    @abstractmethod
    def set_eod_last_update(self): pass



