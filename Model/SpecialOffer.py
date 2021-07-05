import json

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
