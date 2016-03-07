# -*- coding: utf-8 -*-
__author__ = 'leandroloi'
__copyright__ = "Copyright 2016,  "
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi@gmail.com"
__status__ = "Development"

from bottle import default_app, app, run
import os

DEBUG_PORT = "8085"
port = os.environ.get("PORT", DEBUG_PORT)

application = default_app()
import controllers.ping # necessary so that Bottle will install its routes

if int(port) == int(DEBUG_PORT): #debugging
    print 'Starting on port: {}'.format(port)
    run(application, host='0.0.0.0', port=port)