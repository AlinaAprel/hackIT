import turtle # Зовем Черепашку

t = turtle.Turtle()
t.shape("turtle")  # Делаем курсор похожим на настоящую черепашку 🐢
t.color("green")   # Цвет черепашки
t.width(5)         # Толщина линии

# Идем вперед
t.forward(100)
# Поворачиваем налево на 90 градусов
t.left(90)
# Идем вверх
t.forward(100)

turtle.done() # Чтобы окно не закрылось
