# Задача: Изменить нашу старую функцию квадрата так, чтобы мы могли управлять её размером.

import turtle

t = turtle.Turtle()
t.pensize(3)

# СОЗДАЕМ функцию с параметром (настройкой) 'size' (размер)
def draw_square(size):
    for i in range(4):
        t.forward(size) # Используем переданный размер!
        t.left(90)

# ВЫЗЫВАЕМ функцию с разными значениями
draw_square(30)   # Маленький квадрат
draw_square(80)   # Средний
draw_square(150)  # Большой

turtle.done()