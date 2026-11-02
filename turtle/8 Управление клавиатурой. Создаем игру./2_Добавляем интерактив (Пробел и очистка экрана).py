# Задача: Продолжаем код из Задания 1. 
# Добавим возможность поднимать/опускать перо по пробелу, 
# и стирать всё нарисованное кнопкой "c" (clear).

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

# Добавляем новые функции
def lift_pen():
    t.penup()

def drop_pen():
    t.pendown()

def clear_screen():
    t.clear() # Специальная команда, которая стирает рисунок, оставляя черепашку на месте

# --- 2. НАСТРАИВАЕМ КЛАВИАТУРУ ---

turtle.listen() # Говорим компьютеру: "Слушай клавиатуру!"

# Привязываем функции к кнопкам (ОБРАТИТЕ ВНИМАНИЕ: скобок после функций НЕТ!)
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

# Привязываем новые кнопки (добавляем в конец программы перед turtle.done)
turtle.onkeypress(lift_pen, "space")   # Пробел - поднять перо
turtle.onkeypress(drop_pen, "Return")   # Enter - опустить перо
turtle.onkeypress(clear_screen, "c")   # Буква 'c' (англ) - очистить экран

turtle.done()

