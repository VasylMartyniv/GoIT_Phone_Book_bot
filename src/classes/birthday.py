from datetime import datetime, timedelta

from src.classes.data_storage import DataStorage


# Клас для роботи з днем народженнями користувачів
class Birthdaybase:
    def __init__(self):
        self.storage = DataStorage("data.json")

    def get_user_by_id(self, user_id):
        return self.storage.get_user_by_id(user_id)

    # Функція для перевірки коректності дати народження
    def validate_date(self, birthday_str):
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

    # Метод для додавання контакту
    def add_birthday(self, user_id, new_birthday):
        while not self.validate_date(new_birthday):
            new_birthday = input("Введіть новий день народження у форматі 'DD-MM-YYYY': ")
        user = self.storage.get_user_by_id(user_id)
        if user:
            user.birthday = new_birthday
            self.storage.save_users()
            print("День народження оновлено.")
            return True
        print("Користувача з вказаним ID не знайдено.")
        return False

    # Метод для показу дня народження користувача
    def show_birthday(self, user_id):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if user.birthday:
                return user  # Повертаємо об'єкт користувача
            else:
                return "День народження не встановлено для цього користувача."
        return "Користувача з вказаним ID не знайдено."

    # Метод для показу всіх днів народження
    def show_all_birthdays(self):
        birthdays = []
        for user in self.storage.users:
            if user.birthday:
                birthdays.append(
                    f"ID: {user.id}, Name: {user.name}, Birthday: {user.birthday}"
                )
            else:
                birthdays.append(
                    f"ID: {user.id}, Name: {user.name}, Birthday: не встановлено"
                )
        return birthdays

    # Метод для пошуку контактів за датою народження в заданому проміжку
    def search_by_date_birthday(self, days):
        today = datetime.now().date()
        target_date = today + timedelta(days=days)
        matching_users = []

        for user in self.storage.users:
            if user.birthday:
                # Перетворіть рядок з датою народження у об'єкт datetime.date
                user_birthday = datetime.strptime(user.birthday, "%d-%m-%Y").date()
                # Змініть рік дати народження на поточний
                user_birthday_this_year = user_birthday.replace(year=today.year)
                # Перевірте, чи дата народження відповідає заданому проміжку
                if today <= user_birthday_this_year <= target_date:
                    matching_users.append(user)

        return matching_users

    # Метод для видалення дня народження користувача
    def delete_birthday(self, user_id):
        user = self.storage.get_user_by_id(user_id)
        if user:
            user.birthday = None
            self.storage.save_users()
            print("День народження користувача успішно видалено.")
            return True
        else:
            print("Користувача з вказаним ID не знайдено.")
            return False