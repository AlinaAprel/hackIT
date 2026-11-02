# Задача: Написать функцию, которая рисует здание (прямоугольник). 
# В функцию нужно передавать ширину, высоту и цвет. 
# Затем с помощью этой функции построить линию города.

import turtle

# Настройка фона
turtle.bgcolor("midnightblue") # Цвет ночного неба

t = turtle.Turtle()
t.speed(0)

# Функция для постройки здания
# Принимает 3 настройки: ширину (width), высоту (height) и цвет (color)
def draw_building(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    
    # Рисуем прямоугольник
    t.forward(width)     # Низ
    t.left(90)
    t.forward(height)    # Правая стена
    t.left(90)
    t.forward(width)     # Крыша
    t.left(90)
    t.forward(height)    # Левая стена
    t.left(90)           # Возвращаемся в исходное положение!
    
    t.end_fill()
    
    # Чтобы следующее здание рисовалось рядом, 
    # сдвигаем черепашку вправо на ширину только что построенного здания
    t.forward(width)

# --- СТРОИМ ГОРОД ---

# Идем в левый нижний угол экрана
t.penup()
t.goto(-250, -150)
t.pendown()
t.pensize(2)

# Вызываем функцию 5 раз с разными настройками!
draw_building(60, 200, "gray")
draw_building(40, 100, "darkgray")
draw_building(80, 250, "black")
draw_building(50, 150, "gray")
draw_building(70, 300, "darkgray")

turtle.done()