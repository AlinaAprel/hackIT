grade = int(input("Введите вашу оценку (0-100): "))
if 90 <= grade <= 100:
    print("Отлично!")
elif 70 <= grade < 90:
    print("Хорошо")
elif 50 <= grade < 70:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")
