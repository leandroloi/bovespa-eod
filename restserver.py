# -*- coding: utf-8 -*-
__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"



from bottle import default_app, app, run
import os

DEBUG_PORT = "8085"
port = os.environ.get("PORT", DEBUG_PORT)

application = default_app()
import controllers.ping # necessary so that Bottle will install its routes

if int(port) == int(DEBUG_PORT): #debugging
    run(application, host='0.0.0.0', port=port)