import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(5)

# Спрашиваем высоту
tree_height = int(turtle.numinput("Лес", "Какой высоты дерево? (50-200)"))

# Рисуем ствол
t.pencolor("brown")
t.left(90)          # Смотрим вверх
t.forward(tree_height)

# Рисуем крону (круг)
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.right(90)         # Смотрим вправо
t.circle(tree_height / 2) # Размер кроны зависит от высоты ствола!
t.end_fill()

# Спускаемся обратно
t.left(90)          # Снова смотрим вверх
t.backward(tree_height) # Идем задом по стволу вниз

turtle.done()