import json


class Receipt:
    def __init__(self, code, cashier, date_time, price_list, deleted):
        self.code = code
        self.cashier = cashier
        self.date_time = date_time
        self.price_list = price_list
        self.full_price = self.calculate_price()
        self.deleted = deleted
    def calculate_price(self):
        price = 0
        for p in self.price_list.values():
            price = price + p
        return price
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
price_list={"LOTR1": 1230, "LOTR2":1231, "LOTR3": 1234}
r = Receipt(12, 'Roger', '12.06 - 18pm', price_list)
print(r.full_price)

