#Измените круг на прямоугольник. Размеры прямоугольника, например, 100 на 60. Настройте отскок так, чтобы прямоугольник отскакивал ровно своими гранями.
#Подсказка: Для прямоугольника координаты x и y — это его левый верхний угол, а не центр!

import pygame
import random  # Подключаем библиотеку для случайных чисел (для смены цвета)

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация: DVD-логотип")

BLACK = (0, 0, 0)
# Начальный цвет прямоугольника
rect_color = (0, 255, 0) 

clock = pygame.time.Clock()
FPS = 60

# --- ПЕРЕМЕННЫЕ ПРЯМОУГОЛЬНИКА ---
rect_width = 100  # Ширина
rect_height = 60  # Высота

# Начальные координаты (левый верхний угол)
rect_x = 350
rect_y = 270

# Скорость прямоугольника
speed_x = 4
speed_y = 4

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ
    # Двигаем прямоугольник
    rect_x += speed_x
    rect_y += speed_y

    # --- ОТСКОК ПО ГОРИЗОНТАЛИ ---
    # Проверяем правый край (x + ширина) И левый край (просто x)
    if rect_x + rect_width >= WIDTH or rect_x <= 0:
        speed_x = -speed_x  # Меняем направление
        # Меняем цвет на случайный при ударе
        rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # --- ОТСКОК ПО ВЕРТИКАЛИ ---
    # Проверяем нижний край (y + высота) И верхний край (просто y)
    if rect_y + rect_height >= HEIGHT or rect_y <= 0:
        speed_y = -speed_y  # Меняем направление
        # Меняем цвет на случайный при ударе
        rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 3. ОТРИСОВКА
    screen.fill(BLACK)
    
    # Рисуем прямоугольник с нашими переменными
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()