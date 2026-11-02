#Задача: Написать функцию draw_house(), которая рисует домик (квадрат + крыша). 
# Затем с помощью цикла и телепортации построить целую улицу из таких домов.

import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("lightgreen")

# --- УЧИМ ЧЕРЕПАШКУ СТРОИТЬ ДОМ ---
def draw_house():
    # 1. Рисуем фасад (квадрат)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()
    
    # 2. Переходим к крыше
    t.left(90)
    t.forward(60)
    t.right(90)
    
    # 3. Рисуем крышу (треугольник)
    t.fillcolor("red")
    t.begin_fill()
    t.left(60)
    t.forward(60)
    t.right(120)
    t.forward(60)
    t.right(30) # Выравниваем черепашку, чтобы она смотрела прямо (вниз)
    t.end_fill()
    
    # 4. Спускаемся на землю (возвращаемся в начальную точку!)
    # Это очень важное правило хорошего тона для функций
    t.penup()
    t.forward(60)
    t.left(90)
    t.pendown()

# --- СТРОИМ УЛИЦУ ---
# Передвигаем черепашку в левый край экрана, чтобы поместились все дома
t.penup()
t.goto(-200, 0)
t.pendown()

# Строим 4 дома в ряд
for i in range(4):
    draw_house()       # Строим дом
    
    t.penup()
    t.forward(100)     # Отходим вправо на 100 шагов (ширина дома 60 + отступ 40)
    t.pendown()

turtle.done()
