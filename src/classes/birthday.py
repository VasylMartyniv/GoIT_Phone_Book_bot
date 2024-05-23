from datetime import datetime, timedelta
from addressbook import AddressBook, Record, Birthday

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # Викликає функцію, що передана декоратору
        except IndexError:
            return "Не достатньо аргументів. Будь ласка, дотримуйтесь формату команди."
        except ValueError:
            return "Некоректні дані. Переконайтеся, що ви вводите правильні типи даних."
        except KeyError:
            return "Контакт не знайдено."
    return inner

# Функція для додавання дня народження до контакту
@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise IndexError("Please provide a name and a birthday in the format DD.MM.YYYY.")
    name, birthday = args  # Отримуємо ім'я та дату народження з аргументів
    record = book.find(name)  # Знаходимо контакт у книзі за ім'ям
    if record:
        record.add_birthday(birthday)  # Додаємо день народження до контакту
        return f"Birthday for {name} added as {birthday}."
    else:
        raise KeyError(f"Contact '{name}' not found.")  # Виводимо помилку, якщо контакт не знайдено

# Функція для показу дня народження контакту
@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]  # Отримуємо ім'я з аргументів
    record = book.find(name)  # Знаходимо контакт у книзі за ім'ям
    if record:
        if record.birthday:
            return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."
        else:
            return f"{name} does not have a birthday set."
    else:
        raise KeyError(f"Contact '{name}' not found.")  # Виводимо помилку, якщо контакт не знайдено

# Функція для показу всіх контактів з днями народження
@input_error
def show_all_birthdays(book):
    birthdays = [str(record) for record in book.values() if record.birthday]  # Отримуємо всі контакти з днями народження
    if not birthdays:
        return "No birthdays available."
    return "\n".join(birthdays)  # Повертаємо список контактів з днями народження

# Функція для пошуку контактів за датою народження
@input_error
def search_by_date_birthday(args, book):
    if len(args) != 1:
        raise IndexError("Please provide a date in the format DD.MM.YYYY.")
    date_str = args[0]  # Отримуємо дату з аргументів
    try:
        date = datetime.strptime(date_str, '%d.%m.%Y').date()  # Перетворюємо строку в дату
    except ValueError:
        raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    results = [str(record) for record in book.values() if record.birthday and record.birthday.value == date]  # Знаходимо контакти з відповідною датою народження
    if not results:
        return "No contacts found with this birthday."
    return "\n".join(results)  # Повертаємо список контактів з цією датою народження

# Функція для зміни дня народження контакту
@input_error
def change_birthday(args, book):
    if len(args) != 2:
        raise IndexError("Please provide a name and a new birthday in the format DD.MM.YYYY.")
    name, new_birthday = args
    record = book.find(name)
    if record:
        record.change_birthday(new_birthday)
        return f"Birthday for {name} changed to {new_birthday}."
    else:
        raise KeyError(f"Contact '{name}' not found.")

# Функція для видалення дня народження контакту
@input_error
def delete_birthday(args, book):
    if len(args) != 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    record = book.find(name)
    if record:
        record.delete_birthday()
        return f"Birthday for {name} deleted."
    else:
        raise KeyError(f"Contact '{name}' not found.")

