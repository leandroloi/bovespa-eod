# -*- coding: utf-8 -*-
import datetime
from bottle import route
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


@route('/ping')
def ping():
    """
        Inspect method to keed the server alive or to let know, whe is the last time the server responded.

    :return: The current time
    """
    return {"time": datetime.datetime.utcnow().isoformat()}
