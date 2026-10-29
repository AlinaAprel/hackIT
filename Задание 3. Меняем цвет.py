import turtle

t = turtle.Turtle()
t.speed(3)

# Сделайте так, чтобы перед каждым шагом черепашка меняла цвет!

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()