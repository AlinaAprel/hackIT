#Сделать простую "Зомби-монетку". Предмет (или отдельный враг enemy) каждый кадр медленно двигается в сторону игрока.
#  Если он догоняет игрока — игра заканчивается (выход из цикла) или игрок возвращается в центр.

import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("images/bg.jpg"), (WIDTH, HEIGHT))

# Игрок
player_img = pygame.transform.scale(pygame.image.load("images/pers.png"), (80, 80))
player_x, player_y = 400, 300
player_speed = 6

# Враг (загрузите картинку enemy.png или используйте ту же монетку)
enemy_img = pygame.transform.scale(pygame.image.load("images/coin.png"), (60, 60))
enemy_x, enemy_y = 100, 100
enemy_speed = 2  # Враг медленнее игрока!

score = 0 # Из Задания 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Управление игроком ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_DOWN]: player_y += player_speed

    # --- ИИ (Искусственный Интеллект) Врага ---
    # Враг сравнивает свои координаты с координатами игрока и делает шаг к нему
    if enemy_x < player_x:
        enemy_x += enemy_speed
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed

    # --- КОЛЛИЗИИ ---
    player_rect = pygame.Rect(player_x, player_y, 80, 80)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 60, 60)

    # Если враг догнал
    if player_rect.colliderect(enemy_rect):
        print("ПОТРАЧЕНО! Враг вас съел.")
        # Телепортируем игрока обратно в центр
        player_x, player_y = 400, 300
        # Врага отбрасываем в угол
        enemy_x, enemy_y = 50, 50

    # --- Отрисовка ---
    screen.blit(bg, (0, 0))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    screen.blit(player_img, (player_x, player_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()