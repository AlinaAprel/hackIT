#КАЛЬКУЛЯТОР МАССЫ ТЕЛА
def calculate_bmi(weight, height):
    return weight / height ** 2;

weight = input("Введите ваш вес (кг): ");
height = input("Введите ваш рост (м): ");

if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height);
    print("Ваш ИМТ:", bmis);
else:
    print("Некорректные данные");
