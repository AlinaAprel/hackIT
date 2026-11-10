import turtle
t = turtle.Turtle()
t.pensize(5)

my_colors = ["red", "green", "blue"]

for c in my_colors:
    t.pencolor(c)      
    t.forward(50)
    t.left(90)
turtle.done()