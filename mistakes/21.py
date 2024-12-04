def is_even(number):
    if number % 2 == 1:
        return True
    else:
        return False

num = int(input("Введите число: "))
print(f"Число четное: {is_even(num)}")
