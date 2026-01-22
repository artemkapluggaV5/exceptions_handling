from database_exceptions import UserNotFoundError, UserAlreadyExistsError


class UserDatabase:

    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, email):
        if not isinstance(user_id, int):
            raise ValueError("user_id должен быть целым числом")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не может быть пустым")

        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email не может быть пустым")

        if user_id in self.users:
            raise UserAlreadyExistsError(user_id)

        self.users[user_id] = {
            "name": name,
            "email": email
        }

        print(f"Пользователь {name} добавлен")

    def get_user(self, user_id):
        if user_id not in self.users:
            raise UserNotFoundError(user_id)

        return self.users[user_id]

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise UserNotFoundError(user_id)

        deleted_user = self.users.pop(user_id)
        print(f"Пользователь {deleted_user['name']} удалён")

    def get_all_users(self):
        return self.users
