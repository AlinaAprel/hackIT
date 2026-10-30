#Задание: Создать круг, который будет бесконечно лететь вправо по диагонали, пока не улетит за границы окна.

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация: Полет")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# --- НОВЫЙ БЛОК: Настройка времени ---
clock = pygame.time.Clock()  # Создаем "часы" для контроля времени
FPS = 60  # Задаем желаемую частоту кадров (60 кадров в секунду)

# --- НОВЫЙ БЛОК: Переменные объекта ---
# Задаем начальные координаты круга (в центре экрана)
circle_x = 400
circle_y = 300
circle_radius = 40  # Радиус круга

# Задаем скорость движения (на сколько пикселей сдвигаемся за 1 кадр)
speed_x = 5  # Скорость по горизонтали (вправо)
speed_y = 3  # Скорость по вертикали (вниз)

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ (Физика игры)
    # Изменяем координаты на величину скорости в каждом кадре
    circle_x = circle_x + speed_x  
    circle_y = circle_y + speed_y  

    # 3. ОТРИСОВКА
    screen.fill(BLACK)  # Очищаем экран (попробуйте закомментировать эту строку и посмотреть, что будет!)
    
    # Рисуем круг по переменным координатам, а не по фиксированным цифрам
    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), circle_radius)

    pygame.display.flip()  # Обновляем экран
    
    # --- НОВЫЙ БЛОК: Контроль FPS ---
    clock.tick(FPS)  # Просим цикл ждать, чтобы выдавать ровно 60 кадров в секунду

pygame.quit()