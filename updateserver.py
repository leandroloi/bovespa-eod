# -*- coding: utf-8 -*-
from StringIO import StringIO
from scrappers.bovespa import Bovespa
from scrappers.parsers import bovespa_parser

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


def update(self, list_files):
    for f in list_files:
        compressed_file = self.download_manager.get_page(self.historic_path_url + f)
        uncompressed_file = Bovespa.extract_zipfile(StringIO(compressed_file))
        processed_data = bovespa_parser.parse_historic_data_file(uncompressed_file)
        # Todo send processed data to be stored