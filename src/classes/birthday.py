from datetime import datetime, timedelta

from src.classes.field import Field


# Клас для роботи з днем народженнями користувачів
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    # Функція для перевірки коректності дати народження
    @staticmethod
    def validate_date(birthday_str):
        try:
            birthday = datetime.strptime(birthday_str, "%d-%m-%Y")
            today = datetime.now().date()
            # Перевірка, чи дата не є у майбутньому
            if birthday.date() > today:
                print("Дата народження не може бути у майбутньому.")
                return False
            # Перевірка, чи дата не більше за 120 років у минулому
            if today - birthday.date() > timedelta(days=365 * 120):
                print("Дата народження не може бути більше за 120 років у минулому.")
                return False
            return True
        except ValueError:
            print(
                "Некоректний формат дати народження. Будь ласка, введіть у форматі 'DD-MM-YYYY'."
            )
            return False

    # Метод для видалення дня народження користувача
    def delete_birthday(self):
        self.value = None
        print(f"День народження користувача видалено.")
        return

    def __str__(self):
        return self.value
