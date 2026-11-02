#Задача: Зачем мы писали def, если могли просто написать код? 
# А затем, что теперь мы можем нарисовать 3 квадрата в разных местах, 
# написав всего три коротких слова вместо 15 строк кода!

import turtle

t = turtle.Turtle()
t.speed(0)

# Функция (наш чертеж квадрата)
def draw_square():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()

# --- ОСНОВНАЯ ПРОГРАММА ---
# Рисуем первый квадрат
draw_square()

# Телепортируемся в другое место
t.penup()
t.goto(100, 50)
t.pendown()

# Рисуем второй квадрат (просто вызываем команду!)
draw_square()

# Телепортируемся еще раз
t.penup()
t.goto(-100, -50)
t.pendown()

# Рисуем третий квадрат
draw_square()

turtle.done()
