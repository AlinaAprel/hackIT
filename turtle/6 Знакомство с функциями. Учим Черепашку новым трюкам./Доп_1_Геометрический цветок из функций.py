# Задача: У тебя уже есть функция draw_square() (возьми из Задания 1). 
# Напиши цикл, который 36 раз вызывает функцию draw_square(), 
# а после каждого вызова поворачивает черепашку на 10 градусов.
# Полезный урок: Функция работает точно так же, как обычная команда вроде forward(), 
# поэтому её можно вставлять внутрь циклов!

import turtle
t = turtle.Turtle()
t.speed(0)
t.pencolor("purple")

def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)

# Основная программа
for i in range(36):
    draw_square() # Вызов функции
    t.right(10)   # Поворот

turtle.done()