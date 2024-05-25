from collections import UserDict
from datetime import datetime, timedelta

from src.classes.record import Record


class AddressBook(UserDict):
    # Конструктор класу
    def __init__(self, data: dict = None):
        super().__init__(data)
        if data is None:
            self.data = dict()
        else:
            self.data = data

    # Перетворюватись у стрічку для виведення
    def __str__(self) -> str:
        all_address_book = str()
        if len(self.data) == 0:
            return "AddressBook is empty"
        for record in self.data:
            all_address_book += str(self.data[record])
        return all_address_book + "End of the addressbook"

    # Додавати новий запис у список
    def add_record(self, record: Record):
        if record.name in self.data:
            raise ValueError("ERROR: An element with the specified name already exists in the AddressBook ")
        else:
            self.data[record.name] = record

    # Видаляти запис із списку
    def delete_record(self, record: Record):
        if record.name in self.data:
            self.data.pop(record.name)
        else:
            raise ValueError("ERROR: An element does not exist in the AddressBook ")

    # Змінювати ключ запису (Це зміна імені разом із зміною імені у запису через метод класу Record)
    def change_record_name(self, old_record: Record, new_name: str):
        if old_record.name in self.data:
            if new_name in self.data:
                raise ValueError("ERROR: An element with the specified name already exists in the AddressBook ")
            else:
                self.data[new_name] = self.data[old_record.name]
                self.data[new_name].name = new_name
                del self.data[old_record.name]
        else:
            raise ValueError("ERROR: An element does not exist in the AddressBook ")

    # Пошук контакту за іменем
    def find_by_name(self, name: str):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("ERROR: The item with the specified name does not exist in AddressBook")

    # Пошук контакту за телефоном
    def find_by_phone(self, phone: str):
        for record in self.data:
            if self.data[record].find_phone(phone):
                return self.data[record]
        raise KeyError("ERROR: The item with the specified phone does not exist in AddressBook")

    # Пошук контакту за емейлом
    def find_by_email(self, email: str):
        for record in self.data:
            if self.data[record].find_email(email):
                return self.data[record]
        raise KeyError("ERROR: The item with the specified email does not exist in AddressBook")

    def show_all_birthdays(self):
        for record in self.data:
            print(f"Name: {self.data[record].name}, Birthday: {self.data[record].birthday}")
        return "End of the list"

    def show_next_birthdays(self, days):
        today = datetime.now().date()
        for record in self.data:
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d-%m-%Y").date()
                if today <= birthday_date <= today + timedelta(days=days):
                    print(f"Name: {record.name}, Birthday: {record.birthday.value}")
        return "End of the list"
