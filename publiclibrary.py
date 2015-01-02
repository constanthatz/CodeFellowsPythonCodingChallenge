#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Library(object):
    def __init__(self, name):
        self._name = name
        self._shelves = []
        self._unshelved = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def shelves(self):
        return self._shelves

    @property
    def unhelved(self):
        return self._unshelved

    def shelf(self, shelf):
        self._shelves.append(shelf)


class Shelf(object):
    def __init__(self, name):
        self._name = name
        self._books = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def books(self):
        return self._books

    def book(self, book):
        self._books.append(book)

    def book_remove(self, book):
        self._books.remove(book)


class Book(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def enshelf(self, shelf):
        shelf.book(self)

    def unshelf(self, shelf):
        shelf.book_remove(self)

