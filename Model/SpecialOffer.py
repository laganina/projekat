import json
from Model.Book import Book
import datetime


class SpecialOffer:
    def __init__(self, code, books_and_prices, date_time, deleted):
        self.code = code
        self.books_and_prices = books_and_prices
        self.datetime = date_time
        self.deleted = deleted

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def __str__(self):
        return "\n".join([
            "",
            "{:>10}: {}".format("Rok do kad vazi akcija: ", self.datetime),
            "{:>15}: {}".format("Akcijska cena: ", self.books_and_prices)
        ])

    # def print(self):
    #     format_linije = "{:10} {:5}"
    #     print()
    #     print(format_linije.format("Rok do kada vazi akcija: ", self.datetime))
    #     format_linije1 = "{:10} {:20} {:10} {:20} {:10} {:4} {:11}{:10}       {:20}"
    #
    #     for book in self.books_and_prices.keys():
    #         print(format_linije1.format(book.code, book.name, book.isbn, book.author, book.publisher, book.page_number,
    #                                    book.year, self.books_and_prices[book], book.genre))
    #
