import json
from json import JSONEncoder
import jsonpickle


class Book:
    def __init__(self, code, name, isbn, author, publisher, page_number, year, price, genre):
        self.code = code
        self.name = name
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.page_number = page_number
        self.year = year
        self.price = price
        self.genre = genre


#b = Book('code1', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel')
#print(jsonpickle.encode(b, unpicklable= False))