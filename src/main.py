import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


import readline


from tabulate import tabulate


from src.classes.notes_book import NotesBook
from src.classes.birthday import add_birthday, show_birthday, show_all_birthdays, search_by_date_birthday, change_birthday, delete_birthday
from src.constants.commands import commands
from src.utils.utils import *


# Функція для автодоповнення команд
def completer(text, state):
    options = [cmd for cmd in commands.keys() if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


# Функція для отримання введеної команди з автодоповненням
def get_command_input():
    while True:
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")

        command = input("Введіть команду: ").strip()

        matching_commands = [cmd for cmd in commands.keys() if cmd.startswith(command)]

        if len(matching_commands) == 1:
            return matching_commands[0]
        elif len(matching_commands) > 1:
            print("Кілька команд відповідають введеній частині. Будь ласка, уточніть:")
            for cmd in matching_commands:
                print(f" - {cmd}")
        else:
            print("Команду не знайдено. Спробуйте ще раз.")


# Головна функція програми
def main():
    db = NotesBook()

    while True:
        command = get_command_input()
        # Обробка команд
        if command == "hello":
            say_hello()

        elif command == "help":
            print_commands()

        elif command == "add_contact":
            add_contact()

        elif command == "add_phone":
            add_phone_to_contact()

        elif command == "change_contact":
            change_contact()

        elif command == "search_by_phone":
            search_by_phone()

        elif command == "all_contact":
            all_contact()

        elif command == "delete_contact":
            delete_contact()

        elif command == "add_birthday":
            name = input("Enter name: ")
            birthday = input("Enter birthday (DD.MM.YYYY): ")
            print(add_birthday([name, birthday], db))

        elif command == "show_birthday":
            name = input("Enter name: ")
            print(show_birthday([name], db))

        elif command == "show_all_birthdays":
            print(show_all_birthdays(db))

        elif command == "search_by_date_birthday":
            days = input("Enter number of days: ")
            print(search_by_date_birthday([days], db))

        elif command == "change_birthday":
            name = input("Enter name: ")
            new_birthday = input("Enter new birthday (DD.MM.YYYY): ")
            print(change_birthday([name, new_birthday], db))

        elif command == "delete_birthday":
            name = input("Enter name: ")
            print(delete_birthday([name], db))

        elif command == "add_note":
            text = input("Enter note text: ")
            tags = input("Enter tags separated by comma: ").split(",")
            db.add_note(text, tags)
            print("Note added.")
            all_notes = db.get_all_notes()
            print_notes(all_notes)

        elif command == "all_note":
            all_notes = db.get_all_notes()
            print_notes(all_notes)

        elif command == "search_note":
            search_tags = input("Enter tags to search separated by comma: ").split(",")
            found_notes = db.search_notes_by_tags(search_tags)
            print_notes(found_notes)

        elif command == "sorting_note_by_tags":
            sort_tags = input("Enter tags to sort by separated by comma: ").split(",")
            sorted_notes = db.sort_notes_by_tags(sort_tags)
            print_notes(sorted_notes)

        elif command == "delete_note":
            note_id_input = input("Enter note ID to delete: ")
            try:
                note_id = int(note_id_input)
                if db.delete_note(note_id):
                    print("Note deleted.")
                    all_notes = db.get_all_notes()
                    print_notes(all_notes)
                else:
                    print("Note with the given ID not found.")
            except ValueError:
                print(f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID.")

        elif command == "update_note":
            note_id_input = input("Enter note ID to update: ")
            try:
                note_id = int(note_id_input)
                text = input("Enter new text for the note: ")
                tags = input("Enter new tags for the note separated by comma: ").split(",")
                if db.update_note(note_id, text, tags):
                    print("Note updated.")
                    all_notes = db.get_all_notes()
                    print_notes(all_notes)
                else:
                    print("Note with the given ID not found.")
            except ValueError:
                print(f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID.")

        elif command in ("exit", "close"):
            print("Closing the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
