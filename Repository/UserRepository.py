import json
import os
from types import SimpleNamespace

from Model.User import User


class UserRepository:
    def __init__(self):
        self.users = []
        self.load()

    def load(self):
        for root, dirs, files in os.walk("."):
            for filename in files:
                if filename == "users.json":
                    with open('data/users.json', 'r') as jsonfile:
                        lista = json.load(jsonfile)
                        for u in lista:
                            user = json.loads(u, object_hook=lambda d: SimpleNamespace(**d))
                            self.users.append(
                                User(user.username, user.password, user.first_name, user.last_name, user.user_type,
                                 user.deleted))

    def get(self, username):
        for user in self.users:
            if user.username == username and user.deleted == False:
                return user
        return None

    def get_all_undeleted(self):
        undeleted_users = []
        for user in self.users:
            if user.deleted == False:
                undeleted_users.append(user)

        return undeleted_users

    def get_undeleted(self, username):
        for user in self.get_all_undeleted():
            if user.username == username:
                return user
        return None

    def add(self, user):

        user_from_repo = self.get(user.username)
        if user_from_repo is None:
            self.users.append(user)
            json_users = []
            for python_user in self.users:
                json_users.append(python_user.to_json())

            lista = json.dumps(json_users)
            with open('data/users.json', "w") as jsonfile:
                for user in lista:
                    jsonfile.write(user)

            return True

        elif user_from_repo.deleted == True:

            for u in self.users:
                if u.username == user.username:
                    u.deleted = False
                    break

            json_users = []
            for python_user in self.users:
                json_users.append(python_user.to_json())

            lista = json.dumps(json_users)
            with open('data/users.json', "w") as jsonfile:
                for user in lista:
                    jsonfile.write(user)
            return True

        else:
            return False

    def remove(self, username):
        user_from_repo = self.get(username)

        if user_from_repo is not None:
            if user_from_repo.deleted == False:
                for u in self.users:
                    if u.username == username:
                        u.deleted = True
                        break

                json_users = []
                for python_user in self.users:
                    json_users.append(python_user.to_json())

                lista = json.dumps(json_users)
                with open('data/users.json', "w") as jsonfile:
                    for user in lista:
                        jsonfile.write(user)

                return True

        return False

    def update(self, updated_user):
        user_from_repo = self.get(updated_user.username)
        if user_from_repo is not None:
            for u in self.users:
                if u.username == updated_user.username:
                    u.password = updated_user.password
                    u.first_name = updated_user.first_name
                    u.last_name = updated_user.last_name
                    u.user_type = updated_user.user_type
                    u.deleted = updated_user.deleted
                    break

            json_users = []
            for python_user in self.users:
                json_users.append(python_user.to_json())

            lista = json.dumps(json_users)
            with open('data/users.json', "w") as jsonfile:
                for user in lista:
                    jsonfile.write(user)

            return True

        return False



#
# for u in userrepo.users:
#     u.print_user()
