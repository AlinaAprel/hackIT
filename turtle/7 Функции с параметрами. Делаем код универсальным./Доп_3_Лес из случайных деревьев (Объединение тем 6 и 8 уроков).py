# Задача: У тебя есть функция для рисования дерева (ствол + крона). 
# Подключи библиотеку random. 
# Сделай цикл из 10 повторений, где координаты дерева, 
# высота ствола и размер кроны генерируются случайно, а затем передаются в функцию!

import turtle
import random

t = turtle.Turtle()
t.speed(0)

def draw_tree(x, y, h):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90) # Смотрим вверх
    
    # Ствол
    t.pencolor("brown")
    t.pensize(5)
    t.forward(h)
    
    # Крона
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    t.circle(h/2) # Радиус зависит от высоты ствола!
    t.end_fill()

for i in range(10):
    rand_x = random.randint(-200, 200)
    rand_y = random.randint(-200, -50)
    rand_h = random.randint(30, 80)
    
    draw_tree(rand_x, rand_y, rand_h)

turtle.done()
