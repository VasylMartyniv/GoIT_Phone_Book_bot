import re
from src.classes.data_storage import User, DataStorage


class UsersDatabase:
    def __init__(self):
        self.storage = DataStorage("data.json")

    def add_contact(self, contacts):
        for contact in contacts:
            name = contact.get('name')
            phones = contact.get('phones', [])
            email = contact.get('email')
            birthday = contact.get('birthday')

            # Перевірка, чи є ім'я відсутнє або порожнє
            if not name or len(name) == 0:
                print("Ім'я контакту є обов'язковим.")
                continue

            # Перевірка, чи є телефони відсутні або порожні
            if not phones or len(phones) == 0:
                print("Для додавання контакту потрібно вказати хоча б один телефон.")
                continue

            if len(name) > 25:
                print(f"Ім'я {name} не повинно перевищувати 25 символів.")
                continue
            if not self.validate_phones(phones):
                print(f"Неправильний формат телефону для {name}.")
                continue
            if email and not self.validate_email(email):
                print(f"Неправильний формат email-адреси для {name}.")
                continue
            if birthday and not self.validate_date(birthday):
                print(f"Неправильний формат дати народження для {name}.")
                continue

            # Створюємо нового користувача тільки якщо всі поля пройшли валідацію
            new_user = User(id=self.storage.next_id, name=name, phones=phones, email=email, birthday=birthday)
            self.storage.users.append(new_user)
            self.storage.next_id += 1
            self.storage.save_users()  # Оновлюємо базу даних після додавання користувача
            print(f"Контакт з ім'ям {name} успішно додано.")

        self.storage.save_users()

    @staticmethod
    def validate_phones(phones):
        # Перевірка списку телефонів на валідність
        phone_regex = r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
        for phone in phones:
            if not re.match(phone_regex, phone):
                return False
        return True

    @staticmethod
    def validate_email(email):
        # Перевірка email на валідність
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_date(date_text):
        # Перевірка дати на валідність
        date_regex = r'^\d{2}-\d{2}-\d{4}$'
        return re.match(date_regex, date_text) is not None

    # def get_user_by_id(self, user_id):
    #     return self.storage.get_user_by_id(user_id)
    def search_contact(self, query):
        results = []
        for user in self.storage.users:
            if query in user.name or any(query in phone for phone in user.phones):
                results.append(user)
        return results
    
    def search_and_print_contacts(self, query):
        search_results = self.search_contact(query)
        for user in search_results:
            print(f"ID: {user.id}, Name: {user.name}, Phones: {user.phones}, Email: {user.email}, Birthday: {user.birthday}")

    


    def add_phone(self, user_id, phone):
        # Валідація телефону
        if not re.match(r'^\d{10}$', phone):
            print("Телефон повинен містити рівно 10 цифр.")
            return
        user = self.storage.get_user_by_id(user_id)
        if user:
            user.phones.append(phone)
            self.storage.save_users()
            print(f"Телефон {phone} додано до контакту з ID {user_id}.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")

    def change_contact(self, user_id, new_name):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if len(new_name) > 25:
                print("Ім'я не повинно перевищувати 25 символів.")
                return
            user.name = new_name
            self.storage.save_users()
            print(f"Контакт з ID {user_id} змінено на {new_name}.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")

    def delete_user(self, user_id):
        user = self.storage.get_user_by_id(user_id)
        if user:
            self.storage.users.remove(user)
            self.storage.save_users()
            print(f"Користувача з ID {user_id} видалено.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")

    def search_by_phone(self, phone_number):
        matching_users = [user for user in self.storage.users if phone_number in user.phones]
        return matching_users
    
    def delete_phone(self, user_id, phone_number):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if phone_number in user.phones:
                user.phones.remove(phone_number)
                self.storage.save_users()
                print(f"Телефон {phone_number} видалено з контакту з ID {user_id}.")
            else:
                print(f"Телефон {phone_number} не знайдено у контакті з ID {user_id}.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")



    def change_phone(self, user_id, old_phone, new_phone):
        # Валідація нового телефону
        if not re.match(r'^\d{10}$', new_phone):
            print("Новий телефон повинен містити рівно 10 цифр.")
            return
        user = self.storage.get_user_by_id(user_id)
        if user:
            if old_phone in user.phones:
                index = user.phones.index(old_phone)
                user.phones[index] = new_phone
                self.storage.save_users()
                print(f"Телефон {old_phone} змінено на {new_phone} у контакті з ID {user_id}.")
            else:
                print(f"Телефон {old_phone} не знайдено у контакті з ID {user_id}.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")



    def add_email(self, user_id, email):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if self.validate_email(email):
                user.email = email
                self.storage.save_users()
                print(f"Email {email} додано до контакту з ID {user_id}.")
            else:
                print("Неправильний формат email-адреси.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")

    # @staticmethod
    # def validate_email(email):
    #     # Проста перевірка формату email за допомогою регулярного виразу
    #     email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #     return re.match(email_regex, email) is not None
    

    def change_email(self, user_id, new_email):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if self.validate_email(new_email):
                user.email = new_email
                self.storage.save_users()
                print(f"Email для контакту з ID {user_id} змінено на {new_email}.")
            else:
                print("Неправильний формат email-адреси.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")



    def delete_email(self, user_id):
        user = self.storage.get_user_by_id(user_id)
        if user:
            if user.email:
                user.email = None
                self.storage.save_users()
                print(f"Email для контакту з ID {user_id} видалено.")
            else:
                print(f"У контакту з ID {user_id} немає email-адреси для видалення.")
        else:
            print(f"Користувача з ID {user_id} не знайдено.")   
