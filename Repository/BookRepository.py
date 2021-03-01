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
                    with open('books.json', 'r') as jsonfile:
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
            with open('books.json', "w") as jsonfile:
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
            with open('books.json', "w") as jsonfile:
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
                with open('books.json', "w") as jsonfile:
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
            with open('books.json', "w") as jsonfile:
                for book in lista:
                    jsonfile.write(book)

            return True

        return False


b1 = Book('code1','Saptac','109035','Donato Karizi','Vulkan',358,2017,799,'novel',False)
b2 = Book('code2','Ubistvo u Orijent Ekspresu','128754','Agata Kristi','Laguna',254,2017,599,'novel',False)
b3 = Book('code3','Nastavlja se cerupanje haskih curki','036739','Vojislav Seselj','Srpska radikalna stranka',270,2011,999,'scientific literature',False)
b4 = Book('code4','Maternji jezik','021888','Nenad Grujicic','Prosveta',136,2018,499,'poetry',True)
b5 = Book('code5','Biblija','424666','Isus Hrist','Pravoslavna crkva',1200,1,1500,'sci-fi',False)
b6 = Book('code6', 'Veliki prasak je eksplodirao','197000','Russel R. Standish','Grafeks',191,2004,500,'scientific literature',False)
b7 = Book('code7','Iluminati 666','110459','Milan Vidojevic','Mali Princ',199,2015,400,'sci-fi',False)
b8 = Book('code8','21 lekcija za 21 vek','131662','Juval Noa Harari','Laguna',430,2019,1299,'scientific literature',True)
b9 = Book('code9','Lovac u zitu','123456','J.D. Selindzer','Laguna',253, 2017, 899,'novel',True)
b10 = Book('code10','Crne rupe i bebe vaseljene','591138','Stiven Hoking','Alnari',162,2002,399,'scientific literature',True)

bookrepo = BookRepository()
bookrepo.add(b1)
bookrepo.add(b2)
bookrepo.add(b3)
bookrepo.add(b4)
bookrepo.add(b5)
bookrepo.add(b6)
bookrepo.add(b7)
bookrepo.add(b8)
bookrepo.add(b9)
bookrepo.add(b10)

for b in bookrepo.books:
    b.print_book()
#bookrepo = BookRepository()
#bookrepo.add(b)

# for l in bookrepo.books:
#     print(l)
#


# print(bookrepo.books)
# dodavati po listama

# print('brljotina')
# bookrepo.remove('code1')
# for l in bookrepo.books:
#      print(l)
# list = bookrepo.get_all()
#
# for l in list:
#      print(l.code)

# bookrepo.update(b1)
#
# for l in bookrepo.books:
#     print(l.name)
