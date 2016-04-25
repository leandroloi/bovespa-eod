# -*- coding: utf-8 -*-
import simplejson
from bottle import route, response, request, Bottle, error
import datetime
from config import LoggerLoader, ProductionConfig
from models import initialize_database
from models.daily_price import DailyPrice

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

logger = LoggerLoader(__name__).get_logger()
app = Bottle()
DATE_FORMAT = '%Y-%m-%d' #%H:%M:%S'

config = ProductionConfig()
logger.info('Start update database...')
logger.info('Config type: {type}'.format(type=config.CONFIG_TYPE))
settings = config.get_database_from_url(config.DATABASE_URL)
db = initialize_database(settings)

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
    response.content_type='application/json'
    start = request.query['start']
    end = request.query['end']
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

    daily_price = DailyPrice(db)
    results = daily_price.load_price(symbols, 'spot', start_date, end_date)
    resp = simplejson.dumps(results, sort_keys=True, indent=4 * ' ', default=date_handler)
    return {resp}