#Задача: Сделай так, чтобы каждый новый квадрат в мандале менял цвет.
#(Для детей, которые быстро схватывают, можно показать простейший список цветов).

import turtle
t = turtle.Turtle()
t.speed(0)

# Список цветов (в квадратных скобках)
colors = ["red", "blue", "green", "orange", "purple", "gold"]

for i in range(36):
    t.pencolor(colors[i % 6])  # Фокус: остаток от деления выбирает цвет по кругу
    
    for j in range(4):
        t.forward(100)
        t.left(90)
        
    t.right(10)

turtle.done()