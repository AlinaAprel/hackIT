#Задача: Нарисуй 3 круга рядом друг с другом разного цвета (синий, черный, красный),
#  не оставляя между ними соединительных линий. Команды для прыжка ученик должен написать сам.

import turtle
t = turtle.Turtle()
t.pensize(5)

# Кольцо 1 (Синее)
t.pencolor("blue")
t.circle(50)

# Прыжок
t.penup()
t.forward(110)
t.pendown()

# Кольцо 2 (Черное)
t.pencolor("black")
t.circle(50)

# Прыжок
t.penup()
t.forward(110)
t.pendown()

# Кольцо 3 (Красное)
t.pencolor("red")
t.circle(50)

turtle.done()