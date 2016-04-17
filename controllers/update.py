# -*- coding: utf-8 -*-
import logging
from threading import Thread

from models.daily_price import DailyPrice
import scrappers.bovespa as bvmf
from scrappers.parsers import bovespa_parser

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


class Update(object):

    """
        This class is responsible for the daily database update.

    :type database: database.postgres_db.PostgresDataBase
    """

    def __init__(self, database):
        self.bovespa = bvmf.Bovespa()
        self.database = database

    def update_daily_data(self, start_date, end_date):
        """
            Updates database based on the start and end date.
        :type start_date: datetime.datetime
        :type end_date: datetime.datetime
        """
        filename_list = self.bovespa.select_files(start_date, end_date)
        for filename in filename_list:
            data_file = self.bovespa.download_file(filename)
            self.process_update_file(data_file)

    def process_update_file(self, data_file):
        """
            Process the downloaded and uncompressed datafile and make threads to store faster in each table.
        :type data_file: file or Any or StringIO
        """
        price_daily = DailyPrice(self.database)
        if data_file:
            parsed_equities = bovespa_parser.parse_historic_file(data_file)
            for equitie_type, equities in parsed_equities.iteritems():  # Based on each stock type stores.
                logger.debug(equitie_type + ': {}'.format(len(equities)))
                if 'spot' in equitie_type:
                    spot = Thread(name='Spot', target=price_daily.store_spot_prices, args=(equities,))
                    spot.start()
                elif 'option' in equitie_type:
                    option = Thread(name='Option', target=price_daily.store_option_prices, args=(equities,))
                    option.start()
                elif 'auction' in equitie_type:
                    auction = Thread(name='Auction', target=price_daily.store_auction_prices, args=(equities,))
                    auction.start()
                elif 'fractionary' in equitie_type:
                    option = Thread(name='Fractionary', target=price_daily.store_fractionary_prices, args=(equities,))
                    option.start()
                elif 'term' in equitie_type:
                    term = Thread(name='Term', target=price_daily.store_term_prices, args=(equities,))
                    term.start()
                elif 'future' in equitie_type:
                    future = Thread(name='Future', target=price_daily.store_future_prices, args=(equities,))
                    future.start()

        else:
            logger.error('Error on process update file.')
            # Should retry 3 times otherwise notify by email
