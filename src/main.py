import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import readline
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
# from tabulate import tabulate

from src.classes.user import UsersDatabase
from src.classes.notes_book import NotesBook
from src.classes.birthday import Birthdaybase
from src.constants.commands import commands
from src.utils.utils import *


# Функція для автодоповнення команд
def completer(text, state):
    options = [cmd for cmd in commands.keys() if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

# # Функція для отримання введеної команди з автодоповненням
# def get_command_input():
#     while True:
#         readline.set_completer(completer)
#         readline.parse_and_bind("tab: complete")

#         command = input("Введіть команду: ").strip()

#         matching_commands = [cmd for cmd in commands.keys() if cmd.startswith(command)]

#         if len(matching_commands) == 1:
#             return matching_commands[0]
#         elif len(matching_commands) > 1:
#             print("Кілька команд відповідають введеній частині. Будь ласка, уточніть:")
#             for cmd in matching_commands:
#                 print(f" - {cmd}")
#         else:
#             print("Команду не знайдено. Спробуйте ще раз.")
# Створюємо список команд для автодоповнення
command_completer = WordCompleter(list(commands.keys()), ignore_case=True)

# Функція для отримання введеної команди з автодоповненням
def get_command_input():
    while True:
        command = prompt("Введіть команду: ", completer=command_completer)
        command = command.strip()

        # Перевіряємо, чи існує команда
        if command in commands:
            return command
        else:
            print("Команду не знайдено. Спробуйте ще раз.")


# Головна функція програми
def main():
    db = NotesBook()
    user_db = UsersDatabase()
    birthday_db = Birthdaybase()

    while True:
        command = get_command_input()
        # Обробка команд
        if command == "hello":
            say_hello()

        elif command == "help":
            print_commands()
        
        elif command == "add_contact":
            name = input("Введіть ім'я нового контакту: ")
            phones = input("Введіть телефони через кому: ").split(',')
            email = input("Введіть email: ")
            birthday = input("Введіть дату народження у форматі 'DD-MM-YYYY': ")
            # Створюємо список контактів з одним контактом
            contact = [{'name': name, 'phones': phones, 'email': email, 'birthday': birthday}]
            user_db.add_contact(contact)  # Використовуємо метод add_contacts

        elif command == "search_contact":
            query = input("Введіть тег для пошуку: ")
            user_db.search_and_print_contacts(query)

        elif command == "add_phone":
            user_id_input = input("Введіть ID користувача, до якого потрібно додати телефон: ")
            try:
                user_id = int(user_id_input)
                phone = input("Введіть новий телефон: ")
                user_db.add_phone(user_id, phone)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")

        elif command == "change_contact":
            user_id_input = input("Введіть ID користувача, якого потрібно змінити: ")
            try:
                user_id = int(user_id_input)
                new_name = input("Введіть нове ім'я для контакту: ")
                user_db.change_contact(user_id, new_name)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")

        elif command == "search_by_phone":
            phone_number = input("Введіть номер телефону для пошуку: ")
            matching_users = user_db.search_by_phone(phone_number)
            if matching_users:
                print("Знайдені контакти:")
                for user in matching_users:
                    print(user)
            else:
                print("Контакти з таким номером телефону не знайдені.")


        elif command == "delete_phone":
            user_id_input = input("Введіть ID користувача, з якого потрібно видалити телефон: ")
            phone_number = input("Введіть номер телефону, який потрібно видалити: ")
            try:
                user_id = int(user_id_input)
                user_db.delete_phone(user_id, phone_number)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")



        elif command == "change_phone":
            user_id_input = input("Введіть ID користувача, якому потрібно змінити телефон: ")
            old_phone = input("Введіть старий телефон, який потрібно замінити: ")
            new_phone = input("Введіть новий телефон: ")
            try:
                user_id = int(user_id_input)
                user_db.change_phone(user_id, old_phone, new_phone)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")


        elif command == "add_email":
            user_id_input = input("Введіть ID користувача, до якого потрібно додати email: ")
            email = input("Введіть email: ")
            try:
                user_id = int(user_id_input)
                user_db.add_email(user_id, email)
            except ValueError:
                print("ID користувача повинно бути цілим числом.")   

        elif command == "change_email":
            user_id = input("Введіть ID користувача: ")
            new_email = input("Введіть новий email: ")
            user_db.change_email(user_id, new_email)

        elif command == "delete_email":
            user_id = input("Введіть ID користувача: ")
            user_db.delete_email(user_id)




        elif command == "all_contact":
            print("Список всіх контактів:")
            for user in user_db.storage.users:
                print(user)

        elif command == "delete_contact":
            user_id_input = input("Введіть ID користувача, якого потрібно видалити: ")
            try:
                user_id = int(user_id_input)
                if user_db.get_user_by_id(user_id):
                    user_db.delete_user(user_id)
                    print(f"Контакт з ID {user_id} видалено.")
                else:
                    print("Користувача з вказаним ID не знайдено.")
            except ValueError:
                print("ID користувача повинно бути цілим числом.")


        elif command == "add_birthday":
            user_id_input = input(
                "Введіть ID користувача, дату народження якого потрібно оновити: "
            )
            try:
                user_id = int(user_id_input)
                # Перевіряємо, чи існує користувач з введеним ID
                if birthday_db.get_user_by_id(user_id) is not None:
                    new_birthday = input(
                        "Введіть новий день народження у форматі 'DD-MM-YYYY': "
                    )
                    birthday_db.add_birthday(user_id, new_birthday)
                else:
                    print("Користувача з вказаним ID не знайдено.")
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
                    if birthday_db.get_user_by_id(user_id) is not None:
                        birthday_db.delete_birthday(user_id)
                        break  # Вихід з циклу, якщо введення коректне
                    else:
                        print("Користувача з вказаним ID не знайдено.")
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
                user = birthday_db.show_birthday(user_id)
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
            birthdays = birthday_db.show_all_birthdays()
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
                    matching_users = birthday_db.search_by_date_birthday(days)
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
            note_id_input = input("Введіть ID запису для видалення: ")
            try:
                note_id = int(note_id_input)
                if db.get_note_by_id(note_id) is not None:
                    if db.delete_note(note_id):
                        print("Запис видалено.")
                        all_notes = db.get_all_notes()
                        print_notes(all_notes)
                    else:
                        print("Запис з вказаним ID не знайдено.")
                else:
                    print("Запис з вказаним ID не знайдено.")
            except ValueError:
                print(
                    f"Некоректний ID запису '{note_id_input}'. Будь ласка, введіть ціле число."
                )

        elif command == "update_note":
            note_id_input = input("Введіть ID запису, який потрібно оновити: ")
            try:
                note_id = int(note_id_input)
                # Перевіряємо, чи існує запис з введеним ID
                if db.get_note_by_id(note_id) is not None:
                    text = input("Введіть новий текст для запису: ")
                    tags = input("Введіть нові теги для запису, розділені комами: ").split(",")
                    if db.update_note(note_id, text, tags):
                        print("Запис оновлено.")
                        all_notes = db.get_all_notes()
                        print_notes(all_notes)
                    else:
                        print("Запис з вказаним ID не знайдено.")
                else:
                    print("Запис з вказаним ID не знайдено.")
            except ValueError:
                print(
                    f"Некоректний ID запису '{note_id_input}'. Будь ласка, введіть ціле число."
                )


        elif command in ("exit", "close"):
            print("Closing the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
