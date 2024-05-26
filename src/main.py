import readline

from src.classes.notes_book import NotesBook
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
    notes_db = NotesBook()
    users_db = load_contacts()
    try:
        while True:
            command = get_command_input()
            # Обробка команд
            if command == "hello":
                say_hello()

            elif command == "help":
                list_commands()

            elif command == "all_contacts":
                print(users_db)

            elif command == "add_contact":
                add_contact(users_db)

            if command == "search_contact":
                search_contact(users_db)

            elif command == "change_contact":
                change_contact(users_db)

            elif command == "delete_contact":
                delete_contact(users_db)

            elif command == "add_phone":
                add_phone(users_db)

            elif command == "delete_phone":
                delete_phone(users_db)

            elif command == "change_phone":
                change_phone(users_db)

            elif command == "search_by_phone":
                search_by_phone(users_db)

            elif command == "add_email":
                add_email(users_db)

            elif command == "change_email":
                change_email(users_db)

            elif command == "delete_email":
                delete_email(users_db)

            elif command == "search_by_email":
                search_by_email(users_db)

            elif command == "add_birthday":
                add_birthday(users_db)

            elif command == "delete_birthday":
                delete_birthday(users_db)

            elif command == "show_birthday":
                show_birthday(users_db)

            elif command == "show_all_birthdays":
                show_all_birthdays(users_db)

            elif command == "search_by_date_birthday":
                search_by_date_birthday(users_db)

            elif command == "show_next_birthday":
                show_next_birthday(users_db)

            elif command == "add_address":
                add_address(users_db)

            elif command == "change_address":
                change_address(users_db)

            elif command == "delete_address":
                delete_address(users_db)

            elif command == "add_note":
                add_note(notes_db)

            elif command == "all_notes":
                all_notes(notes_db)

            elif command == "search_note":
                search_note_by_tags(notes_db)

            elif command == "sorting_note_by_tags":
                sorting_note_by_tags(notes_db)

            elif command == "delete_note":
                delete_note_by_id(notes_db)

            elif command == "update_note":
                update_note(notes_db)

            elif command in ("exit", "close"):
                save_contacts(users_db)
                print("Closing the program. Goodbye!")
                break
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
