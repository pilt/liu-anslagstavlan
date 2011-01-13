# -*- coding: utf-8 -*-
"""
liuanslagstavlan.constants
~~~~~~~~~~~~~~~~~~~~~~~~~~
Library users probably want to work with this module. No values are discovered
dynamically by querying the web server, this module is broken if remote ids and
such are changed.
 
.. data:: CATEGORIES

    A :obj:`dict` with category ids for keys and American English names for
    values.

    >>> CATEGORIES[11]
    u'accommodation offered, Link\\xf6ping'

.. data:: CATEGORY_ITEMS

    A sorted :obj:`list` of :obj:`tuple`\s.

    >>> CATEGORY_ITEMS[0]
    (11, u'accommodation offered, Link\\xf6ping')

.. data:: CATEGORY_IDS

    Available category ids sorted.

    >>> CATEGORY_IDS[-1]
    62

.. data:: CATEGORY_NAMES

    Available category names sorted.

    >>> CATEGORY_NAMES[0]
    u'accommodation offered, Link\\xf6ping'

"""

LATEST_ENTRIES = u'senaste anslagen i'
POST_NEW_ENTRY = u'Skriv nytt anslag'
CURRENTLY_EMPTY = u'Inga meddelanden för tillfället.'

CATEGORIES = {
    11: u'accommodation offered, Linköping',
    12: u'accommodation wanted, Linköping',
    13: u'accommodation trade, Linköping',

    16: u'accommodation offered, Norrköping',
    17: u'accommodation wanted, Norrköping',
    18: u'accommodation trade, Norrköping',

    21: u'thesis opponents',
    22: u'jobs wanted',
    23: u'jobs offered',

    31: u'books for sale',
    32: u'books wanted',
    32: u'books for trading',

    41: u'ride offers',
    42: u'seeking ride',

    51: u'misc. wanted',
    52: u'misc. for sale',
    53: u'giveaways',
    54: u'lost and found',

    61: u'tickets wanted',
    62: u'tickets for sale',
}

CATEGORY_ITEMS = sorted(CATEGORIES.items(), key=lambda t: t[0])
CATEGORY_IDS = [id for id, name in CATEGORY_ITEMS]
CATEGORY_NAMES = [name for id, name in CATEGORY_ITEMS]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
