import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("black")
turtle.bgcolor("lightblue") # Цвет фона для красоты

line_length = 5

for i in range(80): # 80 линий паутины
    t.forward(line_length)
    t.left(59)               # Угол чуть меньше 60 дает эффект смещения!
    line_length = line_length + 4 # Увеличиваем размер

turtle.done()