from collections import UserDict
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

    # Пошук контакту за іменем
    def find_by_name(self, name: str):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("The item with the specified name does not exist in AddressBook")
    
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

