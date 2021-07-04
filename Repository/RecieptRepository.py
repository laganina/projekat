import json
import os
from types import SimpleNamespace
from datetime import datetime

from Model.Receipt import Receipt


class RecieptRepository:
    def __init__(self):
        self.receipts = []
        self.load()

    def load(self):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename == "receipts.json":
                    with open('data/receipts.json', 'r') as jsonfile:
                        lista = json.load(jsonfile)
                        for u in lista:
                            receipt = json.loads(u, object_hook=lambda d: SimpleNamespace(**d))
                            self.receipts.append(
                                Receipt(receipt.code,receipt.cashier, receipt.datetime,
                                        receipt.books.__dict__, receipt.s_offers.__dict__, receipt.deleted))

    def get(self, code):
        for receipt in self.receipts:
            if receipt.code == code and receipt.deleted == False:
                return receipt
        return None

    def get_all_undeleted(self):
        undeleted_receipts = []
        for receipt in self.receipts:
            if receipt.deleted == False:
                undeleted_receipts.append(receipt)

        return undeleted_receipts

    def get_undeleted(self, code):
        for receipt in self.get_all_undeleted():
            if receipt.code == code:
                return receipt
        return None

    def add(self, receipt):
        receipt_from_repo = self.get(receipt.code)
        if receipt_from_repo is None:
            self.receipts.append(receipt)
            json_receipts = []
            for python_receipt in self.receipts:
                json_receipts.append(python_receipt.to_json())

            lista = json.dumps(json_receipts)
            with open('data/receipts.json', "w") as jsonfile:
                for receipt in lista:
                    jsonfile.write(receipt)

            return True

        elif receipt_from_repo.deleted == True:

            for u in self.receipts:
                if u.code == receipt.code:
                    u.deleted = False
                    break

            json_receipts = []
            for python_receipt in self.receipts:
                json_receipts.append(python_receipt.to_json())

            lista = json.dumps(json_receipts)
            with open('data/receipts.json', "w") as jsonfile:
                for receipt in lista:
                    jsonfile.write(receipt)

            return True

        else:
            return False