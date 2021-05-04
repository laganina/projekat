import json



class Book:
    def __init__(self, code, name, isbn, author, publisher, page_number, year, price, genre, deleted):
        self.code = code
        self.name = name
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.page_number = page_number
        self.year = year
        self.price = price
        self.genre = genre
        self.deleted = deleted

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=0)

    def print_book(self):
        print('[code: '+self.code + ' ,name: '+self.name + ' ,isbn: '+self.isbn + ' ,author: '+self.author + ' ,publisher: '+self.publisher + ' ,page number: '+str(self.page_number) + ' ,year: '+str(self.year) + ' ,price: '+str(self.price) + ' ,genre: '+self.genre + ' ,deleted: '+str(self.deleted)+']')

    def print(self):
        format_linije = "{:10} {:20} {:10} {:20} {:10} {:4} {:11}{:10}       {:20}"

        print()
        print(format_linije.format(self.code, self.name, self.isbn, self.author, self.publisher, self.page_number, self.year, self.price, self.genre))



    def __str__(self):
        return "\n".join([
            "",
            "{:>20}: {}".format("Kod", self.code),
            "{:>20}: {}".format("Naziv", self.name),
            "{:>20}: {}".format("Isbn", self.isbn),
            "{:>20}: {}".format("Autor", self.author),
            "{:>20}: {}".format("Broj stranica", self.page_number),
            "{:>20}: {}".format("Godina izdavanja", self.year),
            "{:>20}: {}".format("Cena", self.price),
            "{:>20}: {}".format("Zanr", self.genre),
        ])

#b = Book('code1', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel')
#print(jsonpickle.encode(b, unpicklable= False))