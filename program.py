from Repository.BookRepository import BookRepository
from Model.Book import Book

class Program:

    def main(self):
        bookRepo = BookRepository()
        #user = UserRepository.login()
        #if user.user_type == "Admin":
        print("1. Show books")
        print("2. Search books")

        option = int(input("Choose option: "))

        if option == 1:
            pass #funkcija koja prikazuje knjige

        b = Book('code1', 'Lovac u zitu', '123456', 'J.D. Selindzer', 'Laguna', 253, 2017, 899, 'novel')
        bookRepo.add(b)
program = Program()
program.main()
