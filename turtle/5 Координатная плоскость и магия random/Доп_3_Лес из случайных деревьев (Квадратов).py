#Задача: Разбросай по экрану не просто точки, а настоящие деревья (зеленые квадратики со стволом). 
# Координата Y должна быть от -200 до 0 (чтобы деревья росли на "земле", в нижней половине экрана), 
# а X — от -250 до 250.
#Подсказка: Создай цикл телепортации. После приземления на случайную точку рисуй линию вверх (ствол) 
# и зеленый квадрат на ней (крону).

import turtle
import random

turtle.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(0)

for i in range(15): # Сажаем 15 деревьев
    # Деревья растут только внизу (Y с минусом)
    x = random.randint(-200, 200)
    y = random.randint(-200, -50)
    
    # Телепортация
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90) # Всегда смотрим строго вверх (север) перед рисованием
    
    # Рисуем ствол
    t.pencolor("brown")
    t.pensize(5)
    t.forward(30)
    
    # Рисуем квадратную крону
    t.pencolor("green")
    t.fillcolor("green")
    t.pensize(1)
    
    t.begin_fill()
    for j in range(4): # Цикл для квадрата (кроны)
        t.forward(40)
        t.right(90)
    t.end_fill()

turtle.done()