# -*- coding: utf-8 -*-
import logging
import zipfile
from StringIO import StringIO

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

logger = logging.getLogger(__name__)


def uncompress_zipfile(compressed_file):
    """
        Uncompress StringIO files in Zip format.
    :type compressed_file: StringIO
    :return: flat format (.TXT)
    """
    try:
        if zipfile.is_zipfile(compressed_file):
            z = zipfile.ZipFile(compressed_file)
            for name in z.namelist():
                return StringIO(z.open(name).read())
    except Exception, e:
        logger.error('An error occurred during the uncompress. Error: {e}'.format(e=e))