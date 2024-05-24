from collections import UserDict
from datetime import datetime, timedelta
from src.classes.record import Record
from src.classes.phone import Phone
from src.classes.email import Email

class AddressBook(UserDict):
    # Перетворюватись у стрічку для виведення
    def __str__(self) -> str: 
        all_address_book = str()
        for record in self.data:
            record_line = f"{record.name.value} {record.phone.value} {record.email.value} {record.birthday.value} \n"
            all_address_book += record_line
        return all_address_book
        

    # Додавати новий запис у список
    def add_record(self, name: str):
        if self.data[name]:
            self.data[name] = Record(name)
        else:
            raise ValueError("ERROR: An element with the specified name already exists in the AddressBook ")
    
    # Видаляти запис із списку
    def delete_record(self, name: str):
        self.data.pop(name)
    
    # Змінювати ключ запису (Це зміна імені разом із зміною імені у запису через метод класу Record)
    def change_record(self, old_name: str, new_name: str):
        self.data[new_name] = self.data[old_name]
        del self.data[old_name]

    # Виводити список всіх днів народження за наступні N днів.
    def show_next_birthdays(self, number_of_days: int):

        def is_day_will_take_place_in_days(day: datetime, days: int):
            first_control_day = datetime.today().date()
            second_control_day = first_control_day + timedelta(days=days)
            return first_control_day <= day <= second_control_day
        
        def this_day_is_weekend(day: datetime):
            return user_birthday.weekday() == 5 or user_birthday.weekday() == 6

        next_celebrations = AddressBook()
        for user in self.data:
            if self.data[user].birthday:
                day = self.data[user].birthday.value.day
                month = self.data[user].birthday.value.month
            user_birthday = datetime(year=datetime.now().year, month=int(month), day=int(day)).date()
            if is_day_will_take_place_in_days(day=user_birthday, days=number_of_days):
                if this_day_is_weekend(user_birthday):
                    delayed_user_birthday = user_birthday + timedelta(days=7 - user_birthday.weekday())
                    next_celebrations.add_record(self.data[user].edit_birthday(delayed_user_birthday))
                else:
                    next_celebrations.add_record(self.data[user])      
        return next_celebrations

    # Пошук контакту
    #   Види пошуку: за номером, за іменем, за поштою.
    #   Вийнятки: контакт не існує, декілька контактів з однаковим іменем (вивід всіх)
    def find_by_name(self, name: str):
        if self.data[name]:
            return self.data[name]
        else:
            raise KeyError("The item with the specified name does not exist in AddressBook")
    
    def find_by_phone(self, number: str):
        for record in self.data:
            if Phone(number) in record.numbers:
                return record
        raise KeyError("ERROR: The item with the specified phone does not exist in AddressBook")

    def find_by_email(self, email: str):
        for record in self.data:
            if Email(email) in record.emails:
                return record
        raise KeyError("ERROR: The item with the specified email does not exist in AddressBook")

    # Суто для тестів!
    def show_all(self):
        for name, record in self.data.items():
            for phone in record.phones:
                print(f"{name}: {phone.value} {record.birthday}")

