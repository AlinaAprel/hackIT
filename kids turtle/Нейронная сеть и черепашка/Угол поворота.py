#Тема нейросети: Определение угла маневра по расстоянию до сенсора
#  (2 входа: сигнал препятствия + смещение bias).
#Таймер: 120 секунд (2 минуты).
#Задание: Создать переменную turn_angle и через if-else повернуть черепашку 
# на угол 45° (плавный поворот) или 90° (резкий поворот).

import turtle
import random

screen = turtle.Screen()
screen.title("Уровень 3: Умный угол поворота")
screen.setup(700, 650)
screen.tracer(0)

bot = turtle.Turtle()
bot.shape("triangle")
bot.color("purple")
bot.pensize(2)
bot.shapesize(1.5)

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()

seconds_left = 120  # Таймер: 2 минуты
w_dist = random.uniform(-0.1, 0.1)
bias = 0.0
lr = 0.08

def update_timer():
    global seconds_left
    hud.clear()
    hud.goto(0, 240)
    if seconds_left > 0:
        seconds_left -= 1
        hud.color("darkorange")
        hud.write(f"⏳ Калибровка гироскопа: {seconds_left} сек.\nЖми '1' (Резкий угол 90°) | '2' (Плавный угол 45°)", 
                  align="center", font=("Arial", 12, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        hud.color("darkgreen")
        hud.write("🎯 2 МИНУТЫ ПРОШЛО! Автопилот углов откалиброван!", 
                  align="center", font=("Arial", 12, "bold"))
    screen.update()

def make_turn(mode):
    global w_dist, bias
    # Режим 1: Резкий (вход 1.0, цель 1), Режим 2: Плавный (вход 0.2, цель -1)
    sensor_input = 1.0 if mode == 1 else 0.2
    target = 1 if mode == 1 else -1

    # Вычисление выхода сети
    if seconds_left > 0:
        pred_val = sensor_input * w_dist + bias + random.uniform(-0.4, 0.4)
        guess = 1 if pred_val >= 0 else -1
        err = target - guess
        w_dist += err * sensor_input * lr
        bias += err * lr
    else:
        guess = 1 if (sensor_input * w_dist + bias) >= 0 else -1

    # =======================================================
    # ЗАДАНИЕ №3:
    # 1. Создай переменную turn_angle.
    # 2. Напиши условие if-else:
    #    Если guess == 1, то turn_angle = 90
    #    Иначе turn_angle = 45
    # 3. Поверни бота bot.left(turn_angle) и сделай шаг bot.forward(50)
    # =======================================================
    # ТВОЙ КОД ЗДЕСЬ:

    # =======================================================

    # Ограничение рабочей зоны
    if abs(bot.xcor()) > 300 or abs(bot.ycor()) > 230:
        bot.penup()
        bot.goto(0, 0)
        bot.pendown()
    screen.update()

screen.listen()
screen.onkey(lambda: make_turn(1), "1")
screen.onkey(lambda: make_turn(2), "2")

update_timer()
turtle.done()