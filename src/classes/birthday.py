import json
from datetime import datetime, timedelta

# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value  # Ініціалізація значення поля

# Клас для зберігання дати народження з валідацією
class Birthday(Field):
    def __init__(self, value):
        try:
            # Перевірка формату дати і перетворення її в об'єкт datetime
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            # Викидання помилки, якщо формат дати некоректний
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        # Перетворення об'єкта дати в строку для виведення
        return self.value.strftime('%d.%m.%Y')

# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ініціалізація імені контакту як об'єкта класу Name
        self.phones = []  # Ініціалізація списку телефонів для контакту
        self.birthday = None  # Ініціалізація поля для дати народження як None

    def add_birthday(self, birthday):
        # Додавання дати народження, перетворюючи строку в об'єкт класу Birthday
        self.birthday = Birthday(birthday)

    def change_birthday(self, new_birthday):
        # Зміна існуючої дати народження на нову, перетворюючи строку в об'єкт класу Birthday
        self.birthday = Birthday(new_birthday)

    def delete_birthday(self):
        # Видалення дати народження, встановлюючи поле 'birthday' як None
        self.birthday = None

    def __str__(self):
        # Перетворення об'єкта Record в строку для виведення
        phones = "; ".join(p.value for p in self.phones)
        birthday = str(self.birthday) if self.birthday else "No birthday"
        return f"Name: {self.name.value}, Phones: {phones}, Birthday: {birthday}"

# Клас для роботи з базою даних користувачів
class UsersDatabase:
    def __init__(self):
        self.users = []  # Список користувачів
        self.next_id = 1  # Наступний ID для нового користувача
        self.load_users()  # Завантаження користувачів з файлу при створенні об'єкта

    def get_user_by_id(self, user_id):
        # Пошук користувача за ID
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def validate_date(self, birthday_str):
        # Функція для перевірки коректності дати народження
        try:
            birthday = datetime.strptime(birthday_str, "%d.%m.%Y")
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
            print("Некоректний формат дати народження. Будь ласка, введіть у форматі 'DD.MM.YYYY'.")
            return False

    def add_birthday(self, user_id, new_birthday):
        # Додавання або оновлення дати народження для користувача
        while not self.validate_date(new_birthday):
            new_birthday = input("Введіть новий день народження у форматі 'DD.MM.YYYY': ")
        for user in self.users:
            if user.id == user_id:
                user.birthday = new_birthday
                self.save_users()
                print("День народження оновлено.")
                return True
        print("Користувача з вказаним ID не знайдено.")
        return False

    def save_users(self):
        # Збереження користувачів у файл
        with open("users.json", "w") as file:
            json_users = [
                {"id": user.id, "name": user.name.value, "birthday": str(user.birthday)}
                for user in self.users
            ]
            json.dump(json_users, file, indent=4)

    def load_users(self):
        # Завантаження користувачів з файлу
        try:
            with open("users.json", "r") as file:
                json_users = json.load(file)
                self.users = [
                    Record(user["name"]) for user in json_users
                ]
                for user, user_data in zip(self.users, json_users):
                    user.id = user_data["id"]
                    if user_data["birthday"]:
                        user.add_birthday(user_data["birthday"])
                self.next_id = (
                    max(self.users, key=lambda user: user.id).id + 1
                    if self.users
                    else 1
                )
        except FileNotFoundError:
            pass

    def delete_birthday(self, user_id):
        # Видалення дати народження користувача
        for user in self.users:
            if user.id == user_id:
                user.birthday = None
                self.save_users()
                print("День народження користувача видалено.")
                return True
        print("Користувача з вказаним ID не знайдено.")
        return False

    def show_birthday(self, user_id):
        # Показ дня народження користувача
        for user in self.users:
            if user.id == user_id:
                if user.birthday:
                    return user
                else:
                    return "День народження не встановлено для цього користувача."
        return "Користувача з вказаним ID не знайдено."

    def show_all_birthdays(self):
        # Показ всіх днів народження
        birthdays = []
        for user in self.users:
            if user.birthday:
                birthdays.append(f"ID: {user.id}, Name: {user.name.value}, Birthday: {user.birthday}")
            else:
                birthdays.append(f"ID: {user.id}, Name: {user.name.value}, Birthday: не встановлено")
        return birthdays

    def search_by_date_birthday(self, days):
        # Пошук днів народження в заданому проміжку
        today = datetime.now().date()
        target_date = today + timedelta(days=days)
        matching_users = []
        for user in self.users:
            if user.birthday:
                user_birthday = datetime.strptime(str(user.birthday), "%d.%m.%Y").date()
                user_birthday_this_year = user_birthday.replace(year=today.year)
                if today <= user_birthday_this_year <= target_date:
                    matching_users.append(user)
        return matching_users

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Не достатньо аргументів. Будь ласка, дотримуйтесь формату команди."
        except ValueError:
            return "Некоректні дані. Переконайтеся, що ви вводите правильні типи даних."
        except KeyError:
            return "Контакт не знайдено."
    return inner

# Функція для додавання дня народження до контакту
@input_error
def add_birthday(args, db):
    if len(args) != 2:
        raise IndexError("Please provide a name and a birthday in the format DD.MM.YYYY.")
    name, birthday = args
    user = db.get_user_by_name(name)
    if user:
        return db.add_birthday(user.id, birthday)
    else:
        raise KeyError(f"Contact '{name}' not found.")

# Функція для показу дня народження контакту
@input_error
def show_birthday(args, db):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    user = db.get_user_by_name(name)
    if user:
        return db.show_birthday(user.id)
    else:
        raise KeyError(f"Contact '{name}' not found.")

# Функція для показу всіх контактів з днями народження
@input_error
def show_all_birthdays(db):
    return db.show_all_birthdays()

# Функція для пошуку контактів за датою народження
@input_error
def search_by_date_birthday(args, db):
    if len(args) != 1:
        raise IndexError("Please provide a number of days.")
    days = int(args[0])
    return db.search_by_date_birthday(days)

# Функція для зміни дня народження контакту
@input_error
def change_birthday(args, db):
    if len(args) != 2:
        raise IndexError("Please provide a name and a new birthday in the format DD.MM.YYYY.")
    name, new_birthday = args
    user = db.get_user_by_name(name)
    if user:
        return db.add_birthday(user.id, new_birthday)
    else:
        raise KeyError(f"Contact '{name}' not found.")

# Функція для видалення дня народження контакту
@input_error
def delete_birthday(args, db):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    user = db.get_user_by_name(name)
    if user:
        return db.delete_birthday(user.id)
    else:
        raise KeyError(f"Contact '{name}' not found.")
