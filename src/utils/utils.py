from tabulate import tabulate

from src.constants.commands import commands

from src.classes.birthday import add_birthday, show_birthday, show_all_birthdays, search_by_date_birthday

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


def add_birthday():
    name = input("Enter name: ")
    birthday = input("Enter birthday (DD.MM.YYYY): ")
    print(add_birthday([name, birthday], book))

def show_birthday():
    name = input("Enter name: ")
    print(show_birthday([name], book))

def show_all_birthdays():
    print(show_all_birthdays(book))

def search_by_date_birthday():
    date = input("Enter date (DD.MM.YYYY): ")
    print(search_by_date_birthday([date], book))


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
