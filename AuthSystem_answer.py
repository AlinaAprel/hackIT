import re

class AuthSystem:
    def __init__(self):
        # База данных в виде словаря: {логин: пароль}
        self.users = {"admin": "Admin123"}
        # Шаблоны регулярных выражений
        self.login_pattern = r"^[a-zA-Z0-9_]{3,15}$"
        self.password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$"

    def validate_login(self, login):
        """Проверяет логин регулярным выражением."""
        return bool(re.match(self.login_pattern, login))

    def validate_password(self, password):
        """Проверяет пароль регулярным выражением."""
        return bool(re.match(self.password_pattern, password))

    def register(self):
        print("\n--- РЕГИСТРАЦИЯ ---")
        login = input("Придумайте логин (3-15 символов, буквы/цифры): ")
        
        if not self.validate_login(login):
            print("❌ Ошибка: Неверный формат логина!")
            return
        
        if login in self.users:
            print("❌ Ошибка: Такой пользователь уже существует!")
            return

        password = input("Придумайте пароль (минимум 6 символов, буквы и цифры): ")
        if not self.validate_password(password):
            print("❌ Ошибка: Пароль слишком простой!")
            return

        self.users[login] = password
        print(f"🎉 Успешная регистрация! Добро пожаловать, {login}!")

    def login(self):
        print("\n--- ВХОД В СИСТЕМУ ---")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in self.users and self.users[login] == password:
            print(f"🔓 Вход выполнен! Привет, {login}!")
        else:
            print("❌ Ошибка: Неверный логин или пароль!")

    def forgot_password(self):
        print("\n--- ВОССТАНОВЛЕНИЕ ПАРОЛЯ ---")
        login = input("Введите ваш логин: ")

        if login in self.users:
            print(f"ℹ️ Напоминание: Ваш пароль: {self.users[login]}")
        else:
            print("❌ Ошибка: Такой пользователь не найден!")

    def start(self):
        """Главный цикл консольного меню."""
        while True:
            print("\n=== ГЛАВНОЕ МЕНЮ ===")
            print("1. Войти")
            print("2. Зарегистрироваться")
            print("3. Забыл пароль")
            print("4. Выйти из программы")
            
            choice = input("Выберите действие (1-4): ")
            
            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                self.forgot_password()
            elif choice == "4":
                print("Программа завершена. До свидания!")
                break
            else:
                print("❌ Неверный ввод! Выберите пункт от 1 до 4.")

# Запуск программы
if __name__ == "__main__":
    app = AuthSystem()
    app.start()
