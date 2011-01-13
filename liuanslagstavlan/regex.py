# -*- coding: utf-8 -*-
"""
liuanslagstavlan.regex
~~~~~~~~~~~~~~~~~~~~~~
Used for parsing request data. Library users aren't exposed to this module. If
formats on the remote end change, this module will have to be updated.
"""
import re

import constants

LATEST_ENTRIES_HEADER = re.compile(
    u'<h3>De \d+ %(LATEST_ENTRIES)s .*</h3>' % constants.__dict__
)
POST_NEW_ENTRY = re.compile(
    u'<p><a href=".*">%(POST_NEW_ENTRY)s</a></p>' % constants.__dict__
)
CURRENTLY_EMPTY = re.compile(
    u'<p>Inga meddelanden för tillfället.</p>'
)

MATCH_H3 = re.compile(
    u'<h3>(.*)</h3>'
)
MATCH_DATETIME = re.compile(
    u'- (.*)</p>'
)
MATCH_MAIL = re.compile(
    u'<p><a href="mailto:(.*)\?subject=.*">.*</a>'
)

MATCH_MESSAGE_ID = re.compile(
    u'<a href="index.pl\?action=display_message&id=(\d+)&language=.*"><img .*'
)
