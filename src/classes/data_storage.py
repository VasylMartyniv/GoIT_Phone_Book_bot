import json
from datetime import datetime, timedelta



class User:
    def __init__(self, id, name, phones=None, email=None, birthday=None):
        self.id = int(id)
        self.name = name
        self.phones = phones if phones is not None else []
        self.email = email
        self.birthday = birthday  # День народження користувача у форматі DD-MM-YYYY

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Phones: {self.phones}, Email: {self.email}, Birthday: {self.birthday}"




class DataStorage:
    def __init__(self, filename):
        self.filename = filename
        self.users = []
        self.next_id = 1
        self.load_users()

    def save_users(self):
        with open(self.filename, "w") as file:
            json_users = [
                {"id": user.id, "name": user.name, "phones": user.phones, "email": user.email, "birthday": user.birthday}
                for user in self.users
            ]
            json.dump(json_users, file, indent=4)

    def load_users(self):
        try:
            with open(self.filename, "r") as file:
                json_users = json.load(file)
                self.users = [
                    User(user["id"], user["name"], phones=user.get("phones", []), email=user.get("email"), birthday=user.get("birthday"))
                    for user in json_users
                ]
                self.next_id = (
                    max(self.users, key=lambda user: user.id).id + 1
                    if self.users
                    else 1
                )
        except FileNotFoundError:
            pass

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None