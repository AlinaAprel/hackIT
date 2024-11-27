import turtle
import time
import random

# Настройки окна
window = turtle.Screen()
window.title("Змейка")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Голова змейки
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Еда для змейки
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Счет
score = 0  # Переменная для хранения текущего счета
high_score = 0  # Переменная для хранения высшего счета

# Отображение счета
score_display = turtle.Turtle()  # Создаем объект для отображения счета
score_display.speed(0)  # Устанавливаем скорость объекта
score_display.color("white")  # Устанавливаем цвет текста
score_display.penup()  # Отключаем рисование линий
score_display.hideturtle()  # Скрываем черепашку (объект) для отображения только текста
score_display.goto(0, 260)  # Устанавливаем позицию для отображения счета
score_display.write("Счет: 0  Высший счет: 0", align="center", font=("Courier", 24, "normal"))  # Начальное отображение счета

# Тело змейки
segments = []  # Список для хранения сегментов тела змейки

# Функции управления
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Управление с клавиатуры
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

# Основной цикл игры
while True:
    window.update()

    # Проверка столкновения с границами окна
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Удаление сегментов тела змейки после столкновения
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0  # Сбрасываем счет при столкновении
        score_display.clear()  # Очищаем предыдущий текст счета
        score_display.write("Счет: {}  Высший счет: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Обновляем отображение счета

    # Проверка столкновения с едой
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)  # Перемещаем еду на новую случайную позицию
        
        new_segment = turtle.Turtle()  # Создаем новый сегмент
        new_segment.speed(0)  # Устанавливаем скорость сегмента
        new_segment.shape("square")  # Устанавливаем форму сегмента
        new_segment.color("grey")  # Устанавливаем цвет сегмента
        new_segment.penup()  # Отключаем рисование линий
        segments.append(new_segment)  # Добавляем новый сегмент в список

        # Увеличиваем счет
        score += 10  # Увеличиваем текущий счет на 10
        if score > high_score:  # Если текущий счет больше высшего счета
            high_score = score  # Обновляем высший счет
        score_display.clear()  # Очищаем текст счета
        score_display.write("Счет: {}  Высший счет: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Обновляем отображение счета

    # Перемещение сегментов тела змейки
    for i in range(len(segments) - 1, 0, -1):  # Перемещаем каждый сегмент на место предыдущего
        x = segments[i - 1].xcor()  # Получаем X координату предыдущего сегмента
        y = segments[i - 1].ycor()  # Получаем Y координату предыдущего сегмента
        segments[i].goto(x, y)  # Перемещаем сегмент на место предыдущего

    if len(segments) > 0:  # Если есть хотя бы один сегмент
        x = head.xcor()  # Получаем текущую X координату головы
        y = head.ycor()  # Получаем текущую Y координату головы
        segments[0].goto(x, y)  # Перемещаем первый сегмент за головой

    move()

    # Проверка столкновения с собственным телом
    for segment in segments:
        if segment.distance(head) < 20:  # Если расстояние между головой и сегментом тела меньше 20 пикселей
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0  # Сбрасываем счет при столкновении с собственным телом
            score_display.clear()  # Очищаем предыдущий текст счета
            score_display.write("Счет: {}  Высший счет: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Обновляем отображение счета

    time.sleep(0.1)

window.mainloop()
