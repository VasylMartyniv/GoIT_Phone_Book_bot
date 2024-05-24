import re

class Email:
    def __init__(self, email):
        if self.validate_email(email):
            self.email = email
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
        return self.email

    def change_email(self, new_email):
        """
        Змінює email-адресу, якщо вона є валідною.
        """
        if self.validate_email(new_email):
            self.email = new_email
        else:
            raise ValueError("Invalid email format")
        
"""
# Приклад використання
try:
    email = Email("example@example.com")
    print(email)  # Виведе: example@example.com

except ValueError as e:
    print(e)

try:
    email.change_email("new_example@example.com")
    print(email)  # Виведе: new_example@example.com
except ValueError as e:
    print(e)
"""