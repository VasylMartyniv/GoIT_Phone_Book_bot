from tabulate import tabulate
from datetime import datetime, timedelta
from src.constants.commands import commands
from src.classes.address_book import AddressBook
from src.classes.record import Record
from src.classes.birthday import Birthday

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # Викликає функцію, що передана декоратору
        except IndexError:
            return "Не достатньо аргументів. Будь ласка, дотримуйтесь формату команди."
        except ValueError:
            return "Некоректні дані. Переконайтеся, що ви вводите правильні типи даних."
        except KeyError:
            return "Контакт не знайдено."
    return inner

# Функції для роботи з контактами
def add_contact():
    print("Feature coming soon")

def add_phone_to_contact():
    print("Feature coming soon")

def change_contact():
    print("Feature coming soon")

def search_by_phone():
    print("Feature coming soon")

def all_contact():
    print("Feature coming soon")

def delete_contact():
    print("Feature coming soon")

# Функції для роботи з днями народження
@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError("Please provide a name and a birthday in the format DD.MM.YYYY.")
    name, birthday = args  # Отримуємо ім'я та дату народження з аргументів
    record = book.find(name)  # Знаходимо контакт у книзі за ім'ям
    if record:
        record.add_birthday(birthday)  # Додаємо день народження до контакту
        return f"Birthday for {name} added as {birthday}."
    else:
        raise KeyError(f"Contact '{name}' not found.")  # Виводимо помилку, якщо контакт не знайдено

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]  # Отримуємо ім'я з аргументів
    record = book.find(name)  # Знаходимо контакт у книзі за ім'ям
    if record:
        if record.birthday:
            return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."
        else:
            return f"{name} does not have a birthday set."
    else:
        raise KeyError(f"Contact '{name}' not found.")  # Виводимо помилку, якщо контакт не знайдено

@input_error
def show_all_birthdays(book: AddressBook):
    birthdays = [str(record) for record in book.values() if record.birthday]  # Отримуємо всі контакти з днями народження
    if not birthdays:
        return "No birthdays available."
    return "\n".join(birthdays)  # Повертаємо список контактів з днями народження

@input_error
def search_by_date_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError("Please provide a date in the format DD.MM.YYYY.")
    date_str = args[0]  # Отримуємо дату з аргументів
    try:
        date = datetime.strptime(date_str, '%d.%m.%Y').date()  # Перетворюємо строку в дату
    except ValueError:
        raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    results = [str(record) for record in book.values() if record.birthday and record.birthday.value == date]  # Знаходимо контакти з відповідною датою народження
    if not results:
        return "No contacts found with this birthday."
    return "\n".join(results)  # Повертаємо список контактів з цією датою народження

# Додаткові функції для роботи з днями народження
@input_error
def change_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise IndexError("Please provide a name and a new birthday in the format DD.MM.YYYY.")
    name, new_birthday = args
    record = book.find(name)
    if record:
        record.change_birthday(new_birthday)
        return f"Birthday for {name} changed to {new_birthday}."
    else:
        raise KeyError(f"Contact '{name}' not found.")

@input_error
def delete_birthday(args, book: AddressBook):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    record = book.find(name)
    if record:
        record.delete_birthday()
        return f"Birthday for {name} deleted."
    else:
        raise KeyError(f"Contact '{name}' not found.")

# Функція для друку нотаток у вигляді таблиці
def print_notes(notes):
    if not notes:
        print("Немає нотаток для виводу.")
    else:
        table = [[note.id, ", ".join(note.tags), note.text] for note in notes]
        print(tabulate(table, headers=["ID", "Tags", "Text"], tablefmt="grid"))

def say_hello():
    print("Hello!")

# Функція для друку команд у вигляді таблиці
def print_commands():
    print("\nAvailable commands:")
    table = [[cmd, description] for cmd, description in commands.items()]
    print(tabulate(table, headers=["Command", "Description"], tablefmt="grid"))
