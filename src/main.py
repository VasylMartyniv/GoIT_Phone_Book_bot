import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import readline

from tabulate import tabulate

from src.classes.notes_book import NotesBook
from src.classes.birthday import UsersDatabase
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
    users_db = UsersDatabase()

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

        
        # Обробка команди "update_birthday" з перевіркою
        elif command == "add_birthday":
            user_id_input = input(
                "Введіть ID користувача, дату народження якого потрібно оновити: "
            )
            try:
                user_id = int(user_id_input)
                new_birthday = input(
                    "Введіть новий день народження у форматі 'DD-MM-YYYY': "
                )
                users_db.add_birthday(user_id, new_birthday)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")

        # Обробка команди "delete_birthday"
        elif command == "delete_birthday":
            while True:
                user_id_input = input(
                    "Введіть ID користувача, для якого потрібно видалити день народження: "
                )
                try:
                    user_id = int(user_id_input)
                    users_db.delete_birthday(user_id)
                    break  # Вихід з циклу, якщо введення коректне
                except ValueError:
                    print(
                        f"Неправильний ID користувача '{user_id_input}'. Будь ласка, введіть коректне ціле число."
                    )

        # Обробка команди "show_birthday"
        elif command == "show_birthday":
            user_id_input = input(
                "Введіть ID користувача, для якого потрібно показати день народження: "
            )
            try:
                user_id = int(user_id_input)
                user = users_db.show_birthday(user_id)
                if user:
                    print(
                        f"ID: {user.id}, Name: {user.name}, Birthday: {user.birthday if user.birthday else 'не встановлено'}"
                    )
                else:
                    print("Користувача з вказаним ID не знайдено.")
            except ValueError:
                print(
                    f"Неправильний ID користувача '{user_id_input}'. Будь ласка, введіть коректне ціле число."
                )

        # Обробка команди "show_all_birthdays"
        elif command == "show_all_birthdays":
            birthdays = users_db.show_all_birthdays()
            for birthday in birthdays:
                print(birthday)

        # Обробка команди "search_by_date_birthday"
        elif command == "search_by_date_birthday":
            while True:
                days_input = input(
                    "Введіть кількість днів (максимум 365), на яку потрібно розширити проміжок для пошуку: "
                )
                try:
                    days = int(days_input)
                    if days > 365:
                        print(
                            "Кількість днів повинна бути не більше 365. Будь ласка, введіть коректне число."
                        )
                        continue  # Повернутись на початок циклу, щоб запитати введення знову
                    matching_users = users_db.search_by_date_birthday(days)
                    if matching_users:
                        print(
                            f"Контакти, у яких день народження відбувається в проміжку через {days} днів:"
                        )
                        for user in matching_users:
                            print(
                                f"ID: {user.id}, Name: {user.name}, Birthday: {user.birthday}"
                            )
                    else:
                        print(
                            f"Немає контактів, у яких день народження відбувається в проміжку через {days} днів."
                        )
                    break  # Вихід з циклу, якщо введення коректне
                except ValueError:
                    print("Неправильне значення днів. Будь ласка, введіть ціле число.")

        
        elif command == "add_note":
            text = input("Enter note text: ")
            tags = input("Enter tags separated by comma: ").split(",")
            db.add_note(text, tags)
            print("Note added.")
            all_notes = (
                db.get_all_notes()
            )  # Оновлюємо all_notes після додавання нотатки
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
                print(
                    f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID."
                )

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
                print(
                    f"Invalid note ID '{note_id_input}'. Please enter a valid integer ID."
                )

        elif command in ("exit", "close"):
            print("Closing the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
