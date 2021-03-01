import json


class SpecialOffer:
    def __init__(self, code, sale_price, date_time, deleted):
        self.code = code
        self.sale_price = sale_price
        self.datetime = date_time
        self.deleted = deleted
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)