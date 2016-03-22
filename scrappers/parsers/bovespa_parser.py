# -*- coding: utf-8 -*-
from decimal import Decimal
from bs4 import BeautifulSoup as Bs
from datetime import datetime as dt

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


def parse_historic_form_files(page):
    result = dict()
    soup = Bs(page, 'html.parser')
    files = soup.find_all('option')
    day = str(soup.find(id="hdnDados").get('value', ''))
    daily = day.split('_|_')
    months = []
    for zip_file in files:
        name = zip_file.get('value')
        if name:
            name = str(name).upper()
            if '.ZIP' in name:
                if 'COTAHIST_A' in name:
                    result[name] = name
                elif 'COTAHIST_M' in name:
                    result[name] = name
            else:
                months.append(zip_file.get('value'))
    # Daily files
    for month in months:
        for day in daily:
            file_month = day[0:2]
            if file_month == month:
                name = str(day[6:28]).upper()
                result[name] = name

    return result


def convert_str_to_date(str_date):
    return dt.strptime(str_date, '%Y%m%d')


def convert_str_to_integer(str_number):
    # N: Numérico;
    return int(str_number)


def convert_str_to_decimal(str_number):
    """
        Convert the Field (11)V99 to a float format.
        V: Indica que o número possui vírgula;
        ( ): Quantidade de caracteres antes da vírgula;
        (99): Quantidade de caracteres depois da vírgula
    :type str_number: str
    :return:
    """
    new_str = str_number[0:11] + '.' + str_number[11:13]
    result = Decimal(new_str)
    return result


def parse_historic_data_file(uncompressed_file):
    # Parse file as layout: http://www.bmfbovespa.com.br/pt-br/download/SeriesHistoricas_Layout.pdf
    result = dict(header={}, equitys=[], trailer={})
    equity_list = []
    header = dict()
    trailer = dict()  # N: Numérico; X: Alfanumérico; V: Indica que o número possui vírgula;
    # ( ): Quantidade de caracteres antes da vírgula;
    # (99): Quantidade de caracteres depois da vírgula
    total_registry = 0
    for line in uncompressed_file.readlines():
        total_registry += 1
        registry_type = convert_str_to_integer(line[0:2])
        if registry_type == 0:
            header = parse_header(line)
        if registry_type == 1:
            equity_list.append(parse_equity(line))
        if registry_type == 99:
            trailer = parse_trailer(line)

    if total_registry == trailer.get('TOTAL_REGISTRIES'):
        result['header'] = header
        result['equitys'] = equity_list
        result['trailer'] = trailer
        header = None
        equity_list = None
        trailer = None
    else:
        raise Exception(
            'Error on process the file. The number of lines doesn\'t match with the number indicated in the file.')

    return result


def parse_header(line):
    header = dict()
    header['tpreg'] = convert_str_to_integer(line[0:2])
    header['file_name'] = line[2:15]
    header['cod_origin'] = line[15:23]
    header['file_created_date'] = convert_str_to_date(line[23:31])
    header['reserve'] = line[31:245]
    return header


def parse_equity(line):
    equity = dict()
    equity['tpreg'] = convert_str_to_integer(line[0:2])
    equity['price_date'] = convert_str_to_date(line[2:10])  # Date
    equity['cod_dbi'] = line[10:12]  # coddbi
    equity['ticker'] = (line[12:24])  # codneg # symbol
    equity['tpmerc'] = convert_str_to_integer(line[24:27])
    equity['name'] = line[27:39]  # NOMRES  # symbol
    equity['especi'] = line[39:49]
    equity['prazot'] = line[49:52]
    equity['modref'] = line[52:56]  # Exchange
    equity['open_price'] = convert_str_to_decimal(line[56:69])  # preabe
    equity['high_price'] = convert_str_to_decimal(line[69:82])  # premax
    equity['low_price'] = convert_str_to_decimal(line[82:95])  # premin
    equity['avg_price'] = convert_str_to_decimal(line[95:108])  # premed
    equity['close_price'] = convert_str_to_decimal(line[108:121])  # preult
    equity['preofc'] = convert_str_to_decimal(line[121:134])
    equity['preofv'] = convert_str_to_decimal(line[134:147])
    equity['totneg'] = convert_str_to_integer(line[147:152])
    equity['quatot'] = convert_str_to_integer(line[152:170])
    equity['volume'] = convert_str_to_decimal(line[170:188])  # voltot
    equity['preexe'] = convert_str_to_decimal(line[188:201])
    equity['indopc'] = convert_str_to_integer(line[201:202])
    equity['datven'] = convert_str_to_date(line[202:210])
    equity['fatcot'] = convert_str_to_integer(line[210:217])
    equity['ptoexec'] = line[217:230]
    equity['codisi'] = line[230:242]
    equity['dismes'] = line[242:245]

    return equity


def parse_trailer(line):
    trailer = dict()
    trailer['tpreg'] = convert_str_to_integer(line[0:2])
    trailer['file_name'] = line[2:15]
    trailer['cod_origin'] = line[15:23]
    trailer['file_created_date'] = convert_str_to_date(line[23:31])
    trailer['total_of_equitys'] = convert_str_to_integer(line[31:42])
    trailer['reserve'] = line[42:245]

    return trailer
