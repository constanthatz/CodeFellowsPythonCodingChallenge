#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Library(object):
    pass


class Shelf(object):
    pass


class Book(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

