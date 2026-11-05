import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("gold")

dlina = 20 # Стартовая длина

for i in range(40):
    t.forward(dlina)
    t.right(144)      # Угол звезды
    dlina = dlina + 10 # Линия растет

turtle.done()