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

    # Виводити список всіх днів народження за наступні N днів.
    def show_next_birthdays(self, number_of_days: int):    # Не перевірено, підозрюю що працює неправильно!!!

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
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("The item with the specified name does not exist in AddressBook")
    
    def find_by_phone(self, phone: str):
        for record in self.data:
            if self.data[record].find_phone(phone):
                return self.data[record]
        raise KeyError("ERROR: The item with the specified phone does not exist in AddressBook")

    def find_by_email(self, email: str):
        for record in self.data:
            if self.data[record].find_email(email):
                return self.data[record]
        raise KeyError("ERROR: The item with the specified email does not exist in AddressBook")


##### Testing:

# book = AddressBook()

# jhon = Record("Jhon")
# jhon.add_phone("0632588820")
# jhon.add_address("UA")
# jhon.add_email("senik.yu@gmail.com")

# emma = Record("Emma")
# emma.add_phone("0632588819")
# emma.add_email("emma@gmail.com")

# eminem = Record("Eminem")
# eminem.add_phone("0631111111")

# book.add_record(jhon)
# book.add_record(emma)

# print(book)

# print(book.find_by_email("s.yu@gmail.com"))