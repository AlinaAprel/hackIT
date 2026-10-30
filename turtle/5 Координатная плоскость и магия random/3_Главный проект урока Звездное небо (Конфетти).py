#Задача: Нарисовать 50 звезд (точек) случайного размера, разбросанных в случайных местах экрана.
#Учитель: Здесь важно использовать penup() и pendown(), иначе Черепашка свяжет все звезды одной длинной "паутиной".

import turtle
import random

turtle.bgcolor("darkblue") # Цвет ночного неба

t = turtle.Turtle()
t.speed(0)
t.pencolor("white")

# Цикл на 50 звезд
for i in range(50):
    # 1. Генерируем случайные координаты (экран обычно размером от -200 до 200)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    
    # 2. Генерируем случайный размер звезды
    size = random.randint(5, 20)
    
    # 3. ТЕЛЕПОРТАЦИЯ (поднимаем перо, летим, опускаем)
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # 4. Рисуем звезду (точку)
    t.dot(size, "yellow")

turtle.done()