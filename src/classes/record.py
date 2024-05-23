class Record:
    def __init__(self, name):
        self.name = Name(name)  # Ініціалізуємо поле 'name' як об'єкт класу Name
        self.phones = []  # Ініціалізуємо список телефонів для контакту
        self.birthday = None  # Ініціалізуємо поле 'birthday' як None (відсутнє значення дати народження)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)  # Додаємо (встановлюємо) день народження, перетворюючи в об'єкт класу Birthday

    def change_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)  # Змінюємо існуючу дату народження на нову, перетворюючи в об'єкт класу Birthday

    def delete_birthday(self):
        self.birthday = None  # Видаляємо дату народження, встановлюючи поле 'birthday' як None
