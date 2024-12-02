def greet(name):
    return "Привет, " + name + "!"

name = input("Введите ваше имя: ")
greeting = greet
print(greeting(name))
