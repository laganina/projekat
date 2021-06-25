import json


class User:
    def __init__(self, username, password, first_name, last_name, user_type, deleted):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.user_type = user_type
        self.deleted = deleted

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=0)

    def __str__(self):
        return "\n".join([
            "",
            "{:>10}: {}".format("Korisnicko ime", self.username),
            "{:>15}: {}".format("Lozinka", self.password),
            "{:>10}: {}".format("Ime", self.first_name),
            "{:>15}: {}".format("Prezime", self.last_name),
            "{:>10}: {}".format("Tip korisnika", self.user_type),
            "{:>15}: {}".format("Da li je korisnik obrisan: ", self.deleted)
        ])

    def print(self):
        format_linije = "{:20} {:20} {:20} {:20}"
        print()
        print(format_linije.format(self.first_name, self.last_name, self.username, self.user_type))