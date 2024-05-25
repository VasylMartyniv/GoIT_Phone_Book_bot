import json

from src.classes.note import Note


# Клас для управління базами даних нотаток
class NotesBook:
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

    # Метод для отримання запису за його ID
    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

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
        while True:
            try:
                id = int(id)  # Перевірка, чи є id цілим числом
                break  # Якщо id є цілим числом, вихід з циклу
            except ValueError:
                print("Неправильний формат ID. Будь ласка, введіть ціле число.")
                id = input("Введіть ID нотатки для оновлення: ")

        for note in self.notes:
            if note.id == id:
                note.text = text
                note.tags = tags
                self.save_notes()  # Збереження нотаток після оновлення
                return True
        print("Нотатки з таким ID не знайдено.")
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
