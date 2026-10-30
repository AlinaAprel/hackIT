#Добавьте в игру второй мяч. У него должны быть свои координаты (например, x2, y2), свой цвет, свой размер и свои, другие скорости 
# (например, speed_x2 = -7, speed_y2 = 4). Оба мяча должны летать одновременно и отскакивать от стен.

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация: Два мяча")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

clock = pygame.time.Clock()
FPS = 60

# --- ПЕРЕМЕННЫЕ ПЕРВОГО МЯЧА (Красный) ---
x1 = 200
y1 = 300
radius1 = 40
speed_x1 = 5
speed_y1 = 5

# --- ПЕРЕМЕННЫЕ ВТОРОГО МЯЧА (Синий) ---
x2 = 600
y2 = 150
radius2 = 25
speed_x2 = -7  # Летит в другую сторону и быстрее
speed_y2 = 3

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ
    
    # --- Логика ПЕРВОГО мяча ---
    x1 += speed_x1
    y1 += speed_y1

    if x1 + radius1 >= WIDTH or x1 - radius1 <= 0:
        speed_x1 = -speed_x1
    if y1 + radius1 >= HEIGHT or y1 - radius1 <= 0:
        speed_y1 = -speed_y1

    # --- Логика ВТОРОГО мяча ---
    x2 += speed_x2
    y2 += speed_y2

    if x2 + radius2 >= WIDTH or x2 - radius2 <= 0:
        speed_x2 = -speed_x2
    if y2 + radius2 >= HEIGHT or y2 - radius2 <= 0:
        speed_y2 = -speed_y2

    # 3. ОТРИСОВКА
    screen.fill(BLACK)
    
    # Рисуем первый мяч
    pygame.draw.circle(screen, RED, (x1, y1), radius1)
    
    # Рисуем второй мяч
    pygame.draw.circle(screen, BLUE, (x2, y2), radius2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()