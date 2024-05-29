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
    def delete_record(self, name: str):
        if name in self.data:
            self.data.pop(name)
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

    def find_by_name(self, name):
        for record in self.data.values():
            if record.name.lower() == name.lower():
                return record
        raise KeyError("ERROR: The item with the specified name does not exist in AddressBook")

    # Пошук контакту за телефономa
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
        current_date = datetime.now().date()
        end_date = current_date + timedelta(days=days)
        birthdays_in_range = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d-%m-%Y").date()
                # Calculate the next birthday date for this year
                next_birthday_date = datetime(current_date.year, birthday_date.month, birthday_date.day).date()
                if current_date <= next_birthday_date <= end_date:
                    birthdays_in_range.append((record.name, next_birthday_date))
                # Check for birthdays in the following year if the range includes January
                elif end_date.month == 1 and birthday_date.month == 12 and current_date.month == 12:
                    next_birthday_date = datetime(current_date.year + 1, birthday_date.month, birthday_date.day).date()
                    if current_date <= next_birthday_date <= end_date:
                        birthdays_in_range.append((record.name, next_birthday_date))

        # Sort birthdays by date
        birthdays_in_range.sort(key=lambda x: x[1])

        # Print the next birthdays
        for name, birthday_date in birthdays_in_range:
            print(f"{name}: {birthday_date.strftime('%d-%m-%Y')}")
