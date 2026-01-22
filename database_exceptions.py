class DatabaseError(Exception):
    pass


class UserNotFoundError(DatabaseError):

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Пользователь с ID {user_id} не найден")


class UserAlreadyExistsError(DatabaseError):

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"Пользователь с ID {user_id} уже существует")
