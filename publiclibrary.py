#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


class Library(object):
    def __init__(self, name):
        '''Initialize library with a name, a list of shelves including
            a special Unshelved shelf'''
        self._name = name
        self._shelves = []
        self._unshelved = Shelf('Unshelved')
        self.shelf_add(self._unshelved)

    @property
    def name(self):
        '''Return library name.'''
        return self._name

    @name.setter
    def name(self, value):
        '''Set library name.'''
        self._name = value

    @property
    def shelves(self):
        '''Return library shelves.'''
        return self._shelves

    @property
    def unshelved(self):
        '''SReturn special Unshelved shelf.'''
        return self._unshelved

    def shelf_add(self, shelf):
        '''Add shelf to library.'''
        self._shelves.append(shelf)
        shelf.library = self

    def unshelved_pile(self, book):
        '''Add book to special unshelved shelf.'''
        self._unshelved._books.append(book)


class Shelf(object):
    def __init__(self, name):
        '''Initialize a Shelf with a name and list of books.'''
        self._name = name
        self._library = None
        self._books = []

    @property
    def name(self):
        '''Return shelf name.'''
        return self._name

    @name.setter
    def name(self, value):
        '''Set shelf name'''
        self._name = value

    @property
    def library(self):
        '''Return library shelf is in.'''
        return self._library

    @library.setter
    def library(self, value):
        '''Set library shelf is in.'''
        self._library = value

    @property
    def books(self):
        '''Return books on shelf.'''
        return self._books

    def book_add(self, book):
        '''Add book to shelf.'''
        self._books.append(book)
        book.shelf = self
        book.library = self._library

    def book_remove(self, book):
        '''Remove book from shef.'''
        self._books.remove(book)


class Book(object):
    def __init__(self, name):
        '''Initialize book with name.'''
        self._name = name
        self._shelf = None
        self._library = None

    @property
    def name(self):
        '''Return book name.'''
        return self._name

    @name.setter
    def name(self, value):
        '''Set book name'''
        self._name = value

    @property
    def shelf(self):
        '''Return shelf the book is on.'''
        return self._shelf

    @shelf.setter
    def shelf(self, value):
        '''Set which shelf book is on.'''
        self._shelf = value

    @property
    def library(self):
        '''Return name of library book is in.'''
        return self._library

    @library.setter
    def library(self, value):
        '''Set library book is in.'''
        self._library = value

    def enshelf(self, shelf):
        '''Add book to shelf.'''
        shelf.book_add(self)
        self._shelf = shelf

    def unshelf(self):
        '''Remove book from shelf.'''
        self._shelf.book_remove(self)
        self._shelf = self._library._unshelved
        self._library.unshelved_pile(self)
