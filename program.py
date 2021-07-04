from Model.Book import Book
from Model.User import User
from Model.Receipt import Receipt
import random
import string
from Repository.BookRepository import BookRepository
from Repository.UserRepository import UserRepository
from Repository.SpecialOfferRepository import SpecialOfferRepository
from Repository.RecieptRepository import RecieptRepository

from Model.SpecialOffer import SpecialOffer
import datetime


def login():
    userrepo = UserRepository()
    print('Molimo Vas da se ulogujete: ')
    i = 0
    while i <= 3:
        if i == 3:
            print('Tri puta ste neuspesno uneli kredencijale.')
            return None

        username = input("Molimo Vas da unesete korisnicko ime: \n")
        password = input("Molimo Vas da unesete lozinku: \n")

        user = userrepo.get_undeleted(username)
        if user is None:
            print('Neuspesno ste se ulovogali. Pokusajte opet. \n')
            i += 1
            continue
        else:
            if password != user.password:
                print('Neuspesno ste se ulogovali. Pokusajte opet. \n')
                i += 1
                continue
            else:
                print("Uspesno ste se ulogovali.")
                return user


def prikazsvihknjiga(usertype):
    bookrepo = BookRepository()
    format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20}"
    format_linije1 = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20} {:8}"

    if usertype == "administrator":
        print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr",
                                    "Brisano"))
        print(
            format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                  "-" * 20, "-" * 8))
        for book in bookrepo.books:
            book.printdeleted()
    else:
        print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
        print(
            format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                 "-" * 20))
        for book in bookrepo.get_all_undeleted():
            book.print()
    print()
    i = 666
    while i != 0:
        print('Odaberite kriterijum sortiranja.')
        print('1 --- po nazivu.')
        print('2 --- po kategoriji.')
        print('3 --- po autoru.')
        print('4 --- po izdavacu.')
        print('5 --- po ceni.')
        print('0 --- povratak na prethodni meni.')
        i = int(input())
        books = bookrepo.get_all_undeleted()
        booksdel = bookrepo.books

        if i == 1:

            if usertype == "administrator":
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                booksdel.sort(key=lambda x: x.name, reverse=False)

                for book in booksdel:
                    book.printdeleted()
            else:
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                books.sort(key=lambda x: x.name, reverse=False)

                for book in books:
                    book.print()
            print()

        elif i == 2:

            if usertype == "administrator":
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                booksdel.sort(key=lambda x: x.name, reverse=False)

                for book in booksdel:
                    book.printdeleted()
            else:
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                books.sort(key=lambda x: x.genre, reverse=False)

                for book in books:
                    book.print()
            print()

        elif i == 3:

            if usertype == "administrator":
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                booksdel.sort(key=lambda x: x.name, reverse=False)

                for book in booksdel:
                    book.printdeleted()
            else:
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                books.sort(key=lambda x: x.author, reverse=False)

                for book in books:
                    book.print()

        elif i == 4:

            if usertype == "administrator":
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                booksdel.sort(key=lambda x: x.name, reverse=False)

                for book in booksdel:
                    book.printdeleted()
            else:
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                books.sort(key=lambda x: x.publisher, reverse=False)

                for book in books:
                    book.print()

        elif i == 5:

            if usertype == "administrator":
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                booksdel.sort(key=lambda x: x.name, reverse=False)

                for book in booksdel:
                    book.printdeleted()
            else:
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                books.sort(key=lambda x: x.price, reverse=False)

                for book in books:
                    book.print()

        else:
            return None


# code=code1
# codesubstr= Od od
def containsCode(code, codesubstr):
    return codesubstr.lower() in code.lower()


def containsName(name, namesubstr):
    return namesubstr.lower() in name.lower()


def containsAuthor(author, authorsubstr):
    return authorsubstr.lower() in author.lower()


def containsGenre(genre, genresubstr):
    return genresubstr.lower() in genre.lower()


def containsPublisher(publisher, publishersubstr):
    return publishersubstr.lower() in publisher.lower()


def isinpricerange(min, max, price):
    return min <= price <= max


