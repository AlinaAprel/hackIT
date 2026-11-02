# Задача: Добавим второй параметр — цвет заливки. Нарисуем три разных треугольника.

import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(0)

# Функция принимает 2 параметра: размер (size) и цвет (color)
def draw_triangle(size, color):
    t.fillcolor(color)   # Используем переданный цвет
    t.begin_fill()
    
    for i in range(3):
        t.forward(size)  # Используем переданный размер
        t.left(120)
        
    t.end_fill()

# --- ОСНОВНАЯ ПРОГРАММА ---

draw_triangle(50, "red")       # Маленький красный

t.penup()
t.forward(100)
t.pendown()

draw_triangle(100, "green")    # Средний зеленый

t.penup()
t.forward(150)
t.pendown()

draw_triangle(150, "orange")   # Большой оранжевый

turtle.done()