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
        '''Return special Unshelved shelf.'''
        return self._unshelved

    def shelf_add(self, shelf):
        '''Add shelf to library.'''
        self._shelves.append(shelf)
        shelf.library = self

    def unshelved_pile(self, book):
        '''Add book to special unshelved shelf.'''
        self._unshelved._books.append(book)
        book.shelf = self._unshelved

    @property
    def report(self):
        '''Return names of books in library by shelf.'''
        print('Library: ', self._name)
        for x in self._shelves:
            x.report


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
        '''Add book to shelf. Set shelf and library values for book itself'''
        self._books.append(book)
        book.shelf = self
        book.library = self._library

    def book_remove(self, book):
        '''Remove book from shef.'''
        self._books.remove(book)

    @property
    def report(self):
        '''Return names of books on shelf.'''
        print('Shelf: ', self._name)
        for x in self._books:
            print('\t', x.name)


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

    def unshelf(self):
        '''Remove book from shelf, set shelf as unshelved, add to unshelved pile in library.'''
        self._shelf.book_remove(self)
        self._library.unshelved_pile(self)

if __name__ == "__main__":
    print('''First I create a library, 2 shleves, and 5 books.\n''')
    '''Create library, shelves, and books'''
    g = Library('Alexandria')
    h = Shelf('Fun')
    i = Shelf('Two')
    j = Book('Hitchhikers Guide to the Galaxy')
    k = Book('Dune')
    l = Book('Game of Thrones')
    m = Book('Every Grain of Rice')
    n = Book('Kingdom Come')

    print('''Then I add the shelves to the library.\n''')
    '''Add the shelves to the library.'''
    g.shelf_add(h)
    g.shelf_add(i)

    print('''Then I enshelf the books.\n''')
    '''Enshelf the books.'''
    j.enshelf(h)
    k.enshelf(h)
    l.enshelf(h)
    m.enshelf(i)
    n.enshelf(i)

    print('''Now I show that the library methods except for unshelved_pile work properly.''')
    print('Library name: {}'.format(g.name))
    print('Library added shelves: {}, {}, {}.'.format(*[x.name for x in g.shelves]))
    print('Library has one special shelf: {}.'.format(g.unshelved.name))
    print('Here is a library report:\n')
    g.report
    print()

    print('''Show that the shelf methods except book_remove work properly.''')
    print('Shelf name: {}'.format(h.name))
    print('Shelf added books: {}, {}, {}.'.format(*[x.name for x in h.books]))
    print('Here is a shelf report.\n')
    h.report
    print()

    print('''Now I unshelf a book''')
    '''Unshelf a book'''
    j.unshelf()

    print('''Show that unshelved_pile and book_remove worked properly.''')
    print('Here is a library report:\n')
    g.report
