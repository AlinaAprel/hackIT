import turtle
import random

t = turtle.Turtle()
t.pensize(5)
colors = ["#FF5733", "#33FF57", "#3357FF", "gold", "purple"]

# Компьютер сам берет 1 случайный цвет из массива
random_col = random.choice(colors) 
t.color(random_col)

for i in range(4):
    t.forward(100)
    t.left(90)