from datetime import datetime

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