def svepretrageKnjiga(usertype):
    bookrepo = BookRepository()
    books = bookrepo.get_all_undeleted()
    format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20}"
    format_linije1 = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20} {:8}"

    i = 7
    while i != 0:
        print('1 --- pretraga po sifri.')
        print('2 --- pretraga po naslovu.')
        print('3 --- pretraga po autoru.')
        print('4 --- pretraga po kategoriji.')
        print('5 --- pretraga po izdavacu.')
        print('6 --- pretraga po opsegu cene.')
        print('0 --- povratak na prethodni meni.')
        i = int(input())
        if i == 1:
            sifra = input('Unesite sifru za pretragu. \n')
            # searched = [x for x in books if containsCode(x.code, sifra)]

            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if containsCode(book.code, sifra) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))

                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if containsCode(book.code, sifra) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()
            print()
        elif i == 2:
            naziv = input('Unesite naziv za pretragu. \n')
            # searched = [x for x in books if containsName(x.name, naziv)]

            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if containsName(book.name, naziv) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))

                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if containsName(book.name, naziv) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()

        elif i == 3:
            autor = input('Unesite ime autora za pretragu. \n')
            # searched = [x for x in books if containsAuthor(x.author, autor)]
            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if containsAuthor(book.author, autor) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if containsAuthor(book.author, autor) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()

        elif i == 4:
            zanr = input('Unesite ime zanra za pretragu. \n')
            # searched = [x for x in books if containsGenre(x.genre, zanr)]

            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if containsGenre(book.genre, zanr) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))

                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if containsGenre(book.genre, zanr) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()

            print()
        elif i == 5:
            izdavac = input('Unesite ime izdavaca za pretragu. \n')
            # searched = [x for x in books if containsPublisher(x.publisher, izdavac)]
            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if containsPublisher(book.publisher, izdavac) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if containsPublisher(book.publisher, izdavac) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()

            print()
        elif i == 6:
            min = int(input('Unesite minimalnu cenu za pretragu. \n'))
            max = int(input('Unesite maksimalnu cenu za pretragu. \n'))
            # searched = [x for x in books if isinpricerange(min, max, x.price)]
            if usertype == "administrator":
                searched = []
                for book in bookrepo.books:
                    if isinpricerange(min, max, book.price) == True:
                        searched.append(book)
                print(format_linije1.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                            "Zanr", "Brisano"))
                print(
                    format_linije1.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                          "-" * 10,
                                          "-" * 20, "-" * 8))
                for book in searched:
                    book.print()
            else:
                searched = []
                for book in books:
                    if isinpricerange(min, max, book.price) == True:
                        searched.append(book)
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))

                for book in searched:
                    book.print()

            print()
        else:
            return None


