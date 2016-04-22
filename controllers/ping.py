# -*- coding: utf-8 -*-
from bottle import route

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"



@route('/ping')
def ping():
    """
        Inspect method to keed the server alive or to let know, whe is the last time the server responded.

    :return: The current time
    """
    return {"time": datetime.datetime.utcnow().isoformat()}
