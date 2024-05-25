import re
from src.classes.field import Field


class Phone(Field):
    def __init__(self, number):
        """
        Ініціалізує об'єкт Phone з заданим номером телефону та виконує валідацію.
        """
        if self.validate_phone(number):
            super().__init__(number)
            self.value = number
        else:
            raise ValueError("Неправильний формат номера телефону, повинен бути '+380...'")

    def validate_phone(self, number):
        """
        Валідує номер телефону.
        """
        pattern = re.compile(r"^\+380\d{9}$")
        return pattern.match(number) is not None

    def __str__(self):
        """
        Повертає номер телефону як строку.
        """
        return self.value

    def change_number(self, new_number):
        """
        Змінює номер телефону, якщо він є валідним.
        """
        if self.validate_phone(new_number):
            self.value = new_number
        else:
            raise ValueError("Неправильний формат номера телефону, повинен бути '+380...'")