def pretragaAkcija():
    specialOfferRepo = SpecialOfferRepository()
    offers = specialOfferRepo.get_all_undeleted()
    bookRepo = BookRepository()

    format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20}"
    i = 7
    while i != 0:
        print('1 --- pretraga po sifri.')
        print('2 --- pretraga po naslovu knjige.')
        print('3 --- pretraga po autoru knjige.')
        print('4 --- pretraga po kategoriji knjige.')
        print('0 --- povratak na prethodni meni.')
        i = int(input())

        if i == 1:
            sifra = input('Unesite sifru za pretragu. \n')
            for offer in offers:
                searched = [x for x in offer.books_and_prices.keys() if containsCode(x, sifra)]

                if len(searched) > 0:
                    print("Code: ", offer.code)
                    print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                    print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                               "Akc. Cena", "Zanr"))
                    print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                               "-" * 10,
                                               "-" * 20))

                    for key in searched:
                        book = bookRepo.get_undeleted(key)
                        print(format_linije.format(key, book.name, book.isbn, book.author, book.publisher,
                                                   book.page_number,
                                                   book.year, offer.books_and_prices[key], book.genre))

                    print("-" * 120)
                    print()
                    print()


        elif i == 2:
            naslov = input('Unesite naslov za pretragu. \n')
            for offer in offers:
                searched = [x for x in offer.books_and_prices.keys() if
                            containsName(bookRepo.get_undeleted(x).name, naslov)]
                if len(searched) > 0:
                    print("Code: ", offer.code)
                    print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                    print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                               "Akc. Cena", "Zanr"))
                    print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                               "-" * 10,
                                               "-" * 20))

                    for key in searched:
                        book = bookRepo.get_undeleted(key)
                        print(format_linije.format(key, book.name, book.isbn, book.author, book.publisher,
                                                   book.page_number,
                                                   book.year, offer.books_and_prices[key], book.genre))

                    print("-" * 120)
                    print()
                    print()

        elif i == 3:
            autor = input('Unesite autora za pretragu. \n')
            for offer in offers:
                searched = [x for x in offer.books_and_prices.keys() if
                            containsAuthor(bookRepo.get_undeleted(x).author, autor)]
                if len(searched) > 0:
                    print("Code: ", offer.code)
                    print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                    print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                               "Akc. Cena", "Zanr"))
                    print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                               "-" * 10,
                                               "-" * 20))

                    for code in searched:
                        book = bookRepo.get_undeleted(code)
                        print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher,
                                                   book.page_number,
                                                   book.year, offer.books_and_prices[code], book.genre))

                    print("-" * 120)
                    print()
                    print()

        elif i == 4:
            kategorija = input('Unesite kategoriju za pretragu. \n')
            for offer in offers:
                searched = [x for x in offer.books_and_prices.keys() if
                            containsGenre(bookRepo.get_undeleted(x).genre, kategorija)]
                if len(searched) > 0:
                    print("Code: ", offer.code)
                    print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                    print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                               "Akc. Cena", "Zanr"))
                    print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                               "-" * 10,
                                               "-" * 20))

                    for code in searched:
                        book = bookRepo.get_undeleted(code)
                        print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher,
                                                   book.page_number,
                                                   book.year, offer.books_and_prices[code], book.genre))

                    print("-" * 120)
                    print()
                    print()

        else:
            return None


def prikaziAkcije():
    specialOfferRepo = SpecialOfferRepository()
    offers = specialOfferRepo.get_all_undeleted()
    bookRepo = BookRepository()

    format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20}"

    for offer in offers:
        print("Kod: ", offer.code)
        print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
        print(
            format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Akc. Cena", "Zanr"))
        print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                   "-" * 20))

        for code in offer.books_and_prices.keys():
            book = bookRepo.get_undeleted(code)
            print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher, book.page_number,
                                       book.year, offer.books_and_prices[code], book.genre))

        print("-" * 120)
        print()
        print()

    i = 666
    while i != 0:
        print('Odaberite kriterijum sortiranja.')
        print('1 --- po sifri.')
        print('2 --- po datumu.')
        print('0 --- povratak na prethodni meni.')
        i = int(input())
        specialOfferRepo = SpecialOfferRepository()
        offers = specialOfferRepo.get_all_undeleted()
        bookRepo = BookRepository()

        if i == 1:
            print('Odaberite rastuce/opadajuce.')
            print('1 --- rastuce.')
            print('bilo sta --- opadajuce.')
            l = int(input())
            if l == 1:
                offers.sort(key=lambda x: x.code, reverse=False)

            else:
                offers.sort(key=lambda x: x.code, reverse=True)

            for offer in offers:
                print("Code: ", offer.code)

                print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Akc. Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))
                print()

                for code in offer.books_and_prices.keys():
                    book = bookRepo.get_undeleted(code)
                    print(
                        format_linije.format(code, book.name, book.isbn, book.author, book.publisher, book.page_number,
                                             book.year, offer.books_and_prices[code], book.genre))

                print("-" * 120)


        elif i == 2:

            print('Odaberite rastuce/opadajuce.')
            print('1 --- rastuce.')
            print('bilo sta --- opadajuce.')
            l = int(input())
            if l == 1:
                offers.sort(key=lambda x: x.datetime, reverse=False)

            else:
                offers.sort(key=lambda x: x.datetime, reverse=True)

            for offer in offers:
                print("Code: ", offer.code)

                print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Akc. Cena",
                                           "Zanr"))
                print(
                    format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10, "-" * 10,
                                         "-" * 20))
                print()

                for code in offer.books_and_prices.keys():
                    book = bookRepo.get_undeleted(code)
                    print(
                        format_linije.format(code, book.name, book.isbn, book.author, book.publisher, book.page_number,
                                             book.year, offer.books_and_prices[code], book.genre))

                print("-" * 120)
    else:
        return None


