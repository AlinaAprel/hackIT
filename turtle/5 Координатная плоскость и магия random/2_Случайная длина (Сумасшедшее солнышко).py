#Задача: Подключаем random. Нарисуем лучи из центра, но длина каждого луча будет случайной!

import turtle
import random  # Подключаем модуль для случайных чисел

t = turtle.Turtle()
t.speed(0)
t.pencolor("gold")
t.pensize(2)

turtle.bgcolor("black") # Черный фон (вызываем у экрана!)

for i in range(36):
    # Компьютер бросает кубик от 20 до 150 и кладет число в переменную dlina
    dlina = random.randint(20, 150) 
    
    t.forward(dlina)     # Идем на случайную длину
    t.backward(dlina)    # Возвращаемся обратно на ту же длину в центр!
    t.right(10)          # Поворачиваемся для следующего луча

turtle.done()