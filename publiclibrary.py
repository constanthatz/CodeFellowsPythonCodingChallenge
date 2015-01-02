#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Library(object):
    def __init__(self, name):
        self._name = name
        self._shelves = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def shelves(self):
        return self._shelves

    def shelf_add(self, shelf):
        self._shelves.append(shelf)


class Shelf(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Book(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
