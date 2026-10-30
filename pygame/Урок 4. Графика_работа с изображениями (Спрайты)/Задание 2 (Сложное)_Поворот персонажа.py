#Проблема: когда мы идем влево, персонаж часто продолжает смотреть вправо (идет спиной).
#Решение: использовать pygame.transform.flip(картинка, по_горизонтали, по_вертикали).

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bg_image = pygame.image.load("images/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (800, 600))

# Загружаем базовую картинку (смотрит вправо)
player_img_right = pygame.image.load("images/pers.png")
player_img_right = pygame.transform.scale(player_img_right, (80, 80))

# Создаем копию картинки, отраженную по горизонтали (True), но не по вертикали (False)
player_img_left = pygame.transform.flip(player_img_right, True, False)

# Текущая картинка, которую мы будем рисовать (по умолчанию смотрит вправо)
current_player_img = player_img_right

player_x = 400
player_y = 300
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        current_player_img = player_img_left  # Меняем картинку!
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        current_player_img = player_img_right # Меняем картинку!
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    screen.blit(bg_image, (0, 0))
    # Рисуем текущую выбранную картинку
    screen.blit(current_player_img, (player_x, player_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()