def registracija():
    ime = input('Unesite ime: ')
    prezime = input('Unesite prezime: ')
    username = ''
    kontrolna = 1
    userRepo = UserRepository()
    while kontrolna == 1:

        username = input('Unesite username: ')
        user = userRepo.get_undeleted(username)

        if user is None:
            kontrolna = 0
        else:
            print('Ovaj username vec postoji, molim Vas ponovite unos.')

    password = input('Unesti lozinku: ')
    type = ''
    i = 0
    while i == 0:
        usertype = input('Odaberite tip korisnika \n 1. Prodavac \n 2. Menadzer \n')
        if usertype == '1':
            type = 'salesman'
            i = 1
        elif usertype == '2':
            type = 'manager'
            i = 1
        else:
            print('Molim vas ponovite unos.')

    newUser = User(username, password, ime, prezime, type, False)
    if userRepo.add(newUser) == True:
        print('Uspesno ste dodali korisnika.')


def prikazsvihkorisnika():
    userrepo = UserRepository()
    format_linije = "{:20} {:20} {:20} {:20}"
    print(format_linije.format("Ime", "Prezime", "Username", "Tip korisnika"))
    print(format_linije.format("-" * 20, "-" * 20, "-" * 20, "-" * 20))
    n = 1
    while n == 1:
        print('Odaberite kriterijum sortiranja.')
        print('1 --- po imenu.')
        print('2 --- po prezimenu.')
        print('3 --- po username-u.')
        print('4 --- po tipu korisnika.')
        print('0 --- za povratak nazad')
        i = int(input())
        users = userrepo.get_all_undeleted()
        if i == 1:

            print(format_linije.format("Ime", "Prezime", "Username", "Tip korisnika"))
            print(format_linije.format("-" * 20, "-" * 20, "-" * 20, "-" * 20))

            users.sort(key=lambda x: x.first_name, reverse=False)

            for user in users:
                user.print()
            print()

        elif i == 2:

            print(format_linije.format("Ime", "Prezime", "Username", "Tip korisnika"))
            print(format_linije.format("-" * 20, "-" * 20, "-" * 20, "-" * 20))

            users.sort(key=lambda x: x.last_name, reverse=False)

            for user in users:
                user.print()
            print()

        elif i == 3:

            print(format_linije.format("Ime", "Prezime", "Username", "Tip korisnika"))
            print(format_linije.format("-" * 20, "-" * 20, "-" * 20, "-" * 20))

            users.sort(key=lambda x: x.username, reverse=False)

            for user in users:
                user.print()
            print()

        elif i == 4:

            print(format_linije.format("Ime", "Prezime", "Username", "Tip korisnika"))
            print(format_linije.format("-" * 20, "-" * 20, "-" * 20, "-" * 20))

            users.sort(key=lambda x: x.user_type, reverse=False)

            for user in users:
                user.print()
            print()

        elif i == 0:

            return None


def dodavanjeknjige():
    ime = input('Unesite ime: ')
    isbn = input('Unesite isbn: ')
    autor = input('Unesite ime autora: ')
    izdavac = input('Unesite ime izdavacke kuce: ')
    broj_stranica = int(input('Unesite broj stranica: '))
    godina_izdavanje = int(input('Unesite godinu izdavanja: '))
    cena = int(input('Unesite cenu knjige: '))
    zanr = input('Unesite zanr knjige: ')
    code = ''

    kontrolna = 1
    bookRepo = BookRepository()
    while kontrolna == 1:

        code = input('Unesite sifru knjige: ')
        book = bookRepo.get(code)

        if book is None:
            kontrolna = 0
        else:
            print('Ova knjiga vec postoji, molim Vas ponovite unos.')

    knjiga = Book(code, ime, isbn, autor, izdavac, broj_stranica, godina_izdavanje, cena, zanr, False)
    if bookRepo.add(knjiga) == True:
        print('Uspesno ste uneli knjigu.')
    else:
        print('Neuspesno ste uneli knjigu')


