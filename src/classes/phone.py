import re

class Phone:
    def __init__(self, number):
        """
        Ініціалізує об'єкт Phone з заданим номером телефону та виконує валідацію.
        """
        if self.validate_phone(number):
            self.number = number
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
        return self.number

    def change_number(self, new_number):
        """
        Змінює номер телефону, якщо він є валідним.
        """
        if self.validate_phone(new_number):
            self.number = new_number
        else:
            raise ValueError("Неправильний формат номера телефону, повинен бути '+380...'")
        

# Приклад використання
try:
    phone = Phone("+1234567890")
    print(phone)  # Виведе: +1234567890

except ValueError as e:
    print(e)

try:
    phone.change_number("+0987654321")
    print(phone)  # Виведе: +0987654321

except ValueError as e:
    print(e)
