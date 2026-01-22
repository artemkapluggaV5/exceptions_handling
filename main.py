from user_database import UserDatabase
from database_exceptions import UserNotFoundError, UserAlreadyExistsError


def main():

    db = UserDatabase()

    print("=" * 50)
    print("ТЕСТ 1: Добавление пользователей")
    print("=" * 50)

    try:
        db.add_user(1, "Иван Иванов", "ivan@test.com")
        db.add_user(2, "Петр Петров", "petr@test.com")
        db.add_user(3, "Петр Алигарх", "petr2@test.com")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 2: Попытка добавить дубликат")
    print("=" * 50)

    try:
        db.add_user(1, "Дубликат", "dup@test.com")
    except UserAlreadyExistsError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 3: Получение пользователя")
    print("=" * 50)

    try:
        user = db.get_user(1)
        print(f"Найден пользователь: {user}")
    except UserNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 4: Получение несуществующего пользователя")
    print("=" * 50)

    try:
        db.get_user(999)
    except UserNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 5: Удаление пользователя")
    print("=" * 50)

    try:
        db.delete_user(2)
    except UserNotFoundError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 6: Некорректные данные")
    print("=" * 50)

    try:
        db.add_user("строка", "", "")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n" + "=" * 50)
    print("ТЕСТ 7: Вывод всех пользователей")
    print("=" * 50)

    all_users = db.get_all_users()
    print(f"Всего пользователей в БД: {len(all_users)}")
    for user_id, user_data in all_users.items():
        print(
            f"  ID: {user_id}, Имя: {user_data['name']}, Email: {user_data['email']}"
        )


if __name__ == "__main__":
    main()
