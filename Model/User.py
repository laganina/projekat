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


    def print_user(self):
        print(
            '[username: ' + self.username + ' ,password: ' + self.password + ' ,first name: ' + self.first_name + ' ,last name: ' + self.last_name + ' ,user type:' + str(self.user_type) + ' ,deleted:' + str(
                self.deleted)+']')
