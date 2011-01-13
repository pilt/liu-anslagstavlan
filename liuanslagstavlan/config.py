# -*- coding: utf-8 -*-
"""
liuanslagstavlan.config
~~~~~~~~~~~~~~~~~~~~~~~

Holds configuration for :mod:`liuanslagstavlan` modules. You will not have to
change these settings for normal use.

.. data:: HTTP_CACHE_DIR

    Directory to store cache in if :mod:`httplib2` (or another package with
    file-based caching) is used. The path is relative to the current working
    directory.

.. data:: BASE_URL
    
    Full URL to "index.pl" of the bulletin board.

.. data:: REMOTE_ENCODING

    Encoding used on the remote end.

.. data:: REMOTE_DATETIME_FORMAT

    How datetimes are formatted at the remote end.

.. data:: REQUEST_SLEEP

    To let the remote server rest. Given in seconds.

"""

HTTP_CACHE_DIR = '.liuanslagstavlan-http-cache'
BASE_URL = 'http://www2.student.liu.se/cgi-bin/anslagstavlan/index.pl'
REMOTE_ENCODING = 'latin-1'
REMOTE_DATETIME_FORMAT = '%d/%m %Y, %H:%M'
REQUEST_SLEEP = 0
