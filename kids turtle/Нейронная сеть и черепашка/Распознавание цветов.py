#Тема нейросети: Обучение перцептрона с одним входом и весом.
#Таймер: 60 секунд. Пока таймер идет, нейросеть «маленькая» 
# и делает случайные ошибки. После 1 минуты накопленные знания активируются.
#Задание: Создать переменную для целевого цвета 
# и через if-else определить сигнал нейросети.

import turtle
import random

screen = turtle.Screen()
screen.title("Уровень 1: Распознавание цветов")
screen.setup(600, 600)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
info_t = turtle.Turtle()
info_t.hideturtle()

# Параметры нейросети
weight = 0.05
lr = 0.2
seconds_left = 60  # Таймер: 1 минута

def update_timer():
    global seconds_left
    info_t.clear()
    info_t.penup()
    info_t.goto(0, 220)
    if seconds_left > 0:
        seconds_left -= 1
        info_t.color("darkred")
        info_t.write(f"🧠 Сбор опыта: осталось {seconds_left} сек.\nНажимай 'G' (зеленый) и 'Y' (желтый)!", 
                     align="center", font=("Arial", 14, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        info_t.color("darkgreen")
        info_t.write("🎉 1 МИНУТА ПРОШЛА! Нейросеть обучена и готова!", 
                     align="center", font=("Arial", 14, "bold"))
    screen.update()

def draw_circle(color):
    t.clear()
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    screen.update()

def process_color(key_pressed):
    global weight

    # =======================================================
    # ЗАДАНИЕ №1:
    # 1. Создай переменную target_signal и target_color.
    # 2. С помощью if-else проверь:
    #    Если key_pressed == "g", то target_signal = 1, а target_color = "green"
    #    Иначе target_signal = -1, а target_color = "yellow"
    # =======================================================
    # ТВОЙ КОД ЗДЕСЬ:
    # =======================================================

    # Пока идет минута — нейросеть иногда ошибается (учится)
    if seconds_left > 0:
        prediction = 1 if (target_signal * weight + random.uniform(-0.5, 0.5)) > 0 else -1
        weight += (target_signal - prediction) * lr
    else:
        prediction = 1 if (target_signal * weight) > 0 else -1

    # Показываем результат предсказания сети
    result_color = "green" if prediction == 1 else "yellow"
    draw_circle(result_color)

screen.listen()
screen.onkey(lambda: process_color("g"), "g")
screen.onkey(lambda: process_color("g"), "G")
screen.onkey(lambda: process_color("y"), "y")
screen.onkey(lambda: process_color("y"), "Y")

draw_circle("gray")
update_timer()
turtle.done()