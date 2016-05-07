# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime

import simplejson
from bottle import response, request, Bottle

from config import LoggerLoader
from models.daily_price import DailyPrice

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()
app = Bottle()
DATE_FORMAT = '%Y-%m-%d'

date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime)
       or isinstance(obj, datetime.date)
    else None
)


@app.error()
@app.route('/spot/<symbol>')
@app.route('/<symbol>')
def spot(symbol):
    response.content_type = 'application/json'
    start = request.query['start']
    end = request.query['end']
    columns = request.query['columns']
    try:
        start_date = datetime.datetime.strptime(start, DATE_FORMAT)
        end_date = datetime.datetime.strptime(end, DATE_FORMAT)
    except Exception, e:
        logger.error(e)
        response.status = 402
        return simplejson.dumps({'error': 'You must inform start and end date.'})
    symbol = symbol.upper()

    if ',' in symbol:
        symbols = symbol.split(',')
    else:
        symbols = [symbol, '']

    daily_price = DailyPrice()
    db_result = daily_price.load_price(symbols, 'spot', start_date, end_date, columns)

    results = defaultdict(list)
    for result in db_result:
        results.setdefault(result.get('ticker'), []).append(result)

    resp = simplejson.dumps(results, sort_keys=True, indent=4 * ' ', default=date_handler)
    return {resp}
