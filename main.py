import json
import readline
from tabulate import tabulate


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
    print("Feature coming soon")


def show_birthday():
    print("Feature coming soon")


def show_all_birthdays():
    print("Feature coming soon")


def search_by_date_birthday():
    print("Feature coming soon")


# Клас для представлення нотатки з ідентифікатором, текстом та тегами
class Note:
    def __init__(self, id, text, tags):
        self.id = id
        self.text = text
        self.tags = tags


# Клас для управління базами даних нотаток
class NotesDatabase:
    def __init__(self):
        self.notes = []
        self.next_id = 1
        self.load_notes()  # Завантаження нотаток з файлу при створенні об'єкта

    # Метод для додавання нотатки
    def add_note(self, text, tags):
        note = Note(self.next_id, text, tags)
        self.notes.append(note)
        self.next_id += 1
        self.save_notes()  # Збереження нотаток після додавання

    # Метод для отримання всіх нотаток
    def get_all_notes(self):
        return self.notes

    # Метод для пошуку нотаток за тегами
    def search_notes_by_tags(self, tags):
        return [note for note in self.notes if any(tag in note.tags for tag in tags)]

    # Метод для сортування нотаток за тегами
    def sort_notes_by_tags(self, tags):
        sorted_notes = sorted(
            [note for note in self.notes if any(tag in note.tags for tag in tags)],
            key=lambda note: sum(tag in note.tags for tag in tags),
            reverse=True,
        )
        return sorted_notes

    # Метод для видалення нотатки за ідентифікатором
    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_notes()  # Збереження нотаток після видалення
        return True

    # Метод для оновлення нотатки
    def update_note(self, id, text, tags):
        for note in self.notes:
            if note.id == id:
                note.text = text
                note.tags = tags
                self.save_notes()  # Збереження нотаток після оновлення
                return True
        return False

    # Метод для збереження нотаток у файл
    def save_notes(self):
        with open("notes.json", "w") as file:
            json_notes = [
                {"id": note.id, "text": note.text, "tags": note.tags}
                for note in self.notes
            ]
            json.dump(json_notes, file)

    # Метод для завантаження нотаток з файлу
    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                json_notes = json.load(file)
                self.notes = [
                    Note(note["id"], note["text"], note["tags"]) for note in json_notes
                ]
                self.next_id = (
                    max(self.notes, key=lambda note: note.id).id + 1
                    if self.notes
                    else 1
                )
        except FileNotFoundError:
            pass


# Словник команд та їх описи
commands = {
    "add_contact": "Додати контакт",
    "add_phone": "Додати телефон до контакту",
    "change_contact": "Змінити контакт",
    "search_by_phone": "Пошук за номером телефону",
    "all_contact": "Показати всі контакти",
    "delete_contact": "Видалити контакт",
    "add_birthday": "Додати день народження",
    "show_birthday": "Показати день народження",
    "show_all_birthdays": "Показати всі дні народження",
    "search_by_date_birthday": "Пошук за датою народження",
    "add_note": "Додати нотатку",
    "all_note": "Показати всі нотатки",
    "search_note": "Пошук нотаток за тегами",
    "sorting_note_by_tags": "Сортування нотаток за тегами",
    "delete_note": "Видалити нотатку",
    "update_note": "Оновити нотатку",
    "hello": "Привіт",
    "exit": "Вийти",
    "close": "Вийти",
}


# Функція для друку нотаток у вигляді таблиці
def print_notes(notes):
    if not notes:
        print("Немає нотаток для виводу.")
    else:
        table = [[note.id, ", ".join(note.tags), note.text] for note in notes]
        print(tabulate(table, headers=["ID", "Tags", "Text"], tablefmt="grid"))


def say_hello():
    print("Hello!")


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

        choice = input("Введіть команду: ").strip()

        matching_commands = [cmd for cmd in commands.keys() if cmd.startswith(choice)]

        if len(matching_commands) == 1:
            return matching_commands[0]
        elif len(matching_commands) > 1:
            print("Кілька команд відповідають введеній частині. Будь ласка, уточніть:")
            for cmd in matching_commands:
                print(f" - {cmd}")
        else:
            print("Команду не знайдено. Спробуйте ще раз.")


# Функція для друку команд у вигляді таблиці
def print_commands(commands):
    table = [[cmd, description] for cmd, description in commands.items()]
    print(tabulate(table, headers=["Command", "Description"], tablefmt="grid"))


# Головна функція програми
def main():
    db = NotesDatabase()

    while True:
        print("\nAvailable commands:")
        print_commands(commands)

        choice = get_command_input()
        # Обробка команд
        if choice == "hello":
            say_hello()

        elif choice == "add_contact":
            add_contact()

        elif choice == "add_phone":
            add_phone_to_contact()

        elif choice == "change_contact":
            change_contact()

        elif choice == "search_by_phone":
            search_by_phone()

        elif choice == "all_contact":
            all_contact()

        elif choice == "delete_contact":
            delete_contact()

        elif choice == "add_birthday":
            add_birthday()

        elif choice == "show_birthday":
            show_birthday()

        elif choice == "show_all_birthdays":
            show_all_birthdays()

        elif choice == "search_by_date_birthday":
            search_by_date_birthday()

        elif choice == "add_note":
            text = input("Enter note text: ")
            tags = input("Enter tags separated by comma: ").split(",")
            db.add_note(text, tags)
            print("Note added.")
            all_notes = (
                db.get_all_notes()
            )  # Оновлюємо all_notes після додавання нотатки
            print_notes(all_notes)

        elif choice == "all_note":
            all_notes = db.get_all_notes()
            print_notes(all_notes)

        elif choice == "search_note":
            search_tags = input("Enter tags to search separated by comma: ").split(",")
            found_notes = db.search_notes_by_tags(search_tags)
            print_notes(found_notes)

        elif choice == "sorting_note_by_tags":
            sort_tags = input("Enter tags to sort by separated by comma: ").split(",")
            sorted_notes = db.sort_notes_by_tags(sort_tags)
            print_notes(sorted_notes)

        elif choice == "delete_note":
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

        elif choice == "update_note":
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

        elif choice in ("exit", "close"):
            print("Closing the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
