# Задача: Написать 4 функции для движения черепашки в 4 стороны 
# (Вверх, Вниз, Влево, Вправо). Привязать их к стрелкам клавиатуры.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.pensize(3)

# --- 1. ПИШЕМ ФУНКЦИИ ДВИЖЕНИЯ ---

def move_up():
    t.setheading(90)  # Поворачиваем на север
    t.forward(20)     # Делаем шаг

def move_down():
    t.setheading(270) # Поворачиваем на юг (или -90)
    t.forward(20)

def move_left():
    t.setheading(180) # Поворачиваем на запад
    t.forward(20)

def move_right():
    t.setheading(0)   # Поворачиваем на восток
    t.forward(20)

# --- 2. НАСТРАИВАЕМ КЛАВИАТУРУ ---

turtle.listen() # Говорим компьютеру: "Слушай клавиатуру!"

# Привязываем функции к кнопкам (ОБРАТИТЕ ВНИМАНИЕ: скобок после функций НЕТ!)
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

turtle.done()