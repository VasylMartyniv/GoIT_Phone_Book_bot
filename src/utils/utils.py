import pickle
from datetime import datetime

from tabulate import tabulate

from src.classes.address_book import AddressBook
from src.classes.birthday import Birthday
from src.classes.record import Record
from src.constants.commands import commands


# MISC

def say_hello():
    print("Hello!")


def list_commands():
    print("\nAvailable commands:")
    table = [[cmd, description] for cmd, description in commands.items()]
    print(tabulate(table, headers=["Command", "Description"], tablefmt="grid"))


def save_contacts(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_contacts(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


# CONTACTS

def add_contact(db):
    try:
        contact = Record(input("Enter name of contact: "))
        phone = input("Enter phone number: ")
        contact.add_phone(phone)
        db.add_record(contact)
        print("Contact added!\n")
    except ValueError as e:
        print(str(e))


def search_contact(users_db):
    name = input("Enter the name of the contact to search: ")
    try:
        contact = users_db.find_by_name(name)
        print(contact)
    except KeyError:
        print("Contact not found.")


def change_contact(users_db):
    name = input("Enter the name of the contact to change: ")
    new_name = input("Enter the new name for the contact: ")
    try:
        users_db.change_record_name(name, new_name)
        print("Contact name changed successfully.")
    except ValueError:
        print("Contact not found or new name already exists.")


def delete_contact(users_db):
    name = input("Enter the name of the contact to delete: ")
    try:
        users_db.delete_record(name)
        print("Contact deleted successfully.")
    except ValueError:
        print("Contact not found.")


# PHONE

def add_phone(users_db):
    name = input("Enter the name of the contact to add phone: ")
    phone = input("Enter the phone number: ")
    try:
        contact = users_db.find_by_name(name)
        contact.add_phone(phone)
        print("Phone added successfully.")
    except KeyError:
        print("Contact not found.")
    except ValueError as e:
        print(str(e))


def delete_phone(users_db):
    name = input("Enter the name of the contact to delete phone: ")
    phone = input("Enter the phone number to delete: ")
    try:
        contact = users_db.find_by_name(name)
        contact.remove_phone(phone)
        print("Phone deleted successfully.")
    except KeyError:
        print("Contact or phone not found.")


def change_phone(users_db):
    name = input("Enter the name of the contact to change phone: ")
    old_phone = input("Enter the old phone number: ")
    new_phone = input("Enter the new phone number: ")
    try:
        contact = users_db.find_by_name(name)
        contact.edit_phone(old_phone, new_phone)
        print("Phone changed successfully.")
    except KeyError:
        print("Contact or phone not found.")
    except ValueError as e:
        print(str(e))


def search_by_phone(users_db):
    phone = input("Enter the phone number to search: ")
    try:
        contact = users_db.find_by_phone(phone)
        print(contact)
    except KeyError:
        print("Contact not found.")


# EMAIL

def add_email(users_db):
    name = input("Enter the name of the contact to add email: ")
    email = input("Enter the email: ")
    try:
        contact = users_db.find_by_name(name)
        contact.add_email(email)
        print("Email added successfully.")
    except KeyError:
        print("Contact not found.")


def change_email(users_db):
    name = input("Enter the name of the contact to change email: ")
    old_email = input("Enter the old email: ")
    new_email = input("Enter the new email: ")
    try:
        contact = users_db.find_by_name(name)
        contact.edit_email(old_email, new_email)
        print("Email changed successfully.")
    except KeyError:
        print("Contact or email not found.")


def delete_email(users_db):
    name = input("Enter the name of the contact to delete email: ")
    email = input("Enter the email to delete: ")
    try:
        contact = users_db.find_by_name(name)
        contact.remove_email(email)
        print("Email deleted successfully.")
    except KeyError:
        print("Contact or email not found.")


def search_by_email(users_db):
    email = input("Enter the email to search: ")
    try:
        contact = users_db.find_by_email(email)
        print(contact)
    except KeyError:
        print("Contact not found.")


# BIRTHDAY

def add_birthday(users_db):
    name = input("Enter the name of the contact to add birthday: ")
    birthday = input("Enter the birthday (format DD-MM-YYYY): ")
    try:
        contact = users_db.find_by_name(name)
        contact.birthday = Birthday(birthday)
        print("Birthday added successfully.")
    except KeyError:
        print("Contact not found.")
    except ValueError:
        print("Invalid birthday format. Please use DD-MM-YYYY.")


def delete_birthday(users_db):
    name = input("Enter the name of the contact to delete birthday: ")
    try:
        contact = users_db.find_by_name(name)
        contact.birthday.delete_birthday()
        print("Birthday deleted successfully.")
    except KeyError:
        print("Contact not found.")


def show_birthday(users_db):
    name = input("Enter the name of the contact to show birthday: ")
    try:
        contact = users_db.find_by_name(name)
        print(f"Birthday: {contact.birthday}")
    except KeyError:
        print("Contact not found.")


def show_all_birthdays(users_db):
    print("Showing all birthdays:")
    users_db.show_all_birthdays()


def search_by_date_birthday(users_db):
    date = input("Enter the date to search (format DD-MM-YYYY): ")
    try:
        datetime.strptime(date, "%d-%m-%Y")  # validate date format
        contacts = [contact for contact in users_db.data.values() if
                    contact.birthday and contact.birthday.value == date]
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("No contacts found with this birthday.")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")


def show_next_birthday(users_db):
    days = int(input("Enter the number of days: "))
    print("Showing next birthdays:")
    users_db.show_next_birthdays(days)


# NOTES

def update_note(db):
    note_id_input = input("Enter note ID to update: ")
    try:
        note_id = int(note_id_input)
        text = input("Enter new text for the note: ")
        tags = input("Enter new tags for the note separated by comma: ").split(",")
        if db.update_note(note_id, text, tags):
            print("Note updated.")
            notes = db.get_all_notes()
            print_notes(notes)
        else:
            print("Note with the given ID not found.")
    except ValueError:
        print(
            f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID."
        )


def add_note(db):
    text = input("Enter note text: ")
    tags = input("Enter tags separated by comma: ").split(",")
    db.add_note(text, tags)
    print("Note added.")
    notes = (
        db.get_all_notes()
    )
    print_notes(notes)


def all_notes(db):
    notes = db.get_all_notes()
    print_notes(notes)


def search_note_by_tags(db):
    search_tags = input("Enter tags to search separated by comma: ").split(",")
    found_notes = db.search_notes_by_tags(search_tags)
    print_notes(found_notes)


def sorting_note_by_tags(db):
    sort_tags = input("Enter tags to sort by separated by comma: ").split(",")
    sorted_notes = db.sort_notes_by_tags(sort_tags)
    print_notes(sorted_notes)


def print_notes(notes):
    if not notes:
        print("No notes to show.")
    else:
        table = [[note.id, ", ".join(note.tags), note.text] for note in notes]
        print(tabulate(table, headers=["ID", "Tags", "Text"], tablefmt="grid"))


def delete_note_by_id(db):
    note_id_input = input("Enter id for removal: ")
    try:
        note_id = int(note_id_input)
        if db.delete_note(note_id):
            print("Note deleted.")
            notes = db.get_all_notes()
            print_notes(notes)
        else:
            print("Note with the given ID not found.")
    except ValueError:
        print(
            f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID."
        )
