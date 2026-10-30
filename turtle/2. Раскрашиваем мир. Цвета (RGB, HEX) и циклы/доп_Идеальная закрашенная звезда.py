#Задача: Нарисовать пятиконечную звезду и залить её желтым цветом (у звезды 5 линий, угол поворота 144 градуса).

import turtle
t = turtle.Turtle()
t.fillcolor("#FFD700") # Золотой цвет (Gold)
t.begin_fill()

for i in range(5):
    t.forward(150)
    t.right(144)       # Угол для классической звезды

t.end_fill()
turtle.done()