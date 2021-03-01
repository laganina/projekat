import json


class SpecialOffer:
    def __init__(self, code, sale_price, date_time):
        self.code = code
        self.sale_price = sale_price
        self.datetime = date_time
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)