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

def add_birthday(args, db):
    name = input("Enter name: ")
    birthday = input("Enter birthday (DD.MM.YYYY): ")
    print(add_birthday([name, birthday], db))

def show_birthday(args, db):
    name = input("Enter name: ")
    print(show_birthday([name], db))

def show_all_birthdays(db):
    print(show_all_birthdays(db))

def search_by_date_birthday(args, db):
    date = input("Enter date (DD.MM.YYYY): ")
    print(search_by_date_birthday([date], db))

def print_notes(notes):
    if not notes:
        print("Немає нотаток для виводу.")
    else:
        table = [[note.id, ", ".join(note.tags), note.text] for note in notes]
        print(tabulate(table, headers=["ID", "Tags", "Text"], tablefmt="grid"))

def say_hello():
    print("Hello!")

def print_commands():
    print("\nAvailable commands:")
    table = [[cmd, description] for cmd, description in commands.items()]
    print(tabulate(table, headers=["Command", "Description"], tablefmt="grid"))
