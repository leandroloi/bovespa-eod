# -*- coding: utf-8 -*-
from decimal import Decimal
import logging
from datetime import datetime as dt
from bs4 import BeautifulSoup as Bs

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"


logger = logging.getLogger(__name__)


def parse_files_form(page):
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


def __convert_str_to_date(str_date):
    return dt.strptime(str_date, '%Y%m%d')


def __convert_str_to_integer(str_number):
    # N: Numérico;
    return int(str_number)


def __trim_str(str_value):
    return str_value.strip()


def __convert_str_to_decimal(str_number):
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


def __convert_to_tuple(equity):
    return (equity.get('price_date'), equity.get('cod_dbi'), equity.get('ticker'), equity.get('tpmerc'),
                 equity.get('especi'), equity.get('prazot'), equity.get('open_price'), equity.get('high_price'),
                 equity.get('low_price'), equity.get('avg_price'), equity.get('close_price'), equity.get('preofc'),
                 equity.get('preofv'), equity.get('totneg'), equity.get('quatot'), equity.get('volume'),
                 equity.get('preexe'), equity.get('indopc'), equity.get('datven'), equity.get('fatcot'),
                 equity.get('ptoexec'), equity.get('codisi'), equity.get('dismes'))


def get_trailer(data_file):
    trailer = dict()
    data_file.seek(-1024, 2)
    last = data_file.readlines()[-1].decode()
    registry_type = __convert_str_to_integer(last[0:2])
    if registry_type == 99:
        trailer = __parse_trailer(last)

    return trailer


def get_header(data_file):
    header = dict()
    first_line = data_file.readlines()[0]
    registry_type = __convert_str_to_integer(first_line[0:2])
    if registry_type == 0:
        header = __parse_header(first_line)

    return header


def parse_historic_file(data_file, skip, end=None):
    # Parse data_file as layout: http://www.bmfbovespa.com.br/pt-br/download/SeriesHistoricas_Layout.pdf
    result = dict(spot=[], option=[], auction=[], fractionary=[], term=[], future=[])
    """
    010 VISTA
    012 EXERCÍCIO DE OPÇÕES DE COMPRA
    013 EXERCÍCIO DE OPÇÕES DE VENDA
    017 LEILÃO
    020 FRACIONÁRIO
    030 TERMO
    050 FUTURO COM RETENÇÃO DE GANHO
    060 FUTURO COM MOVIMENTAÇÃO CONTÍNUA
    070 OPÇÕES DE COMPRA
    080 OPÇÕES DE VENDA
    """
    tpmerc = dict(vista=10, exec_compra=12, exec_venda=13, leilao=17, fracionario=20, termo=30, futuro_ret=50,
                  fut_cont=60, opcao_compra=70, opcao_venda=80)
    processed = 0
    for line in data_file:#itertools.islice(data_file, skip, end):
        registry_type = __convert_str_to_integer(line[0:2])
        if registry_type == 1:
            processed += 1
            #logger.debug('Total processed: {total}'.format(total=processed))
            #print('Total processed: {total}'.format(total=processed))
            equity = __parse_equity(line)
            #print equity
            equity_tuple = __convert_to_tuple(equity)
            equity_type = equity.get('tpmerc')

            if equity_type== tpmerc.get('vista'):  # restricts to spot market
                result['spot'].append(equity_tuple)

            elif equity_type == tpmerc.get('fracionario'):
                result['fractionary'].append(equity_tuple)

            elif equity_type in [tpmerc.get('exec_compra'), tpmerc.get('exec_venda'), tpmerc.get('opcao_compra'),
                                        tpmerc.get('opcao_venda')]:
                result['option'].append(equity_tuple)

            elif equity_type == tpmerc.get('leilao'):
                result['auction'].append(equity_tuple)

            elif equity_type == tpmerc.get('termo'):
                result['term'].append(equity_tuple)

            elif equity_type in[tpmerc.get('futuro_ret'), tpmerc.get('fut_cont')]:
                result['future'].append(equity_tuple)

    return result


def __parse_header(line):
    header = dict()
    header['tpreg'] = __convert_str_to_integer(line[0:2])
    header['file_name'] = line[2:15]
    header['cod_origin'] = line[15:23]
    header['file_created_date'] = __convert_str_to_date(line[23:31])
    header['reserve'] = __trim_str(line[31:245])
    return header



def __parse_equity(line):
    equity = dict()

    equity['tpreg'] = __convert_str_to_integer(line[0:2])
    equity['price_date'] = __convert_str_to_date(line[2:10])  # Date
    equity['cod_dbi'] = __convert_str_to_integer(line[10:12])  # coddbi
    equity['ticker'] = __trim_str(line[12:24]) # codneg symbol
    equity['tpmerc'] = __convert_str_to_integer(line[24:27])
    #equity['name'] = __trim_str(line[27:39])  # NOMRES  # symbol
    equity['prazot'] = __trim_str(line[49:52])
    equity['modref'] = line[52:56]  # symbol
    equity['open_price'] = __convert_str_to_decimal(line[56:69])  # preabe
    equity['high_price'] = __convert_str_to_decimal(line[69:82])  # premax
    equity['low_price'] = __convert_str_to_decimal(line[82:95])  # premin
    equity['avg_price'] = __convert_str_to_decimal(line[95:108])  # premed
    equity['close_price'] = __convert_str_to_decimal(line[108:121])  # preult
    equity['preofc'] = __convert_str_to_decimal(line[121:134])
    equity['preofv'] = __convert_str_to_decimal(line[134:147])
    equity['totneg'] = __convert_str_to_integer(line[147:152])
    equity['quatot'] = __convert_str_to_integer(line[152:170])
    equity['volume'] = __convert_str_to_decimal(line[170:188])  # voltot
    equity['preexe'] = __convert_str_to_decimal(line[188:201])
    equity['indopc'] = __convert_str_to_integer(line[201:202])
    equity['datven'] = __convert_str_to_date(line[202:210])
    equity['fatcot'] = __convert_str_to_integer(line[210:217])
    equity['ptoexec'] = line[217:230]
    equity['codisi'] = line[230:242]
    equity['dismes'] = __convert_str_to_integer(line[242:245])

    return equity


def __parse_trailer(line):
    trailer = dict()
    trailer['tpreg'] = __convert_str_to_integer(line[0:2])
    trailer['file_name'] = line[2:15]
    trailer['cod_origin'] = line[15:23]
    trailer['file_created_date'] = __convert_str_to_date(line[23:31])
    trailer['total_of_equities'] = __convert_str_to_integer(line[31:42])
    trailer['reserve'] = __trim_str(line[42:245])

    return trailer
