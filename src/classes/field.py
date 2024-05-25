class Field:
    def __init__(self, value, name, id, birthday=None):
        self.value = value
        self.name = name
        self.id = int(id)
        self.birthday = birthday  # День народження користувача у форматі DD-MM-YYYY

    def __str__(self):
        return str(self.value)
