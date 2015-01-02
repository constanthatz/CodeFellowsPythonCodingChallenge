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
    def unshelved(self):
        return self._unshelved

    def shelf_add(self, shelf):
        self._shelves.append(shelf)
        shelf.library = self

    def unshelved_pile(self, book):
        self._unshelved.append(book)


class Shelf(object):
    def __init__(self, name):
        self._name = name
        self._library = None
        self._books = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, value):
        self._library = value

    @property
    def books(self):
        return self._books

    def book_add(self, book):
        self._books.append(book)
        book.shelf = self
        book.library = self._library

    def book_remove(self, book):
        self._books.remove(book)
        book.shelf = None


class Book(object):
    def __init__(self, name):
        self._name = name
        self._shelf = None
        self._library = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def shelf(self):
        return self._shelf

    @shelf.setter
    def shelf(self, value):
        self._shelf = value

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, value):
        self._library = value

    def enshelf(self, shelf):
        shelf.book(self)
        self._shelf = shelf

    def unshelf(self):
        self._shelf.book_remove(self)
        self._shelf = None
        self._library.unshelved_pile(self)
