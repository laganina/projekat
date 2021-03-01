import json
from types import SimpleNamespace

import jsonpickle
import os

from Model.Book import Book


class BookRepository:

    def __init__(self):
        self.books = []
        self.load()
        #print(self.books)

    def load(self):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename == 'books.json':
                    with open('books.json','r') as jsonfile:
                        lista = json.load(jsonfile)
                        self.books = lista

    def add(self, book):
        if self.get(str(book.code)) is None:
            self.books.append(book.to_json())
            lista = json.dumps(self.books)
            with open('books.json', "w") as jsonfile:
                for book in lista:
                    jsonfile.write(book)
        else :
            return None

    def get_all(self):
        list = []
        for b in self.books:
            book = json.loads(b, object_hook=lambda d: SimpleNamespace(**d))
            list.append(Book(book.code, book.name, book.isbn, book.author, book.publisher, book.page_number, book.year, book.price, book.genre))
        return list

    def get(self, code):
        for b in self.get_all():
            # print(b.code)
            if str(b.code) == code:
                return b

        return None


    def remove(self, code):
        books_for_dump = []
        if self.get(code) is not None:
            books = self.get_all()
            for book in books:
                if str(book.code) != code:
                    books_for_dump.append(book.to_json())
            self.books = books_for_dump
            books_for_dump = json.dumps(books_for_dump)
            with open('books.json', "w") as jsonfile:
                for book in books_for_dump:
                    jsonfile.write(book)

# def add(book):
#     with open('books.json', "a") as outputfile:
#         jsonobject = json.dump(jsonpickle.encode(book,unpicklable=False, indent=0),outputfile)

b = Book('code4', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel')
bookrepo = BookRepository()
bookrepo.add(b)


for l in bookrepo.books:
     print(l)
#print(bookrepo.books)
#dodavati po listama

#print('brljotina')
bookrepo.remove('code3')
for l in bookrepo.books:
     print(l)
# list = bookrepo.get_all()
#
# for l in list:
#      print(l.code)
