from Model.Book import Book
from Model.User import User
from Repository.BookRepository import BookRepository
from Repository.UserRepository import UserRepository

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

        user = userrepo.get(username)
        if user is None:
            print('Neuspesno ste se ulovogali. Pokusajte opet. \n')
            i += 1
            continue
        else:
            if password != user.password:
                print('Neuspesno ste se ulogovali. Pokusajte opet. \n')
                i += 1
                continue
            else :
                print("Uspesno ste se ulogovali.")
                return user

def prikazsvihknjiga():
    bookrepo = BookRepository()
    format_linije = "{:10} {:20} {:10} {:20} {:10} {:10} {:10} {:10} {:20}"
    print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
    print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10, "-" * 20))
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
        if i == 1:

            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            books.sort(key=lambda x: x.name, reverse=False)
            for book in books:
                book.print()
            print()

        elif i == 2:

            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            books.sort(key=lambda x: x.genre, reverse=False)
            for book in books:
                book.print()
            print()

        elif i == 3:

            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            books.sort(key=lambda x: x.author, reverse=False)
            for book in books:
                book.print()
            print()

        elif i == 4:

            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            books.sort(key=lambda x: x.publisher, reverse=False)
            for book in books:
                book.print()
            print()

        elif i == 5:

            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            books.sort(key=lambda x: x.price, reverse=False)
            for book in books:
                book.print()
            print()

        else:
            return None

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


def svepretrage():
    bookerepo = BookRepository()
    books = bookerepo.get_all_undeleted()
    format_linije = "{:10} {:20} {:10} {:20} {:10} {:10} {:10} {:10} {:20}"
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
            searched = [x for x in books if containsCode(x.code, sifra)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        elif i == 2:
            naziv = input('Unesite naziv za pretragu. \n')
            searched = [x for x in books if containsName(x.name, naziv)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        elif i == 3:
            autor = input('Unesite ime autora za pretragu. \n')
            searched = [x for x in books if containsAuthor(x.author, autor)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        elif i == 4:
            zanr = input('Unesite ime zanra za pretragu. \n')
            searched = [x for x in books if containsGenre(x.genre, zanr)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        elif i == 5:
            izdavac = input('Unesite ime izdavaca za pretragu. \n')
            searched = [x for x in books if containsPublisher(x.publisher, izdavac)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        elif i == 6:
            min = int(input('Unesite minimalnu cenu za pretragu. \n'))
            max = int(input('Unesite maksimalnu cenu za pretragu. \n'))
            searched = [x for x in books if isinpricerange(min, max, x.price)]
            print(format_linije.format("Kod", "Naziv", "Isbn", "Autor", "Izdavac", "Br str", "God izd", "Cena", "Zanr"))
            print(format_linije.format("-" * 10, "-" * 20, "-" * 10, "-" * 20, "-" * 10, "-" * 10, "-" * 10, "-" * 10,
                                       "-" * 20))
            for book in searched:
                book.print()
            print()
        else:
            return None


def showMenuForAdmin():
    kontrolna = 42
    while kontrolna != 0 :
        print("Odaberite opciju: ")
        print("1 --- prikaz svih knjiga.")
        print("2 --- pretraga knjiga.")
        print("0 --- izlaz.")
        kontrolna = int(input())
        if kontrolna == 1:
            prikazsvihknjiga()
        elif kontrolna == 2:
            svepretrage()
        elif kontrolna == 0:
            continue


def test():
    user = login()
    if user is None:
        return
    else:
        if user.user_type == "administrator":
            showMenuForAdmin()
        elif user.user_type == "manager":
            print('Ja sam Menadzer')
        else:
            if user.user_type == "salesman":
                print('Ja sam prodavac')

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


    b1 = Book('code1','Saptac','109035','Donato Karizi','Vulkan',358,2017,799,'novel',False)
    b2 = Book('code2','Valis','128754','Filip Dik','Laguna',254,2017,599,'novel',False)
    b3 = Book('code3','Hipnotizer','036739','Las Kepler','Vulkan',270,2011,999,'novel',False)
    b4 = Book('code4','Maternji jezik','021888','Nenad Grujicic','Prosveta',136,2018,499,'poetry',True)
    b5 = Book('code5','Biblija','424666','Isus Hrist','Crkva',1200,1,1500,'sci-fi',False)
    b6 = Book('code6', 'Alijenista','197000','Kejleb Kar','Grafeks',191,2004,500,'adventure',False)
    b7 = Book('code7','Iluminati 666','110459','Milan Vidojevic','Mali Princ',199,2015,400,'sci-fi',False)
    b8 = Book('code8','Sapijens','131662','Juval N. Harari','Laguna',430,2019,1299,'scientific literature',True)
    b9 = Book('code9','Lovac u zitu','123456','J.D. Selindzer','Laguna',253, 2017, 899,'novel',True)
    b10 = Book('code10','Cvece zla','591138','Sarl Bodler','Alnari',162,2002,399,'poetry',True)

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

if __name__=="__main__":
    #seedBooks()

    test()