def izmenaknjige():
    code = ''
    bookrepo = BookRepository()
    kontrolna = 0
    oldBook = None

    while kontrolna == 0:
        code = input('Unesite sifru knjige. \n')

        oldBook = bookrepo.get(code)
        if oldBook is not None:
            kontrolna = 1

    novoIme = input('Unesite novo ime, ako zelite staro kliknite enter. \n')
    if novoIme == '':
        novoIme = oldBook.name

    noviIsbn = input('Unesite novi isbn, ako zelite stari kliknite enter. \n')
    if noviIsbn == '':
        noviIsbn = oldBook.isbn

    noviAutor = input('Unesite novo ime autora, ako zelite staro kliknite enter. \n')
    if noviAutor == '':
        noviAutor = oldBook.author

    noviIzdavac = input('Unesite novo ime izdavaca, ako zelite staro kliknite enter.\n')
    if noviIzdavac == '':
        noviIzdavac = oldBook.publisher

    noviBr = input('Unesite novi broj stranica, ako zelite stari kliknite enter. \n')
    if noviBr == '':
        noviBr = oldBook.page_number
    else:
        noviBr = int(noviBr)

    novaGod = input('Unesite novu godinu izdanja, ako zelite staru kliknite enter. \n')
    if novaGod == '':
        novaGod = oldBook.year
    else:
        novaGod = int(novaGod)

    novaCena = input('Unesite novu cenu, ako zelite staru kliknite enter. \n')
    if novaCena == '':
        novaCena = oldBook.price
    else:
        novaCena = int(novaCena)

    noviZanr = input('Unesite novi zanr knjige, ako zelite stari kliknite enter. \n')
    if noviZanr == '':
        noviZanr = oldBook.genre

    i = 0
    while i == 0:
        delStatus = input('Odaberite status knjige \n 1. Obrisana \n 2. Postojeca \n')
        if delStatus == '1':
            oldBook.deleted = True
            i = 1
        elif delStatus == '2':
            oldBook.deleted = False
            i = 1
        else:
            print('Molim vas ponovite unos.')

    novaKnjiga = Book(code, novoIme, noviIsbn, noviAutor, noviIzdavac, noviBr, novaGod, novaCena, noviZanr,
                      oldBook.deleted)

    if bookrepo.update(novaKnjiga) == True:
        print('Uspesno ste update-ovali knjigu.')
    else:
        print('Neuspesno ste update-ovali knjigu.')

def brisanjeknjige():
    code = ''
    bookrepo = BookRepository()
    kontrolna = 0
    oldBook = None

    while kontrolna == 0:
        code = input('Unesite sifru knjige. \n')

        oldBook = bookrepo.get(code)
        if oldBook is not None:
            kontrolna = 1

    delStatus = input('Ako zelite da obrisete knjigu, kliknite enter. \n Ako ne zelite da obrisete knjigu, pritisnite bilo koji karakter na tastaturi. \n')
    if delStatus == '':
        oldBook.deleted = True

    novaKnjiga = Book(code, oldBook.name, oldBook.isbn, oldBook.author, oldBook.publisher, oldBook.page_number, oldBook.year, oldBook.price, oldBook.genre,
                      oldBook.deleted)

    if bookrepo.update(novaKnjiga) == True:
        print('Uspesno ste obrisali knjigu.')
    else:
        print('Neuspesno ste obrisali knjigu.')


