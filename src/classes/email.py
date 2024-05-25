import re

from src.classes.field import Field


class Email(Field):
    def __init__(self, email):
        if self.validate_email(email):
            super().__init__(email)
        else:
            raise ValueError("Invalid email format")

    def validate_email(self, email):
        """
        Валідує email-адресу.
        """
        pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        return pattern.match(email) is not None

    def __str__(self):
        """
        Повертає email-адресу як строку.
        """
        return self.value

    def change_email(self, new_email):
        """
        Змінює email-адресу, якщо вона є валідною.
        """
        if self.validate_email(new_email):
            self.value = new_email
        else:
            raise ValueError("Invalid email format")
