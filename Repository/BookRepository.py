import json
import jsonpickle

from Model.Book import Book


def add(book):
    with open('../Data/books.json', "a") as outputfile:
        jsonobject = json.dump(jsonpickle.encode(book,unpicklable=False,indent=0),outputfile)


b = Book('code1', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel')
add(b)