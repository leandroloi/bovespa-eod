# -*- coding: utf-8 -*-
from decimal import Decimal
import unittest
from datetime import datetime as dt
import fakeredis
import os
from utils.download_manager import DownloadManager
import scrappers.bovespa as bvmf
from scrappers.parsers import bovespa_parser

__author__ = 'leandroloi'


class DownloadTestCase(unittest.TestCase):

    def setUp(self):
        self.download_manager = DownloadManager()
        self.bovespa_file_manager = bvmf.Bovespa()
        self.redis = fakeredis.FakeStrictRedis()
        self.analysable_files = {'COTAHIST_A1988.ZIP': 'COTAHIST_A1988.ZIP', 'COTAHIST_M052015.ZIP': 'COTAHIST_M052015.ZIP', 'COTAHIST_D06012016.ZIP': 'COTAHIST_D06012016.ZIP', 'COTAHIST_D22012016.ZIP': 'COTAHIST_D22012016.ZIP', 'COTAHIST_A1996.ZIP': 'COTAHIST_A1996.ZIP', 'COTAHIST_M042015.ZIP': 'COTAHIST_M042015.ZIP', 'COTAHIST_A2009.ZIP': 'COTAHIST_A2009.ZIP', 'COTAHIST_A1986.ZIP': 'COTAHIST_A1986.ZIP', 'COTAHIST_D05012016.ZIP': 'COTAHIST_D05012016.ZIP', 'COTAHIST_D10022016.ZIP': 'COTAHIST_D10022016.ZIP', 'COTAHIST_D07012016.ZIP': 'COTAHIST_D07012016.ZIP', 'COTAHIST_A1992.ZIP': 'COTAHIST_A1992.ZIP', 'COTAHIST_A1989.ZIP': 'COTAHIST_A1989.ZIP', 'COTAHIST_A1990.ZIP': 'COTAHIST_A1990.ZIP', 'COTAHIST_D14012016.ZIP': 'COTAHIST_D14012016.ZIP', 'COTAHIST_A2012.ZIP': 'COTAHIST_A2012.ZIP', 'COTAHIST_M032015.ZIP': 'COTAHIST_M032015.ZIP', 'COTAHIST_D15022016.ZIP': 'COTAHIST_D15022016.ZIP', 'COTAHIST_D19022016.ZIP': 'COTAHIST_D19022016.ZIP', 'COTAHIST_D29012016.ZIP': 'COTAHIST_D29012016.ZIP', 'COTAHIST_D05022016.ZIP': 'COTAHIST_D05022016.ZIP', 'COTAHIST_D02022016.ZIP': 'COTAHIST_D02022016.ZIP', 'COTAHIST_A2000.ZIP': 'COTAHIST_A2000.ZIP', 'COTAHIST_D22022016.ZIP': 'COTAHIST_D22022016.ZIP', 'COTAHIST_M112015.ZIP': 'COTAHIST_M112015.ZIP', 'COTAHIST_A2003.ZIP': 'COTAHIST_A2003.ZIP', 'COTAHIST_D23022016.ZIP': 'COTAHIST_D23022016.ZIP', 'COTAHIST_A2010.ZIP': 'COTAHIST_A2010.ZIP', 'COTAHIST_A1991.ZIP': 'COTAHIST_A1991.ZIP', 'COTAHIST_A2014.ZIP': 'COTAHIST_A2014.ZIP', 'COTAHIST_D04012016.ZIP': 'COTAHIST_D04012016.ZIP', 'COTAHIST_D27012016.ZIP': 'COTAHIST_D27012016.ZIP', 'COTAHIST_D26022016.ZIP': 'COTAHIST_D26022016.ZIP', 'COTAHIST_D18022016.ZIP': 'COTAHIST_D18022016.ZIP', 'COTAHIST_D20012016.ZIP': 'COTAHIST_D20012016.ZIP', 'COTAHIST_A2011.ZIP': 'COTAHIST_A2011.ZIP', 'COTAHIST_D25022016.ZIP': 'COTAHIST_D25022016.ZIP', 'COTAHIST_A1994.ZIP': 'COTAHIST_A1994.ZIP', 'COTAHIST_D17022016.ZIP': 'COTAHIST_D17022016.ZIP', 'COTAHIST_D28012016.ZIP': 'COTAHIST_D28012016.ZIP', 'COTAHIST_A2001.ZIP': 'COTAHIST_A2001.ZIP', 'COTAHIST_D21012016.ZIP': 'COTAHIST_D21012016.ZIP', 'COTAHIST_A2007.ZIP': 'COTAHIST_A2007.ZIP', 'COTAHIST_A2013.ZIP': 'COTAHIST_A2013.ZIP', 'COTAHIST_D04022016.ZIP': 'COTAHIST_D04022016.ZIP', 'COTAHIST_D19012016.ZIP': 'COTAHIST_D19012016.ZIP', 'COTAHIST_A2016.ZIP': 'COTAHIST_A2016.ZIP', 'COTAHIST_M062015.ZIP': 'COTAHIST_M062015.ZIP', 'COTAHIST_D01022016.ZIP': 'COTAHIST_D01022016.ZIP', 'COTAHIST_D29022016.ZIP': 'COTAHIST_D29022016.ZIP', 'COTAHIST_D18012016.ZIP': 'COTAHIST_D18012016.ZIP', 'COTAHIST_M012016.ZIP': 'COTAHIST_M012016.ZIP', 'COTAHIST_M092015.ZIP': 'COTAHIST_M092015.ZIP', 'COTAHIST_M102015.ZIP': 'COTAHIST_M102015.ZIP', 'COTAHIST_D12012016.ZIP': 'COTAHIST_D12012016.ZIP', 'COTAHIST_D16022016.ZIP': 'COTAHIST_D16022016.ZIP', 'COTAHIST_D15012016.ZIP': 'COTAHIST_D15012016.ZIP', 'COTAHIST_D11022016.ZIP': 'COTAHIST_D11022016.ZIP', 'COTAHIST_D13012016.ZIP': 'COTAHIST_D13012016.ZIP', 'COTAHIST_D08012016.ZIP': 'COTAHIST_D08012016.ZIP', 'COTAHIST_M072015.ZIP': 'COTAHIST_M072015.ZIP', 'COTAHIST_D03022016.ZIP': 'COTAHIST_D03022016.ZIP', 'COTAHIST_A1995.ZIP': 'COTAHIST_A1995.ZIP', 'COTAHIST_A2002.ZIP': 'COTAHIST_A2002.ZIP', 'COTAHIST_M022016.ZIP': 'COTAHIST_M022016.ZIP', 'COTAHIST_A1993.ZIP': 'COTAHIST_A1993.ZIP', 'COTAHIST_A1998.ZIP': 'COTAHIST_A1998.ZIP', 'COTAHIST_M082015.ZIP': 'COTAHIST_M082015.ZIP', 'COTAHIST_A2005.ZIP': 'COTAHIST_A2005.ZIP', 'COTAHIST_A2015.ZIP': 'COTAHIST_A2015.ZIP', 'COTAHIST_D12022016.ZIP': 'COTAHIST_D12022016.ZIP', 'COTAHIST_A1997.ZIP': 'COTAHIST_A1997.ZIP', 'COTAHIST_A2006.ZIP': 'COTAHIST_A2006.ZIP', 'COTAHIST_D24022016.ZIP': 'COTAHIST_D24022016.ZIP', 'COTAHIST_D26012016.ZIP': 'COTAHIST_D26012016.ZIP', 'COTAHIST_A2008.ZIP': 'COTAHIST_A2008.ZIP', 'COTAHIST_A1999.ZIP': 'COTAHIST_A1999.ZIP', 'COTAHIST_A1987.ZIP': 'COTAHIST_A1987.ZIP', 'COTAHIST_A2004.ZIP': 'COTAHIST_A2004.ZIP', 'COTAHIST_M122015.ZIP': 'COTAHIST_M122015.ZIP', 'COTAHIST_D11012016.ZIP': 'COTAHIST_D11012016.ZIP'}

    def test_download_file(self):
        files = self.download_manager.get_page('http://www.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2010.ZIP')
        self.assertIsNotNone(files)

    def test_list_of_files_to_download_same_month(self):
        same_month = ['COTAHIST_D01022016.ZIP', 'COTAHIST_D02022016.ZIP', 'COTAHIST_D03022016.ZIP',
                      'COTAHIST_D04022016.ZIP', 'COTAHIST_D05022016.ZIP', 'COTAHIST_D10022016.ZIP',
                      'COTAHIST_D11022016.ZIP', 'COTAHIST_D12022016.ZIP', 'COTAHIST_D15022016.ZIP']

        self.redis.set('bov-eod-scrapper:last_update', dt(2016, 02, 01))
        last_update = self.redis.get('bov-eod-scrapper:last_update')
        files_list = self.bovespa_file_manager.list_of_files_to_download(self.analysable_files,
            last_update=dt.strptime(last_update, '%Y-%m-%d %H:%M:%S'), current_date=dt(2016, 02, 15))
        self.assertListEqual(same_month, files_list)

    def test_list_of_files_to_download_diff_year(self):
        same_month = ['COTAHIST_A2014.ZIP', 'COTAHIST_A2015.ZIP', 'COTAHIST_M012016.ZIP', 'COTAHIST_D01022016.ZIP',
                      'COTAHIST_D02022016.ZIP', 'COTAHIST_D03022016.ZIP',
                      'COTAHIST_D04022016.ZIP', 'COTAHIST_D05022016.ZIP', 'COTAHIST_D10022016.ZIP',
                      'COTAHIST_D11022016.ZIP', 'COTAHIST_D12022016.ZIP', 'COTAHIST_D15022016.ZIP']
        self.redis.set('bov-eod-scrapper:last_update', dt(2014, 11, 01))
        last_update = self.redis.get('bov-eod-scrapper:last_update')
        files_list = self.bovespa_file_manager.list_of_files_to_download(self.analysable_files,
            last_update=dt.strptime(last_update, '%Y-%m-%d %H:%M:%S'), current_date=dt(2016, 02, 15))
        self.assertListEqual(same_month, files_list)

    def test_scrap_filename_from_page(self):
        url = 'http://www.bmfbovespa.com.br/pt-br/cotacoes-historicas/FormSeriesHistoricasArq.asp'
        result = self.bovespa_file_manager.download_list_of_files_from_page(url)
        self.assertDictContainsSubset(self.analysable_files, result)

    def test_extract_zipfile(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_A2015.ZIP'
        fh = open(f, 'rb')
        txt_file = self.bovespa_file_manager.extract_zipfile(fh)
        for line in txt_file.readlines():
            if '012015122882CSNAM44' in line:
                self.assertEqual(True, True)
        fh.close()

    # def test_update(self):
    #     list_of_files = ['COTAHIST_A2014.ZIP']
    #     try:
    #         self.bovespa_file_manager.update(list_of_files)
    #         self.assertEqual(True, True)
    #     except Exception, e:
    #         self.assertEqual(True, False, e)

    def test_parse_historic_data(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016.TXT'
        fh = open(f, 'rb')
        try:
            bovespa_parser.parse_historic_data(fh)
            self.assertEqual(True,True)
        except Exception, e:
            self.assertEqual(True, False, e)

        fh.close()

    def test_parse_historic_data_exception(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016_EXCEPTION.TXT'
        fh = open(f, 'rb')
        try:
            bovespa_parser.parse_historic_data(fh)
            self.assertEqual(False, True)
        except Exception, e:
            self.assertEqual(True, True)

        fh.close()

    def test_convert_str_to_float(self):
        numbers_str = ['0000001213887', '0000000213887', '0000000013889', '0000000003800', '0000000038000', '0000000003881']
        numbers_decimal = [Decimal('12138.87'), Decimal('2138.87'), Decimal('138.89'), Decimal('38.00'), Decimal('380.00'), Decimal('38.81')]
        results = []
        for number in numbers_str:
            results.append(bovespa_parser.convert_str_to_decimal(number))

        self.assertListEqual(numbers_decimal, results)

    def test_convert_str_to_integer(self):
        results = []
        numbers_str = ['-1', '0', '2', '10', '100', '1000', '10000', '100000', '1000000']
        numbers_int = [-1, 0, 2, 10, 100, 1000, 10000, 100000, 1000000]

        for number in numbers_str:
            results.append(bovespa_parser.convert_str_to_integer(number))

        self.assertListEqual(numbers_int, results)

    def test_convert_str_to_date(self):
        expected_result = dt(2010, 01, 01)
        self.assertEqual(expected_result, bovespa_parser.convert_str_to_date('20100101'))


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_insert_database(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
