# Задача: Вернись к коду из Задания 1 (где мы управляем одной черепашкой во все стороны). 
# Добавь 3 функции: одна меняет цвет черепашки на красный, другая на синий, 
# третья на зеленый. Привяжи их к кнопкам 1, 2 и 3 на клавиатуре.

def color_red():
    t.color("red")

def color_blue():
    t.color("blue")

def color_green():
    t.color("green")

# ... в настройках кнопок:
turtle.onkeypress(color_red, "1")
turtle.onkeypress(color_blue, "2")
turtle.onkeypress(color_green, "3")