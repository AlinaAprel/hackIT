# Задание: Создать корабль игрока, который двигается только влево и вправо по низу экрана. 
# Создать список из 7 метеоритов, которые падают сверху вниз.

import pygame
import random

pygame.init()

# Для шутеров часто делают вертикальные окна, как на телефоне или игровом автомате
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космический Шутер")
clock = pygame.time.Clock()

# --- 1. ЗАГРУЗКА КАРТИНОК ---
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (60, 60))
meteor_img = pygame.transform.scale(pygame.image.load("meteor.png"), (50, 50))

# --- 2. НАСТРОЙКА ИГРОКА ---
player_x = WIDTH // 2 - 30  # Ставим по центру экрана
player_y = HEIGHT - 100     # Ставим в самом низу
player_speed = 7

# --- 3. НАСТРОЙКА МЕТЕОРИТОВ (СПИСОК) ---
meteors = []  # Пустой список для хитбоксов метеоритов
meteor_speed = 5

# Создаем 7 метеоритов перед началом игры
for i in range(7):
    # Генерируем случайные координаты. 
    # y делаем отрицательным, чтобы они падали из-за пределов экрана!
    m_x = random.randint(0, WIDTH - 50)
    m_y = random.randint(-500, -50)
    
    # Создаем хитбокс и кладем его в список
    meteor_rect = pygame.Rect(m_x, m_y, 50, 50)
    meteors.append(meteor_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- УПРАВЛЕНИЕ ИГРОКОМ (только влево/вправо) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 60:
        player_x += player_speed

    # --- ЛОГИКА МЕТЕОРИТОВ ---
    # Перебираем все метеориты в списке по очереди
    for m in meteors:
        m.y += meteor_speed  # Двигаем каждый метеорит ВНИЗ

    # --- ОТРИСОВКА ---
    screen.blit(bg, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    
    # Рисуем все метеориты из списка
    for m in meteors:
        screen.blit(meteor_img, (m.x, m.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

