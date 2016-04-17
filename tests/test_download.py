# -*- coding: utf-8 -*-
from decimal import Decimal
import unittest
from datetime import datetime as dt
import fakeredis
import os
from scrappers.bovespa import Bovespa
from scrappers.parsers import bovespa_parser
from utils.browser import Browser
from utils.tools import uncompress_zipfile

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


class DownloadTestCase(unittest.TestCase):

    def setUp(self):
        self.download_manager = Browser()
        self.bovespa = Bovespa()
        self.redis = fakeredis.FakeStrictRedis()
        self.analysable_files = {'COTAHIST_A1988.ZIP': 'COTAHIST_A1988.ZIP', 'COTAHIST_M052015.ZIP': 'COTAHIST_M052015.ZIP', 'COTAHIST_D06012016.ZIP': 'COTAHIST_D06012016.ZIP', 'COTAHIST_D22012016.ZIP': 'COTAHIST_D22012016.ZIP', 'COTAHIST_A1996.ZIP': 'COTAHIST_A1996.ZIP', 'COTAHIST_M042015.ZIP': 'COTAHIST_M042015.ZIP', 'COTAHIST_A2009.ZIP': 'COTAHIST_A2009.ZIP', 'COTAHIST_A1986.ZIP': 'COTAHIST_A1986.ZIP', 'COTAHIST_D05012016.ZIP': 'COTAHIST_D05012016.ZIP', 'COTAHIST_D10022016.ZIP': 'COTAHIST_D10022016.ZIP', 'COTAHIST_D07012016.ZIP': 'COTAHIST_D07012016.ZIP', 'COTAHIST_A1992.ZIP': 'COTAHIST_A1992.ZIP', 'COTAHIST_A1989.ZIP': 'COTAHIST_A1989.ZIP', 'COTAHIST_A1990.ZIP': 'COTAHIST_A1990.ZIP', 'COTAHIST_D14012016.ZIP': 'COTAHIST_D14012016.ZIP', 'COTAHIST_A2012.ZIP': 'COTAHIST_A2012.ZIP', 'COTAHIST_M032015.ZIP': 'COTAHIST_M032015.ZIP', 'COTAHIST_D15022016.ZIP': 'COTAHIST_D15022016.ZIP', 'COTAHIST_D19022016.ZIP': 'COTAHIST_D19022016.ZIP', 'COTAHIST_D29012016.ZIP': 'COTAHIST_D29012016.ZIP', 'COTAHIST_D05022016.ZIP': 'COTAHIST_D05022016.ZIP', 'COTAHIST_D02022016.ZIP': 'COTAHIST_D02022016.ZIP', 'COTAHIST_A2000.ZIP': 'COTAHIST_A2000.ZIP', 'COTAHIST_D22022016.ZIP': 'COTAHIST_D22022016.ZIP', 'COTAHIST_M112015.ZIP': 'COTAHIST_M112015.ZIP', 'COTAHIST_A2003.ZIP': 'COTAHIST_A2003.ZIP', 'COTAHIST_D23022016.ZIP': 'COTAHIST_D23022016.ZIP', 'COTAHIST_A2010.ZIP': 'COTAHIST_A2010.ZIP', 'COTAHIST_A1991.ZIP': 'COTAHIST_A1991.ZIP', 'COTAHIST_A2014.ZIP': 'COTAHIST_A2014.ZIP', 'COTAHIST_D04012016.ZIP': 'COTAHIST_D04012016.ZIP', 'COTAHIST_D27012016.ZIP': 'COTAHIST_D27012016.ZIP', 'COTAHIST_D26022016.ZIP': 'COTAHIST_D26022016.ZIP', 'COTAHIST_D18022016.ZIP': 'COTAHIST_D18022016.ZIP', 'COTAHIST_D20012016.ZIP': 'COTAHIST_D20012016.ZIP', 'COTAHIST_A2011.ZIP': 'COTAHIST_A2011.ZIP', 'COTAHIST_D25022016.ZIP': 'COTAHIST_D25022016.ZIP', 'COTAHIST_A1994.ZIP': 'COTAHIST_A1994.ZIP', 'COTAHIST_D17022016.ZIP': 'COTAHIST_D17022016.ZIP', 'COTAHIST_D28012016.ZIP': 'COTAHIST_D28012016.ZIP', 'COTAHIST_A2001.ZIP': 'COTAHIST_A2001.ZIP', 'COTAHIST_D21012016.ZIP': 'COTAHIST_D21012016.ZIP', 'COTAHIST_A2007.ZIP': 'COTAHIST_A2007.ZIP', 'COTAHIST_A2013.ZIP': 'COTAHIST_A2013.ZIP', 'COTAHIST_D04022016.ZIP': 'COTAHIST_D04022016.ZIP', 'COTAHIST_D19012016.ZIP': 'COTAHIST_D19012016.ZIP', 'COTAHIST_A2016.ZIP': 'COTAHIST_A2016.ZIP', 'COTAHIST_M062015.ZIP': 'COTAHIST_M062015.ZIP', 'COTAHIST_D01022016.ZIP': 'COTAHIST_D01022016.ZIP', 'COTAHIST_D29022016.ZIP': 'COTAHIST_D29022016.ZIP', 'COTAHIST_D18012016.ZIP': 'COTAHIST_D18012016.ZIP', 'COTAHIST_M012016.ZIP': 'COTAHIST_M012016.ZIP', 'COTAHIST_M092015.ZIP': 'COTAHIST_M092015.ZIP', 'COTAHIST_M102015.ZIP': 'COTAHIST_M102015.ZIP', 'COTAHIST_D12012016.ZIP': 'COTAHIST_D12012016.ZIP', 'COTAHIST_D16022016.ZIP': 'COTAHIST_D16022016.ZIP', 'COTAHIST_D15012016.ZIP': 'COTAHIST_D15012016.ZIP', 'COTAHIST_D11022016.ZIP': 'COTAHIST_D11022016.ZIP', 'COTAHIST_D13012016.ZIP': 'COTAHIST_D13012016.ZIP', 'COTAHIST_D08012016.ZIP': 'COTAHIST_D08012016.ZIP', 'COTAHIST_M072015.ZIP': 'COTAHIST_M072015.ZIP', 'COTAHIST_D03022016.ZIP': 'COTAHIST_D03022016.ZIP', 'COTAHIST_A1995.ZIP': 'COTAHIST_A1995.ZIP', 'COTAHIST_A2002.ZIP': 'COTAHIST_A2002.ZIP', 'COTAHIST_M022016.ZIP': 'COTAHIST_M022016.ZIP', 'COTAHIST_A1993.ZIP': 'COTAHIST_A1993.ZIP', 'COTAHIST_A1998.ZIP': 'COTAHIST_A1998.ZIP', 'COTAHIST_M082015.ZIP': 'COTAHIST_M082015.ZIP', 'COTAHIST_A2005.ZIP': 'COTAHIST_A2005.ZIP', 'COTAHIST_A2015.ZIP': 'COTAHIST_A2015.ZIP', 'COTAHIST_D12022016.ZIP': 'COTAHIST_D12022016.ZIP', 'COTAHIST_A1997.ZIP': 'COTAHIST_A1997.ZIP', 'COTAHIST_A2006.ZIP': 'COTAHIST_A2006.ZIP', 'COTAHIST_D24022016.ZIP': 'COTAHIST_D24022016.ZIP', 'COTAHIST_D26012016.ZIP': 'COTAHIST_D26012016.ZIP', 'COTAHIST_A2008.ZIP': 'COTAHIST_A2008.ZIP', 'COTAHIST_A1999.ZIP': 'COTAHIST_A1999.ZIP', 'COTAHIST_A1987.ZIP': 'COTAHIST_A1987.ZIP', 'COTAHIST_A2004.ZIP': 'COTAHIST_A2004.ZIP', 'COTAHIST_M122015.ZIP': 'COTAHIST_M122015.ZIP', 'COTAHIST_D11012016.ZIP': 'COTAHIST_D11012016.ZIP'}

    def test_download_file(self):
        files = self.bovespa.download_file('COTAHIST_A1988.ZIP')
        self.assertIsNotNone(files)

    def test_select_files(self):
        files_expected = ['COTAHIST_A2014.ZIP', 'COTAHIST_A2015.ZIP']
        start = dt(2014, 1, 1)
        end = dt(2016, 1, 1)
        received_files = self.bovespa.select_files(start, end)
        self.assertListEqual(files_expected, received_files)

    def test_extract_zipfile(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_A2015.ZIP'
        fh = open(f, 'rb')
        txt_file = uncompress_zipfile(fh)
        for line in txt_file.readlines():
            if '012015122882CSNAM44' in line:
                self.assertEqual(True, True)
        fh.close()

    def test_parse_historic_data(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016.TXT'
        fh = open(f, 'rb')
        try:
            bovespa_parser.parse_historic_file(fh)
            self.assertEqual(True, True)
        except Exception, e:
            self.assertEqual(True, False, e)

        fh.close()

    def test_parse_header(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016.TXT'
        fh = open(f, 'rb')
        expected_header = {'cod_origin': 'BOVESPA ', 'file_name': 'COTAHIST.2016', 'file_created_date': dt(2016, 2, 29, 0, 0), 'reserve': '', 'tpreg': 0}
        try:
            header = bovespa_parser.get_header(fh)
            self.assertDictEqual(expected_header,header)
        except Exception, e:
            self.assertEqual(True, False, e)

        fh.close()

    def test_parse_trailer(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016.TXT'
        fh = open(f, 'rb')
        expected_trailer = {'file_created_date': dt(2016, 2, 29, 0, 0), 'file_name': u'COTAHIST.2016', 'tpreg': 99, 'total_of_equities': 1911, 'cod_origin': u'BOVESPA ', 'reserve': u''}
        try:
            trailer = bovespa_parser.get_trailer(fh)

            self.assertDictEqual(expected_trailer,trailer)
        except Exception, e:
            self.assertEqual(True, False, e)

        fh.close()

    def test_parse_historic_data_exception(self):
        f = os.path.join(os.path.abspath(os.path.dirname(__file__))) + '/res/COTAHIST_D29022016_EXCEPTION.TXT'
        fh = open(f, 'rb')
        try:
            bovespa_parser.parse_historic_file(fh)
        except Exception, e:
            self.assertEqual(True, True)

        fh.close()

    # def test_convert_str_to_float(self):
    #     numbers_str = ['0000001213887', '0000000213887', '0000000013889', '0000000003800', '0000000038000', '0000000003881']
    #     numbers_decimal = [Decimal('12138.87'), Decimal('2138.87'), Decimal('138.89'), Decimal('38.00'), Decimal('380.00'), Decimal('38.81')]
    #     results = []
    #     for number in numbers_str:
    #         results.append(bovespa_parser.__convert_str_to_decimal(number))
    #
    #     self.assertListEqual(numbers_decimal, results)
    #
    # def test_convert_str_to_integer(self):
    #     results = []
    #     numbers_str = ['-1', '0', '2', '10', '100', '1000', '10000', '100000', '1000000']
    #     numbers_int = [-1, 0, 2, 10, 100, 1000, 10000, 100000, 1000000]
    #
    #     for number in numbers_str:
    #         results.append(bovespa_parser.__convert_str_to_integer(number))
    #
    #     self.assertListEqual(numbers_int, results)
    #
    # def test_convert_str_to_date(self):
    #     expected_result = dt(2010, 01, 01)
    #
    #     resp = bovespa_parser.__convert_str_to_date('20100101')
    #     self.assertEqual(expected_result, resp)