def showMenuForAdmin(usertype):
    kontrolna = 42
    while kontrolna != 0:
        print("Odaberite opciju: ")
        print("1 --- prikaz svih knjiga.")
        print("2 --- pretraga knjiga.")
        print("3 --- prikaz svih akcija.")
        print("4 --- pretraga akcija.")
        print("5 --- registacija korisnika.")
        print("6 --- prikaz svih korisnika.")
        print("7 --- dodavanje knjige.")
        print("8 --- izmena knjige.")
        print("9 --- brisanje knjige.")
        print("0 --- izlaz.")

        kontrolna = int(input())
        if kontrolna == 1:
            prikazsvihknjiga(usertype)
        elif kontrolna == 2:
            svepretrageKnjiga(usertype)
        elif kontrolna == 3:
            prikaziAkcije()
        elif kontrolna == 4:
            pretragaAkcija()
        elif kontrolna == 5:
            registracija()
        elif kontrolna == 6:
            prikazsvihkorisnika()
        elif kontrolna == 7:
            dodavanjeknjige()
        elif kontrolna == 8:
            izmenaknjige()
        elif kontrolna == 9:
            brisanjeknjige()
        elif kontrolna == 0:
            continue


def showMenuForManager(usertype):
    kontrolna = 42
    while kontrolna != 0:
        print("Odaberite opciju: ")
        print("1 --- prikaz svih knjiga.")
        print("2 --- pretraga knjiga.")
        print("3 --- prikaz svih akcija.")
        print("4 --- pretraga akcija.")
        print("5 --- registacija korisnika.")
        print("6 --- prikaz svih korisnika.")
        print("0 --- izlaz.")

        kontrolna = int(input())
        if kontrolna == 1:
            prikazsvihknjiga(usertype)
        elif kontrolna == 2:
            svepretrageKnjiga(usertype)
        elif kontrolna == 3:
            prikaziAkcije()
        elif kontrolna == 4:
            pretragaAkcija()
        elif kontrolna == 5:
            registracija()
        elif kontrolna == 6:
            prikazsvihkorisnika()
        elif kontrolna == 0:
            continue
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def prodajaknjiga(cashier):
    books = {}
    s_offer_books = {}

    specialOfferRepo = SpecialOfferRepository()
    offers = specialOfferRepo.get_all_undeleted()
    bookRepo = BookRepository()
    receiptRepo = RecieptRepository()

    kontrolna = 1312
    while kontrolna != 0:
        print('Ako zelite da dodate knjigu u korpu upisivanjem njene sifre, zajedno sa kolicinom zeljene knjige, pritisnite broj 1.')
        print('Ako zelite da odabere akciju, pritisnite broj 2.')
        print('Ukoliko zelite da vidite trenutnu korpu, kliknite broj 3')
        print('Ukoliko zelite da potvrdite kupovinu, kliknite broj 4')
        print('Ako zelite da otkazete kupovinu, pritisnite broj 0.')
        kontrolna = int(input())

        if kontrolna == 1:
            i =  7
            while i != 0:
                print('Unesite sifru knjige i kolicinu zeljenu odvojeno zarezom.')
                print('Ukoliko je zadovoljena kolicina knjiga, pritisnite broj 0')
                code_book = input()
                if code_book == '0':
                    i = 0
                else:
                    strings = code_book.split(',')
                    code = strings[0].strip()
                    number = int(strings[1].strip())
                    if books.get(code) is None:
                        books[code] = [number, bookRepo.get_undeleted(code).price]
                    else:
                        oldnumber = books.get(code)
                        newnumber = oldnumber[0] + number
                        if bookRepo.get_undeleted(code) is not None:
                            books[code] = [newnumber, bookRepo.get_undeleted(code).price]
                        else:
                            print('Uneli ste sifru nepostojece knjige.')
        elif kontrolna == 2:
            i = 1

            format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:20}"

            for offer in offers:
                print("Kod: ", offer.code)
                print("Akcija vazi do:", offer.datetime.strftime("%d/%m/%Y"))
                print(
                    format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                         "Akc. Cena", "Zanr"))
                print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                           "-" * 10,
                                           "-" * 20))

                for code in offer.books_and_prices.keys():
                    book = bookRepo.get_undeleted(code)
                    print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher,
                                               book.page_number,
                                               book.year, offer.books_and_prices[code], book.genre))

                print("-" * 120)
                print()
                print()




            while i != 0:
                print('Unesite sifru akcije.')
                print('Ukoliko zelite da izadjete pritisnite broj 0.')
                s_offer = input()
                if s_offer == '0':
                    i = 0
                else:
                    if specialOfferRepo.get_undeleted(s_offer) is not None:
                        offer = specialOfferRepo.get_undeleted(s_offer)
                        for code in offer.books_and_prices.keys():
                            if s_offer_books.get(code) is None:
                                s_offer_books[code] = [1, offer.books_and_prices[code]]
                            else:
                                oldnumber = s_offer_books.get(code)
                                newnumber = oldnumber[0] + 1
                                s_offer_books[code] = [newnumber, offer.books_and_prices[code]]


                    else:
                        print('Uneli ste sifru nepostojece akcije.')
        elif kontrolna==3:
            format_linije = "{:10} {:20} {:10} {:20} {:20} {:10} {:10} {:10} {:10} {:20}"
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd",
                                       "Cena", "Kolicina", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 20, "-" * 10, "-" * 10,
                                       "-" * 10,
                                       "-" * 10,
                                       "-" * 20))
            if len(s_offer_books)!=0:
                for code in s_offer_books.keys():
                    book = bookRepo.get_undeleted(code)
                    print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher,
                                               book.page_number,
                                               book.year,s_offer_books[code][1], s_offer_books[code][0], book.genre))

            if len(books):
                for code in books.keys():
                    book = bookRepo.get_undeleted(code)
                    print(format_linije.format(code, book.name, book.isbn, book.author, book.publisher,
                                               book.page_number,
                                               book.year, books[code][1], books[code][0], book.genre))

            now= datetime.datetime.today().strftime("%d/%m/%Y")
            r = Receipt(get_random_string(5), cashier, str(now)
                            , books, s_offer_books, False)

            print('Ukupna cena je: ' +str(r.full_price))

        elif kontrolna==4:
            now = datetime.datetime.today().strftime("%d/%m/%Y")
            r = Receipt(get_random_string(5), cashier, str(now), books, s_offer_books, False)
            print(str(r))
            if receiptRepo.add(r):
                print('Uspesno ste prodali knjige')
                return
        else:
            kontrolna = 0











