# -*- coding: utf-8 -*-
__author__ = 'leandroloi'
__copyright__ = "Copyright 2016,  "
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi@gmail.com"
__status__ = "Development"

from bottle import route, run
import json
from datetime import datetime as dt

@route('/ping')
def ping():
    return {"time": dt.utcnow().isoformat()}

run(host='localhost', port=8080)