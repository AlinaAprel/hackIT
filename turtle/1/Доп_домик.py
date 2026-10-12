import turtle
t = turtle.Turtle()
t.shape("turtle")

# Рисуем основу (квадрат)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Переходим к рисованию крыши (черепашка смотрит вправо)
t.left(90)     # Поворачиваем вверх
t.forward(100) # Поднимаемся на крышу (в левый верхний угол)
t.right(90)    # Снова смотрим вправо

# Рисуем крышу (треугольник)
t.left(60)     # Угол наклона левого ската крыши
t.forward(100)
t.right(120)   # Острый угол крыши
t.forward(100)

turtle.done()