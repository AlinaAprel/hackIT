#Задача: Сделай так, чтобы точки из Задания 3 были не только желтыми, но и других случайных цветов. 
# Для этого используем новую команду — выбор случайного элемента из списка.

import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Создаем список возможных цветов (в квадратных скобках)
colors = ["red", "blue", "green", "yellow", "purple", "white", "cyan", "magenta"]

for i in range(100):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    size = random.randint(5, 25)
    
    # Выбираем случайный цвет из списка!
    random_color = random.choice(colors) 
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.dot(size, random_color)

turtle.done()