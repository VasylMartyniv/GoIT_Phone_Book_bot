from src.classes.address import Address
from src.classes.email import Email
from src.classes.phone import Phone


class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones = list()
        self.emails = list()
        self.address = None
        self.birthday = None

    def __str__(self) -> str:
        name = "Name: " + self.name + "\n"
        # Зібрати телефони
        if self.phones:
            phones = str()
            for phone in self.phones:
                phones += phone.value + " "
            phones = f"Phones: {phones.rstrip()}\n"
        else:
            phones = ""

        # Зібрати емейли
        if self.emails:
            emails = str()
            for email in self.emails:
                emails += email.value + " "
            emails = f"Emails: {emails.rstrip()}\n"
        else:
            emails = ""

        # Зібрати адресу
        if self.address:
            address = "Address: " + self.address.value + "\n"
        else:
            address = ""

        # Зібрати день народження
        if self.birthday.value:
            birthday = "Birthday:" + self.birthday.value + "\n"
        else:
            birthday = ""

        # Зібрати стрічку
        return f"{name}{phones}{emails}{address}{birthday}" + "\n"

    def add_birthday(users_db):
        name = input("Enter the name of the contact to add birthday: ")
        birthday_str = input("Enter the birthday (DD-MM-YYYY): ")
        try:
            record = users_db.get(name)
            if record:
                record.set_birthday(birthday_str)
                print(f"Birthday {birthday_str} added to contact {name}.")
            else:
                print(f"No contact found with the name {name}.")
        except ValueError as e:
            print(e)

    # Tools for working with the field:   phones
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        is_exception = True
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i].change_number(new_phone)
                is_exception = False
        if is_exception:
            raise ValueError("ERROR: There is no such phone")

    def find_phone(self, phone: str):
        for element in self.phones:
            if element.value == phone:
                return phone
        return None

    def remove_phone(self, phone: str):
        is_exception = True
        for element in self.phones:
            if element.value == phone:
                self.phones.remove(element)
                is_exception = False
        if is_exception:
            raise ValueError("ERROR: There is no such phone")

    # Tools for working with the field:   email

    def add_email(self, email: str):
        self.emails.append(Email(email))

    def edit_email(self, old_email: str, new_email: str):
        is_exception = True
        for i in range(len(self.emails)):
            if self.emails[i].value == old_email:
                self.emails[i].change_email(new_email)
                is_exception = False
        if is_exception:
            raise ValueError("ERROR: There is no such email")

    def find_email(self, email: str):
        for element in self.emails:
            if element.value == email:
                return email
        return None

    def remove_email(self, email: str):
        is_exception = True
        for element in self.emails:
            if element.value == email:
                self.emails.remove(element)
                is_exception = False
        if is_exception:
            raise ValueError("ERROR: There is no such email")

    # Tools for working with the field:   address

    def add_address(self, address: str):
        if self.address is None:
            self.address = Address(address)
        else:
            raise ValueError("ERROR: The address is already specified")

    def edit_address(self, new_address: str):
        self.address.change_address(new_address)

    def remove_address(self):
        self.address = None
