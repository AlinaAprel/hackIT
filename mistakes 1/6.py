#ПРОСТОЙ КАЛЬКУЛЯТОР
def add(a, b):
    return a + b;

def subtract(a, b):
    return a - b;

operation = input("Введите операцию (+ или -): ");
num1 = int(input("Введите первое число: "));
num2 = int(input("Введите второе число: "));

if operation == "+":
    res = add(num1, num2);
else if operation == "-":
    res = subtract(num1, num2);
else:
    print("Операция не распознана");

print("Результат:", result);
