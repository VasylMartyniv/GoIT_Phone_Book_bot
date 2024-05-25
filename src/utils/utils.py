from tabulate import tabulate

from src.constants.commands import commands


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


def add_birthday(book):
    print("Feature coming soon")


def show_birthday(book):
    print("Feature coming soon")


def show_all_birthdays(book):
    print("Feature coming soon")


def search_by_date_birthday(book):
    print("Feature coming soon")


def change_birthday(book):
    print("Feature coming soon")


def delete_birthday(book):
    print("Feature coming soon")


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
