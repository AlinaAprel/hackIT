#Тема нейросети: Определение знака перемещения.
#Таймер: 90 секунд (1.5 минуты).
#Задание: Создать переменную шага step_distance 
# и с помощью if-else заставить черепашку идти вперед 
# или назад в зависимости от ответа сети.

import turtle
import random

screen = turtle.Screen()
screen.title("Уровень 2: Направление движения")
screen.setup(650, 600)

car = turtle.Turtle()
car.shape("turtle")
car.color("blue")
car.shapesize(2)
car.penup()

ui = turtle.Turtle()
ui.hideturtle()
ui.penup()

seconds_left = 90  # Таймер: 1.5 минуты
weight = 0.01
lr = 0.15

def update_timer():
    global seconds_left
    ui.clear()
    ui.goto(0, 230)
    if seconds_left > 0:
        seconds_left -= 1
        ui.color("red")
        ui.write(f"⏱ Обучение навигатору: осталось {seconds_left} сек.\nКлавиша ВВЕРХ (Вперед) | Клавиша ВНИЗ (Назад)", 
                 align="center", font=("Arial", 12, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        ui.color("green")
        ui.write("🚀 1.5 МИНУТЫ ПРОШЛО! Нейросеть безошибочно ведет черепашку!", 
                 align="center", font=("Arial", 12, "bold"))

def move_turtle(command):
    global weight
    
    # 1 - ехать вперед, -1 - ехать назад
    target = 1 if command == "up" else -1
    
    # Обучение перцептрона
    if seconds_left > 0:
        noise = random.uniform(-0.6, 0.6)
        guess = 1 if (target * weight + noise) >= 0 else -1
        weight += (target - guess) * lr
    else:
        guess = 1 if (target * weight) >= 0 else -1

    # =======================================================
    # ЗАДАНИЕ ДЛЯ УЧЕНИКА №2:
    # 1. Создай переменную step_distance.
    # 2. Напиши конструкцию if-else:
    #    Если ответ сети (переменная guess) равен 1, то step_distance = 40
    #    Иначе step_distance = -40
    # 3. Перемести черепашку командой car.forward(step_distance)
    # =======================================================
    # ТВОЙ КОД ЗДЕСЬ:

    # =======================================================

    # Если черепаха уползла за экран — возвращаем
    if abs(car.xcor()) > 280 or abs(car.ycor()) > 220:
        car.goto(0, 0)

screen.listen()
screen.onkey(lambda: move_turtle("up"), "Up")
screen.onkey(lambda: move_turtle("down"), "Down")

update_timer()
turtle.done()