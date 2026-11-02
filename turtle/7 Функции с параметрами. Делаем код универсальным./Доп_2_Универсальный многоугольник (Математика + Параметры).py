# Задача: Напиши функцию draw_polygon(sides, length). 
# Функция должна принимать количество сторон (sides) и длину линии (length). 
# Угол поворота функция должна вычислять сама внутри себя (вспомни формулу 360 / sides). 
# Нарисуй с помощью этой функции треугольник, квадрат и шестиугольник.

import turtle
t = turtle.Turtle()
t.speed(0)

def draw_polygon(sides, length):
    # Компьютер сам считает угол!
    angle = 360 / sides 
    
    for i in range(sides):
        t.forward(length)
        t.left(angle)

# Рисуем
draw_polygon(3, 100) # Треугольник (3 стороны)
draw_polygon(4, 100) # Квадрат (4 стороны)
draw_polygon(6, 100) # Шестиугольник (6 сторон)
draw_polygon(10, 50) # Десятиугольник

turtle.done()