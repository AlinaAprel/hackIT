#Задание: Загрузить картинку фона (на весь экран) и картинку персонажа, которым можно управлять с клавиатуры.
#Задание 1 (Легкое): Декорации
#Скачайте еще одну картинку (например, дерево или камень stone.png). 
#Загрузите её, уменьшите и нарисуйте с помощью blit в статичных координатах (например, 200, 200),
#  чтобы она была частью уровня.

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Урок 4: Спрайты")

clock = pygame.time.Clock()
FPS = 60

# --- 1. ЗАГРУЗКА И НАСТРОЙКА КАРТИНОК ---
# Загружаем фон и подгоняем его под размер окна
bg_image = pygame.image.load("images/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Загружаем персонажа и делаем его размером 80x80
player_image = pygame.image.load("images/pers.png")
player_image = pygame.transform.scale(player_image, (80, 80))

# Переменные для координат персонажа
player_x = 400
player_y = 300
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- УПРАВЛЕНИЕ ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # --- ОТРИСОВКА ---
    # ВАЖНО: Сначала рисуем фон! Он заменит нам screen.fill(BLACK)
    # Фон рисуем в координатах (0, 0) - с левого верхнего угла
    screen.blit(bg_image, (0, 0))
    
    # Теперь рисуем персонажа ПОВЕРХ фона
    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()