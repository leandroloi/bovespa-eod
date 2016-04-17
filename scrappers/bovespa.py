# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as td
from StringIO import StringIO
from dateutil.relativedelta import relativedelta
from utils.browser import Browser
import parsers.bovespa_parser as bovespa_parser
from utils.tools import uncompress_zipfile

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class Bovespa(object):
    """
        Class responsible to manage the operations with the website of bovespa.
    """

    def __init__(self):
        self.__browser = Browser()
        self.bovespa_url_base = 'http://bvmf.bmfbovespa.com.br'

    @staticmethod
    def _files_from_period(files_list, last_update, current_date=dt.today()):
        """
            From all the files available in the website, selects only the ones between the range date
            ( last update, current date)
        :param files_list: List of the files available on the Bovespa website
        :param last_update: Last time the update was made
        :param current_date: Current time ( normally today )
        :return: list of files to be download
        """
        result = []
        file_avaliable = None
        while last_update.date() <= current_date.date():
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

    def _available_files(self):
        """
            Get all the file names available to download on the bovespa website.
        :return : List of available files in the website
        """
        url = self.bovespa_url_base + '/pt-br/cotacoes-historicas/FormSeriesHistoricasArq.asp'
        page = self.__browser.get_page(url)
        files = bovespa_parser.parse_files_form(page)
        return files

    def select_files(self, start_dt, finish_dt=dt.now()):
        """
            Select the files to be download to update the database
        :type start_dt: datetime.datetime
        :type finish_dt: datetime.datetime
        :return: List of files to download based on the start and finish date
        """
        available_files = self._available_files()
        return self._files_from_period(available_files, start_dt, finish_dt)

    def download_file(self, file_name):
        """
            Download a file from bovespa historic website, and returns uncompressed.
        :type file_name: str
        :return: A TXT file.
        """
        url = self.bovespa_url_base + '/InstDados/SerHist/'
        downloaded_file = self.__browser.get_page(url + file_name)
        compressed_file = StringIO(downloaded_file)
        uncompressed_file = uncompress_zipfile(compressed_file)
        return uncompressed_file
