#Задание: Игрок бегает по экрану. В случайном месте лежит монетка.
#  Если игрок касается монетки, она исчезает и появляется в новом случайном месте.

#Задание 1 (Легкое): Подсчет очков в консоли
#Добавьте переменную score = 0 перед циклом while. 
# Каждый раз, когда игрок собирает монетку, увеличивайте score на 1 и выводите его через print(f"Счет: {score}").
#Задание 2 (Среднее): Враг-Шип (Ядовитый предмет)
#Добавьте еще одну картинку (например, spike.png или bomb.png). 
# Задайте для нее свои координаты. Если игрок касается бомбы:
#Очки (score) уменьшаются на 1.
#Бомба телепортируется в другое случайное место, как и монетка.
#Смысл в том, чтобы дети сами создали еще один хитбокс bomb_rect и написали еще один if.

import pygame
import random  # Понадобится для случайных координат монетки

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Урок 5: Коллизии")

clock = pygame.time.Clock()
FPS = 60

# Загружаем картинки (фон, игрок, монетка)
bg = pygame.transform.scale(pygame.image.load("images/bg.jpg"), (WIDTH, HEIGHT))

player_img = pygame.transform.scale(pygame.image.load("images/pers.png"), (80, 80))
player_x = 400
player_y = 300
player_speed = 6

coin_img = pygame.transform.scale(pygame.image.load("images/coin.png"), (40, 40))
# Монетка спавнится в случайных координатах (с отступом от краев)
coin_x = random.randint(50, 700)
coin_y = random.randint(50, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. УПРАВЛЕНИЕ ИГРОКОМ
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_DOWN]: player_y += player_speed

    # 2. ЛОГИКА СТОЛКНОВЕНИЙ (КОЛЛИЗИИ)
    # Создаем виртуальные невидимые коробки (хитбоксы) там же, где сейчас картинки
    # pygame.Rect(x, y, ширина_картинки, высота_картинки)
    player_rect = pygame.Rect(player_x, player_y, 80, 80)
    coin_rect = pygame.Rect(coin_x, coin_y, 40, 40)

    # Проверяем пересечение двух коробок
    if player_rect.colliderect(coin_rect):
        # Если коснулись - меняем координаты монетки на новые (телепортируем ее)
        coin_x = random.randint(50, 700)
        coin_y = random.randint(50, 500)
        print("Монетка собрана!") # Пока выводим текст в консоль (текст на экране будет в Уроке 6)

    # 3. ОТРИСОВКА
    screen.blit(bg, (0, 0))
    screen.blit(coin_img, (coin_x, coin_y))  # Монетку рисуем первой (чтобы она лежала "на земле")
    screen.blit(player_img, (player_x, player_y)) # Игрока рисуем поверх монетки

    # *Для отладки: можно раскомментировать строки ниже, чтобы ДЕТИ УВИДЕЛИ ХИТБОКСЫ*
    pygame.draw.rect(screen, (255,0,0), player_rect, 2) 
    pygame.draw.rect(screen, (0,255,0), coin_rect, 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()