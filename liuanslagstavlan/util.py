# -*- coding: utf-8 -*-
"""
liuanslagstavlan.util
~~~~~~~~~~~~~~~~~~~~~
Methods here are used internally. Library users need only be concerned with
:mod:`liuanslagstavlan.api` and :mod:`liuanslagstavlan.constants`. However, if
you plan on extending the library, this module is of interest, and care should
be taken to use the set of utilities whenever possible.
"""
import urllib
import functools
from datetime import datetime
from time import sleep

import config


class HTTPError(Exception):
    pass

class InternalHTTPError(HTTPError):
    pass


def _http_open_wrap(f):
    @functools.wraps(f)
    def wrapper(*args, **kwds):
        try:
             data = f(*args, **kwds)
        except Exception, e:
            raise InternalHTTPError()
        else:
            sleep(config.REQUEST_SLEEP)
            return data.decode(config.REMOTE_ENCODING)
    return wrapper


HTTP_LIB = None
try:
    import httplib2

    _http = httplib2.Http(config.HTTP_CACHE_DIR)
    @_http_open_wrap
    def http_open(url):
        resp, content = _http.request(url)
        return content

    HTTP_LIB = 'httplib2'
except ImportError:
    import urllib2
    
    @_http_open_wrap
    def http_open(url):
        content = urllib2.urlopen(url)
        return content.read()

    HTTP_LIB = 'urllib2'

http_open.__doc__ = """Returns data from a web resource as a string. Raises 
:exc:`InternalHTTPError`.

>>> data = http_open('http://google.com')
>>> data.find('Google') != -1
True
>>> try:
...     http_open('foo')
... except InternalHTTPError:
...     print "oops!"
... else:
...     print "should not get here"
...
oops!

:mod:`httplib2` is used internally if available, otherwise :mod:`urllib2`.
See :const:`liuanslagstavlan.config.HTTP_CACHE_DIR` and
:const:`liuanslagstavlan.config.REMOTE_ENCODING`.
"""


def raw_query(**kwds):
    """Query board's web site. This is a thin wrapper around :func:`http_open`
    that fetches "index.pl" with `kwds` encoded using :func:`urllib.urlencode`.

    >>> data = raw_query(category_id=0)
    >>> data.find('Anslagstavlan') != -1
    True

    See :const:`liuanslagstavlan.config.BASE_URL`.
    """
    return http_open("%s?%s" % (config.BASE_URL, urllib.urlencode(kwds)))


def parse_datetime(s):
    """See :const:`liuanslagstavlan.config.REMOTE_DATETIME_FORMAT`.
    """
    return datetime.strptime(s, config.REMOTE_DATETIME_FORMAT)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
