import   # Библиотека для случайных чисел
import turtle

# 1. Настройка экрана
screen = turtle.Screen()
screen.title("Поймай точку!")
screen.bgcolor("")  # Черный фон, как в настоящей аркаде

# 2. Создание черепашки-игрока
player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.pensize(3)
player.speed()  # Максимальная скорость движения

# 3. Создание «цели» (монетки)
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(, ), random.randint(, ))


# 4. Функция движения: что происходит, когда мы кликаем мышкой по экрану
def move_turtle(x, y):
    player.goto(x, y)  # Черепашка бежит туда, куда кликнули мышкой

    # Проверяем: если черепашка подошла близко к цели (монетке)
    if player.distance(target) < 20:
        # Прячем монетку и переносим её в новое случайное место
        target.hideturtle()
        target.goto(random.randint(, ), random.randint(, ))
        target.showturtle()


# 5. Связываем клик мышки по экрану с нашей функцией
screen.onclick(move_turtle)

# Оставляем окно открытым
screen.mainloop()