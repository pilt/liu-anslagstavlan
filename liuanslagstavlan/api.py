# -*- coding: utf-8 -*-
"""
liuanslagstavlan.api
~~~~~~~~~~~~~~~~~~~~
The interface looks a lot like the :mod:`django` ORM interface. Example usage:

>>> cat = Category.objects.get(0)
Traceback (most recent call last):
    ...
Invalid: invalid id 0
>>> ride_offers = Category.objects.get(41)
>>> # The constants can be found in the `constants` module.
>>> ride_offers.title == constants.CATEGORIES[41]
True
>>> entry = Entry.objects.get(0)
Traceback (most recent call last):
    ...
Empty: empty entry 0
"""

import re

from util import raw_query, parse_datetime
import regex
import config
import constants


class Error(Exception):
    """Base exception of module."""
    pass


class Manager(object):
    pass


class EntryManager(Manager):
    """Entry manager class. You should always work with :attr:`Entry.objects`,
    which is an instance of this class."""

    def get(self, id):
        """Fetch entry by id. Raises :exc:`Entry.Empty` if the entry is
        unfound. Blocking."""
        data = raw_query(
            action='display_message',
            id=int(id),
            language='sv',
        )

        token_order = ['title', 'mail1', 'submitted', 'body', 'mail2', 'report']
        cur_token_id = 0

        title = u''
        submitted = None
        body = u''
        mail = u''

        token = None
        for line in data.splitlines()[1:-1]:
            token = token_order[cur_token_id]
            line = line.strip()
            if token == 'title':
                title = regex.MATCH_H3.match(line).groups()[0]
                cur_token_id += 1
            elif token == 'mail1':
                mail = regex.MATCH_MAIL.match(line).groups()[0]
                cur_token_id += 1
            elif token == 'submitted':
                try:
                    submitted = parse_datetime(
                        regex.MATCH_DATETIME.match(line).groups()[0]
                    )
                except:
                    pass
                cur_token_id += 1
            elif token == 'body':
                start_p = '<p>'
                end_p = '</p>'
                ends_now = line.endswith(end_p)
                body += line.replace(start_p, '').replace(end_p, '')
                if ends_now:
                    cur_token_id += 1
                else:
                    body += '\n'
            elif token == 'mail2':
                cur_token_id += 1
            elif token == 'report':
                break

        assert token == token_order[-1]
        if not title and not body:
            raise Entry.Empty('empty entry %s' % id)
        return Entry(id, title, mail, submitted, body)


class Entry(object):
    """A single board entry.

    .. attribute:: objects

        Instance of :class:`EntryManager`.

    .. attribute:: id
        
        Numerical id of the entry.

    .. attribute:: title
        
        Title of the entry, as entered by the poster.

    .. attribute:: mail
        
        Email address of the poster.

    .. attribute:: submitted
        
        :obj:`datetime.datetime` instance of when the entry was submitted.

    .. attribute:: body

        Body of the entry, as entered by the poster. This includes HTML.

    """

    class Empty(Error):
        """Empty entry error. Raised by :func:`EntryManager.get`."""
        pass

    def __init__(self, id, title, mail, submitted, body):
        self.id = id
        self.title = title
        self.mail = mail
        self.submitted = submitted
        self.body = body

    objects = EntryManager()

    def __repr__(self):
        return u"<Category %s>" % self.id


class CategoryManager(Manager):
    """Category manager class. You should always work with
    :attr:`Category.objects`, which is an instance of this class."""
    
    def get(self, id):
        """Fetch category by id. Blocking."""
        if id in constants.CATEGORIES:
            title = constants.CATEGORIES[id]
        else:
            raise Category.Invalid('invalid id %s' % id)

        data = raw_query(
            category_id=int(id),
            language='sv',
        )

        for reg in [
            regex.LATEST_ENTRIES_HEADER,
            regex.CURRENTLY_EMPTY,
            ]:
            if re.search(reg, data):
                return Category(id, title, [])

        lines = data.splitlines()
        entry_ids = []
        for line in lines:
            if regex.POST_NEW_ENTRY.search(line):
                continue

            match = regex.MATCH_MESSAGE_ID.search(line)
            if not match:
                continue

            entry_ids.append(int(match.groups()[0]))

        entries = []
        for eid in entry_ids:
            try:
                entries.append(Entry.objects.get(eid))
            except Entry.Empty:
                pass
        return Category(id, title, entries)

    def all(self):
        """Fetch all categories. Blocking.

        See :mod:`liuanslagstavlan.constants`.
        """
        for id in constants.CATEGORY_IDS:
            yield self.get(id)


class Category(object):
    """Class representing a board category.

    .. attribute:: objects

        Instance of :class:`CategoryManager`.

    .. attribute:: id
        
        Numerical id of the category.

    .. attribute:: title
        
        Title of the category. See :mod:`liuanslagstavlan.constants`.

    .. attribute:: entries
        
        A list of :class:`Entry` objects.
    """

    def __init__(self, id, title, entries):
        self.id = id
        self.title = title
        self.entries = entries

    class Invalid(Error):
        """Raised when a category cannot be created because it is invalid. This
        occurs for example if you call :func:`CategoryManager.get` (accessed
        through :attr:`Category.objects`) with an invalid id. """
        pass

    def __repr__(self):
        return u"<Category %s>" % self.id

    objects = CategoryManager()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
