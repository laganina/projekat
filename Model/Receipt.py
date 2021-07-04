import json


class Receipt:
    def __init__(self, code, cashier, datetime, books, s_offers, deleted):
        self.code = code
        self.cashier = cashier
        self.datetime = datetime
        self.books = books
        self.s_offers = s_offers
        self.full_price = self.calculate_price()
        self.deleted = deleted

    def calculate_price(self):
        price = 0
        for p in self.books.values():
            price += p[0]*p[1]
        for p in self.s_offers.values():
            price += p[0]*p[1]
        return price

    def __str__(self):
        return 'Receipt(code=' + str(self.code) + ' ,cashier=' + self.cashier+' , date_time=' + self.datetime + ' , books=' + str(self.books)+' , offers=' + str(self.s_offers)+' , full_price=' + str(self.full_price) +')'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