def showMenuForSalesman(usertype,cashier):
    kontrolna = 42
    while kontrolna != 0:
        print("Odaberite opciju: ")
        print("1 --- prikaz svih knjiga.")
        print("2 --- pretraga knjiga.")
        print("3 --- prikaz svih akcija.")
        print("4 --- pretraga akcija.")
        print("5 --- dodavanje knjige.")
        print("6 --- izmena knjige.")
        print("7 --- brisanje knjige.")
        print("8 --- prodaja knjiga.")
        print("0 --- izlaz.")

        kontrolna = int(input())
        if kontrolna == 1:
            prikazsvihknjiga(usertype)
        elif kontrolna == 2:
            svepretrageKnjiga(usertype)
        elif kontrolna == 3:
            prikaziAkcije()
        elif kontrolna == 4:
            pretragaAkcija()
        elif kontrolna == 5:
            dodavanjeknjige()
        elif kontrolna == 6:
            izmenaknjige()
        elif kontrolna == 7:
            brisanjeknjige()
        elif kontrolna == 8:
            prodajaknjiga(cashier)
        elif kontrolna == 0:
            continue


def test():
    user = login()
    if user is None:
        return
    else:
        if user.user_type == "administrator":
            showMenuForAdmin(user.user_type)
        elif user.user_type == "manager":
            showMenuForManager(user.user_type)
        else:
            if user.user_type == "salesman":
                showMenuForSalesman(user.user_type, user.username)


def seedUsers():
    u1 = User('laganina', 'vandrful', 'severna', 'juznic', 'administrator', False)
    u2 = User('devedesete', 'samojako', 'Cetnik', 'Mirko', 'manager', True)
    u3 = User('ribojzla', 'majas1a', 'Rajko', 'Cardakovic', 'manager', False)
    u4 = User('mehveh', 'sv3j3zavj3ra', 'Milojka', 'Ruzinovic', 'salesman', False)

    userrepo = UserRepository()
    userrepo.add(u1)
    userrepo.add(u2)
    userrepo.add(u3)
    userrepo.add(u4)


