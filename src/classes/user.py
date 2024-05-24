# Клас для роботи з користувачами
class User:
    def __init__(self, id, name, birthday=None):
        self.id = id
        self.name = name
        self.birthday = birthday  # День народження користувача у форматі DD-MM-YYYY