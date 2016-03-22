# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as td
from StringIO import StringIO
from dateutil.relativedelta import relativedelta
from utils.download_manager import DownloadManager
import parsers.bovespa_parser as bovespa_parser
import zipfile

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class Bovespa(object):
    def __init__(self):
        self.download_manager = DownloadManager()
        self.historic_path_url = 'http://www.bmfbovespa.com.br/InstDados/SerHist/'

    @staticmethod
    def list_of_files_to_download(files_list, last_update, current_date=dt.today()):
        result = []
        file_avaliable = None
        while last_update <= current_date:
            day = last_update.day
            month = last_update.month
            if day < 10:
                day = '0{0}'.format(last_update.day)
            if month < 10:
                month = '0{0}'.format(last_update.month)
            if last_update.year != current_date.year:
                file_avaliable = files_list.get('COTAHIST_A{year}.ZIP'.format(year=last_update.year))
                last_update += relativedelta(years=1)
                last_update = last_update.replace(day=01)
                last_update = last_update.replace(month=01)
            elif (last_update.year == current_date.year) and (last_update.month != current_date.month):
                file_avaliable = files_list.get(
                    'COTAHIST_M{month}{year}.ZIP'.format(month=month, year=last_update.year))
                last_update += relativedelta(months=1)
            elif (last_update.year == current_date.year) and (last_update.month == current_date.month):
                file_avaliable = files_list.get('COTAHIST_D{day}{month}{year}.ZIP'.format(
                    day=day, month=month, year=last_update.year))
                last_update += td(days=1)

            if file_avaliable:
                result.append(file_avaliable)

        return result

    def download_list_of_files_from_page(self, uri):
        page = self.download_manager.get_page(uri)
        files = bovespa_parser.parse_historic_form_files(page)
        return files

    @staticmethod
    def extract_zipfile(compressed_file):
        z = zipfile.ZipFile(compressed_file)
        for name in z.namelist():
            return StringIO(z.open(name).read())
