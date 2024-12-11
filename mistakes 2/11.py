def is_odd(number):
    if number % 2 == 1: 
        return True
    return Flase

num = int(input("Введите число: "))
if is_odd(num):
    print("Число нечетное.")
elif is_odd(num) == False:  # Ошибка: ненужное сравнение с False
    print("Число четное.")
