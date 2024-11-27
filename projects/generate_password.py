import random
import string

def generate_password(length):
    """
    Генерирует случайный пароль заданной длины.
    :param length: Длина пароля (int)
    :return: Сгенерированный пароль (str)
    """
    if length < 4:
        return "Пароль должен быть не менее 4 символов!"

    # Список символов для пароля
    characters = string.ascii_letters + string.digits + string.punctuation

    # Гарантируем, что пароль будет содержать хотя бы одну букву, цифру и специальный символ
    password = [
        random.choice(string.ascii_lowercase),  # Одна строчная буква
        random.choice(string.ascii_uppercase),  # Одна заглавная буква
        random.choice(string.digits),          # Одна цифра
        random.choice(string.punctuation)      # Один спецсимвол
    ]

    # Добавляем остальные случайные символы
    password += random.choices(characters, k=length - 4)

    # Перемешиваем пароль, чтобы порядок символов был случайным
    random.shuffle(password)

    return ''.join(password)

# Пример использования
if __name__ == "__main__":
    print("Генератор пароля")
    try:
        length = int(input("Введите длину пароля: "))
        print(f"Ваш сгенерированный пароль: {generate_password(length)}")
    except ValueError:
        print("Ошибка: длина пароля должна быть числом.")
