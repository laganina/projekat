import json
import os
from types import SimpleNamespace
from datetime import datetime

from Model.SpecialOffer import SpecialOffer


class SpecialOfferRepository:
    def __init__(self):
        self.offers = []
        self.load()

    def load(self):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename == "offers.json":
                    with open('data/offers.json', 'r') as jsonfile:
                        lista = json.load(jsonfile)
                        for u in lista:
                            offer = json.loads(u, object_hook=lambda d: SimpleNamespace(**d))
                            self.offers.append(
                                SpecialOffer(offer.code, offer.books_and_prices.__dict__,  offer.datetime, offer.deleted))

    def get(self, code):
        for offer in self.offers:
            if offer.code == code and offer.deleted == False:
                return offer
        return None

    def get_all_undeleted_and_valid(self):
        undeleted_offers = []
        today = datetime.today().strftime("%d/%m/%Y")
        today_date = datetime.strptime(today, "%d/%m/%Y")
        for offer in self.offers:
            offer_date = datetime.strptime(offer.datetime, "%d/%m/%Y")
            if offer.deleted == False and offer_date>=today_date:
                undeleted_offers.append(offer)
        return undeleted_offers

    def get_undeleted(self, code):
        for offer in self.get_all_undeleted_and_valid():
            if offer.code == code:
                return offer
        return None

    def add(self, offer):
        offer_from_repo = self.get(offer.code)
        if offer_from_repo is None:
            self.offers.append(offer)
            json_offers = []
            for python_offer in self.offers:
                json_offers.append(python_offer.to_json())

            lista = json.dumps(json_offers)
            with open('data/offers.json', "w") as jsonfile:
                for offer in lista:
                    jsonfile.write(offer)

            return True

        elif offer_from_repo.deleted == True:

            for u in self.offers:
                if u.code == offer.code:
                    u.deleted = False
                    break

            json_offers = []
            for python_offers in self.offers:
                json_offers.append(python_offers.to_json())

            lista = json.dumps(json_offers)
            with open('data/offers.json', "w") as jsonfile:
                for offer in lista:
                    jsonfile.write(offer)
            return True

        else:
            return False

    def get_max_code(self):
        max_code = self.get_all_undeleted_and_valid()[0].code
        for offer in self.get_all_undeleted_and_valid():
            if int(offer.code) >= int(max_code):
                max_code = offer.code
        return int(max_code)


