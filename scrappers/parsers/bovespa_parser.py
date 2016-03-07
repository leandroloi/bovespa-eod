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
    #N: Numérico;
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


def parse_historic_data(uncompressed_file):
    # Parse file as layout: http://www.bmfbovespa.com.br/pt-br/download/SeriesHistoricas_Layout.pdf
    result = dict(header={}, quotes=[], trailer={})
    quote_list = []
    quote = dict()
    header = dict()
    trailer = dict()                # N: Numérico; X: Alfanumérico; V: Indica que o número possui vírgula;
                                    # ( ): Quantidade de caracteres antes da vírgula;
                                    # (99): Quantidade de caracteres depois da vírgula
    total_registry = 0
    for line in uncompressed_file.readlines():
        total_registry += 1
        registry_type = convert_str_to_integer(line[0:2])
        if registry_type == 0:
            header['TPREG'] = registry_type
            header['FILE_NAME'] = line[2:15]
            header['COD_ORIGIN'] = line[15:23]
            header['FILE_CREATED_DATE'] = convert_str_to_date(line[23:31])
            header['RESERVE'] = line[31:245]
        elif registry_type == 1:
            quote['TPREG'] = registry_type
            quote['DATE'] = convert_str_to_date(line[2:10])
            quote['CODBDI'] = line[10:12]
            quote['CODNEG'] = (line[12:24])
            quote['TPMERC'] = convert_str_to_integer(line[24:27])
            quote['NOMRES'] = line[27:39]
            quote['ESPECI'] = line[39:49]
            quote['PRAZOT'] = line[49:52]
            quote['MODREF'] = line[52:56]
            quote['PREABE'] = convert_str_to_decimal(line[56:69])
            quote['PREMAX'] = convert_str_to_decimal(line[69:82])
            quote['PREMIN'] = convert_str_to_decimal(line[82:95])
            quote['PREMED'] = convert_str_to_decimal(line[95:108])
            quote['PREULT'] = convert_str_to_decimal(line[108:121])
            quote['PREOFC'] = convert_str_to_decimal(line[121:134])
            quote['PREOFV'] = convert_str_to_decimal(line[134:147])
            quote['TOTNEG'] = convert_str_to_integer(line[147:152])
            quote['QUATOT'] = convert_str_to_integer(line[152:170])
            quote['VOLTOT'] = convert_str_to_decimal(line[170:188])
            quote['PREEXE'] = convert_str_to_decimal(line[188:201])
            quote['INDOPC'] = convert_str_to_integer(line[201:202])
            quote['DATVEN'] = convert_str_to_date(line[202:210])
            quote['FATCOT'] = convert_str_to_integer(line[210:217])
            quote['PTOEXE'] = line[217:230]
            quote['CODISI'] = line[230:242]
            quote['DISMES'] = line[242:245]

            quote_list.append(quote)

        elif registry_type == 99:
            trailer['TPREG'] = registry_type
            trailer['FILE_NAME'] = line[2:15]
            trailer['COD_ORIGIN'] = line[15:23]
            trailer['FILE_CREATED_DATE'] = convert_str_to_date(line[23:31])
            trailer['TOTAL_REGISTRIES'] = convert_str_to_integer(line[31:42])
            trailer['RESERVE'] = line[42:245]

    if total_registry == trailer.get('TOTAL_REGISTRIES'):
        result['header'] = header
        result['quotes'] = quote_list
        result['trailer'] = trailer
        header = None
        quote_list = None
        trailer = None
    else:
        raise Exception(
            'Error on process the file. The number of lines doesn\'t match with the number indicated in the file.')

    return result
