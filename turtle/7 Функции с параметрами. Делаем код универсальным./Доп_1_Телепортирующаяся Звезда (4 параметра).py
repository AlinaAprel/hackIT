# Задача: Напиши функцию draw_star(x, y, size, color). 
# Эта функция должна сама телепортировать Черепашку по координатам x и y, 
# а затем рисовать там звезду заданного размера и цвета. 
# В основной программе разбросай 3 разные звезды.

import turtle
t = turtle.Turtle()
t.speed(0)

def draw_star(x, y, size, color):
    # Телепортация внутри функции!
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Рисование
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Вызовы
draw_star(100, 100, 50, "gold")
draw_star(-150, 50, 30, "red")
draw_star(0, -100, 100, "purple")

turtle.done()
