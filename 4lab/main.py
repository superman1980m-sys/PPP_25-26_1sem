import json
import re


# Интерфейс для пользователя
class User:
    def get_full_name(self):
        raise NotImplementedError

    def get_email(self):
        raise NotImplementedError

    def display_info(self):
        raise NotImplementedError


# Класс для пользователей из CSV
class UserCSV(User):
    def __init__(self, uid, full_name, email):
        self.uid = uid
        self.full_name = full_name
        self.email = email

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def display_info(self):
        return f"{self.full_name} {self.email}"


# Класс для пользователей из JSON
class UserJSON(User):
    def __init__(self, data):
        self.uid = data["uid"]
        self.full_name = f"{data['first_name']} {data['last_name']}"
        self.email = data["contacts"]["email"]

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def display_info(self):
        return f"{self.full_name} {self.email}"


# Класс для пользователей из текстового формата
class UserRaw(User):
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_full_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def display_info(self):
        return f"{self.full_name} {self.email}"


# Функция для валидации email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))


# Класс для управления пользователями
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_by_name(self, name):
        result = [user for user in self.users if name.lower() in user.get_full_name().lower()]
        return result

    def get_all_emails(self):
        return [user.get_email() for user in self.users]

    def find_invalid_emails(self):
        invalid_users = [user for user in self.users if not is_valid_email(user.get_email())]
        return invalid_users


# Пример использования
if __name__ == "__main__":
    # Создание пользователей
    user1 = UserCSV("123", "Иван Иванов", "ivan@example.com")
    user2 = UserJSON({
        "uid": 42,
        "first_name": "Petr",
        "last_name": "Petrov",
        "contacts": {"email": "petr@example.com"}
    })
    user3 = UserRaw("Алексей Смирнов", "alexey.smirnov@invalid_email")
    
    # Управление пользователями
    manager = UserManager()
    manager.add_user(user1)
    manager.add_user(user2)
    manager.add_user(user3)

    # Пример поиска пользователей по имени
    search_results = manager.find_by_name("Иван")
    print("Search results for name 'Иван':")
    for user in search_results:
        print(user.display_info())

    # Пример вывода всех email
    print("\nAll emails:")
    for email in manager.get_all_emails():
        print(email)

    # Пример поиска некорректных email
    print("\nInvalid emails:")
    for user in manager.find_invalid_emails():
        print(user.display_info())

