import json
import os
from types import SimpleNamespace

from Model.Book import Book


# TREBALO BI DA SE BARATA SA PYTHON OBJEKTIMA

class BookRepository:
    def __init__(self):
        self.books = []
        self.load()

    def load(self):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename == 'books.json':
                    with open("data/books.json", 'r') as jsonfile:
                        lista = json.load(jsonfile)
                        for b in lista:
                            book = json.loads(b, object_hook=lambda d: SimpleNamespace(**d))
                            self.books.append(
                                Book(book.code, book.name, book.isbn, book.author, book.publisher, book.page_number,
                                     book.year, book.price, book.genre, book.deleted))

    def add(self, book):

        book_from_repo = self.get(book.code)

        if book_from_repo is None:
            self.books.append(book)
            json_books = []
            for python_book in self.books:
                json_books.append(python_book.to_json())

            lista = json.dumps(json_books)
            with open('data/books.json', "w") as jsonfile:
                for book in lista:
                    jsonfile.write(book)

            return True

        elif book_from_repo.deleted == True:

            for b in self.books:
                if b.code == book.code:
                    b.deleted = False
                    break

            json_books = []
            for python_book in self.books:
                json_books.append(python_book.to_json())

            lista = json.dumps(json_books)
            with open('data/books.json', "w") as jsonfile:
                for book in lista:
                    jsonfile.write(book)
            return True

        else:
            return False

    def get_all_undeleted(self):
        undeleted_books = []
        for book in self.books:
            if book.deleted == False:
                undeleted_books.append(book)

        return undeleted_books

    def get_undeleted(self, code):
        for book in self.get_all_undeleted():
            if book.code == code:
                return book
        return None

    def get(self, code):
        for book in self.books:
            if book.code == code:
                return book
        return None

    def remove(self, code):
        book_from_repo = self.get(code)

        if book_from_repo is not None:
            if book_from_repo.deleted == False:
                for b in self.books:
                    if b.code == code:
                        b.deleted = True
                        break

                json_books = []
                for python_book in self.books:
                    json_books.append(python_book.to_json())

                lista = json.dumps(json_books)
                with open('data/books.json', "w") as jsonfile:
                    for book in lista:
                        jsonfile.write(book)

                return True

        return False

    def update(self, updated_book):
        book_from_repo = self.get(updated_book.code)
        if book_from_repo is not None:
            for b in self.books:
                if b.code == updated_book.code:
                    b.author = updated_book.author
                    b.name = updated_book.name
                    b.isbn = updated_book.isbn
                    b.publisher = updated_book.publisher
                    b.page_number = updated_book.page_number
                    b.year = updated_book.year
                    b.price = updated_book.price
                    b.genre = updated_book.genre
                    b.deleted = updated_book.deleted
                    break

            json_books = []
            for python_book in self.books:
                json_books.append(python_book.to_json())

            lista = json.dumps(json_books)
            with open('data/books.json', "w") as jsonfile:
                for book in lista:
                    jsonfile.write(book)

            return True

        return False
