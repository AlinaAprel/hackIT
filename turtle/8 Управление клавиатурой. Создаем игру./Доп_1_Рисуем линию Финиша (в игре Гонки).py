# Задача: В коде из Задания 3, перед тем как создавать игроков, создай третью черепашку-судью. 
# Пусть она нарисует вертикальную белую линию на координате X = 200 (это будет финиш), 
# а затем спрячется (команда hideturtle()).

import turtle

# Настройка экрана
turtle.bgcolor("sandybrown")

# 1. СОЗДАЕМ ИГРОКА 1 (Красный)
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("red")
p1.shapesize(2)      # Делаем черепашку побольше
p1.penup()
p1.goto(-200, 50)    # Ставим на линию старта (чуть выше центра)

# 2. СОЗДАЕМ ИГРОКА 2 (Синий)
p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("blue")
p2.shapesize(2)
p2.penup()
p2.goto(-200, -50)   # Ставим на линию старта (чуть ниже центра)

# Судья рисует финиш
referee = turtle.Turtle()
referee.speed(0)
referee.penup()
referee.goto(200, 150)
referee.pendown()
referee.pensize(5)
referee.color("white")
referee.goto(200, -150) # Рисует линию сверху вниз
referee.hideturtle()    # Прячем судью, чтобы не мешался

# 3. ФУНКЦИИ ДЛЯ ШАГА (Двигаются только вперед)
def p1_move():
    p1.forward(15)

def p2_move():
    p2.forward(15)

# 4. НАСТРОЙКА КЛАВИАТУРЫ
turtle.listen()

# Игрок 1 жмет английскую 'd'
turtle.onkeypress(p1_move, "d") 

# Игрок 2 жмет стрелку 'Вправо'
turtle.onkeypress(p2_move, "Right")

turtle.done()