def seedBooks():
    b1 = Book('code1', 'Saptac', '109035', 'Donato Karizi', 'Vulkan', 358, 2017, 799, 'novel', False)
    b2 = Book('code2', 'Valis', '128754', 'Filip Dik', 'Laguna', 254, 2017, 599, 'novel', False)
    b3 = Book('code3', 'Hipnotizer', '036739', 'Las Kepler', 'Vulkan', 270, 2011, 999, 'novel', False)
    b4 = Book('code4', 'Maternji jezik', '021888', 'Nenad Grujicic', 'Prosveta', 136, 2018, 499, 'poetry', True)
    b5 = Book('code5', 'Biblija', '424666', 'Isus Hrist', 'Crkva', 1200, 1, 1500, 'sci-fi', False)
    b6 = Book('code6', 'Alijenista', '197000', 'Kejleb Kar', 'Grafeks', 191, 2004, 500, 'adventure', False)
    b7 = Book('code7', 'Iluminati 666', '110459', 'Milan Vidojevic', 'Mali Princ', 199, 2015, 400, 'sci-fi', False)
    b8 = Book('code8', 'Sapijens', '131662', 'Juval N. Harari', 'Laguna', 430, 2019, 1299, 'scientific literature',
              True)
    b9 = Book('code9', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel', True)
    b10 = Book('code10', 'Cvece zla', '591138', 'Sarl Bodler', 'Alnari', 162, 2002, 399, 'poetry', True)

    bookrepo = BookRepository()
    bookrepo.add(b1)
    bookrepo.add(b2)
    bookrepo.add(b3)
    bookrepo.add(b4)
    bookrepo.add(b5)
    bookrepo.add(b6)
    bookrepo.add(b7)
    bookrepo.add(b8)
    bookrepo.add(b9)
    bookrepo.add(b10)


def seedOffers():
    b1 = Book('code1', 'Saptac', '109035', 'Donato Karizi', 'Vulkan', 358, 2017, 799, 'novel', False)
    b2 = Book('code2', 'Valis', '128754', 'Filip Dik', 'Laguna', 254, 2017, 599, 'novel', False)
    b3 = Book('code3', 'Hipnotizer', '036739', 'Las Kepler', 'Vulkan', 270, 2011, 999, 'novel', False)
    b4 = Book('code4', 'Maternji jezik', '021888', 'Nenad Grujicic', 'Prosveta', 136, 2018, 499, 'poetry', True)
    b5 = Book('code5', 'Biblija', '424666', 'Isus Hrist', 'Crkva', 1200, 1, 1500, 'sci-fi', False)
    b6 = Book('code6', 'Alijenista', '197000', 'Kejleb Kar', 'Grafeks', 191, 2004, 500, 'adventure', False)
    b7 = Book('code7', 'Iluminati 666', '110459', 'Milan Vidojevic', 'Mali Princ', 199, 2015, 400, 'sci-fi', False)
    b8 = Book('code8', 'Sapijens', '131662', 'Juval N. Harari', 'Laguna', 430, 2019, 1299, 'scientific literature',
              True)
    b9 = Book('code9', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel', True)
    b10 = Book('code10', 'Cvece zla', '591138', 'Sarl Bodler', 'Alnari', 162, 2002, 399, 'poetry', True)

    dict1 = {b1.code: 569, b2.code: 499, b3.code: 800, b5.code: 299}
    dict2 = {b3.code: 569, b5.code: 499, b6.code: 800}

    special_offer1 = SpecialOffer('code2', dict1, datetime.datetime(2021, 7, 18).strftime("%d/%m/%Y"), False)
    special_offer2 = SpecialOffer('code1', dict2, datetime.datetime(2021, 7, 17).strftime("%d/%m/%Y"), False)

    specialOfferRepo = SpecialOfferRepository()

    specialOfferRepo.add(special_offer1)
    specialOfferRepo.add(special_offer2)


if __name__ == "__main__":
    # seedUsers()
    # seedBooks()
    # seedOffers()
    test()
