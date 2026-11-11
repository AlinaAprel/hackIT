#Тема нейросети: Многоклассовая классификация (3 выходных нейрона-индикатора).
#Таймер: 150 секунд (2.5 минуты).
#Задание: Создать строковую переменную shape_type и с помощью цепочки
#  if - elif - else нарисовать нужную фигуру (круг, треугольник или квадрат).

import turtle
import random

screen = turtle.Screen()
screen.title("Уровень 4: Распознавание геометрических фигур")
screen.setup(700, 700)
screen.tracer(0)

artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()

seconds_left = 150  # Таймер: 2.5 минуты

# Веса для трех классов (0: Круг, 1: Треугольник, 2: Квадрат)
weights = [0.1, 0.1, 0.1]
lr = 0.1

def update_timer():
    global seconds_left
    hud.clear()
    hud.goto(0, 260)
    if seconds_left > 0:
        seconds_left -= 1
        hud.color("#b71c1c")
        hud.write(f"🧠 Глубокое обучение зрению: {seconds_left} сек.\nКлавиши: [C] - Круг | [T] - Треугольник | [S] - Квадрат", 
                  align="center", font=("Arial", 12, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        hud.color("#1b5e20")
        hud.write("🏆 2.5 МИНУТЫ ПРОШЛО! Нейросеть безошибочно чертит все 3 фигуры!", 
                  align="center", font=("Arial", 12, "bold"))
    screen.update()

def draw_circle():
    artist.fillcolor("cyan"); artist.begin_fill()
    artist.circle(45); artist.end_fill()

def draw_triangle():
    artist.fillcolor("orange"); artist.begin_fill()
    for _ in range(3): artist.forward(90); artist.left(120)
    artist.end_fill()

def draw_square():
    artist.fillcolor("pink"); artist.begin_fill()
    for _ in range(4): artist.forward(80); artist.left(90)
    artist.end_fill()

def classify_and_draw(target_id):
    global weights
    
    # Режим накопления данных (до истечения 2.5 минут)
    if seconds_left > 0:
        # Сеть путается из-за высокого уровня шума
        scores = [weights[i] + random.uniform(-0.8, 0.8) for i in range(3)]
        pred_id = scores.index(max(scores))
        # Обучение
        for i in range(3):
            err = (1 if i == target_id else 0) - (1 if i == pred_id else 0)
            weights[i] += err * lr
    else:
        # Сеть обучена и выбирает правильный класс
        pred_id = target_id

    artist.clear()
    artist.penup()
    artist.goto(-40, -40)
    artist.pendown()

    # =======================================================
    # ЗАДАНИЕ №4:
    # 1. Создай переменную shape_type.
    # 2. Напиши цепочку if - elif - else:
    #    Если pred_id == 0, то shape_type = "круг" и вызови draw_circle()
    #    Иначе если pred_id == 1, то shape_type = "треугольник" и вызови draw_triangle()
    #    Иначе shape_type = "квадрат" и вызови draw_square()
    # =======================================================
    # ТВОЙ КОД ЗДЕСЬ:

    # =======================================================

    artist.penup()
    artist.goto(0, -90)
    artist.color("black")
    artist.write(f"Распознано: {shape_type.upper()}", align="center", font=("Arial", 12, "bold"))
    screen.update()

screen.listen()
screen.onkey(lambda: classify_and_draw(0), "c")  # Circle
screen.onkey(lambda: classify_and_draw(1), "t")  # Triangle
screen.onkey(lambda: classify_and_draw(2), "s")  # Square

update_timer()
turtle.done()