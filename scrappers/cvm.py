# -*- coding: utf-8 -*-
import requests
from utils.browser import Browser
import xml.etree.ElementTree

__author__ = 'leandroloi'
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"

browser = Browser()
#http://sistemas.cvm.gov.br/
data = {
    'txtLogin' : '397dwllo',
    'txtSenha' : 'nova2504',
    'txtData' : '01/04/2016',
    'txtHora' : '00:00',
    'txtDocumento' : 'TODOS',
    'txtAssuntoIPE' : 'SIM',



}
for d in xrange(1,2):
    data['txtData'] = '1'+str(d)+'/04/2016'
    resp = browser.session.post('https://WWW.RAD.CVM.GOV.BR/DOWNLOAD/SolicitaDownload.asp', data, verify=False)
    if resp.status_code == requests.codes.ok:
        e = xml.etree.ElementTree.parse(resp.content).getroot()
        print xml
        for atype in e.findall('url'):
            print(atype.get('url'))

