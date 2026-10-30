# Сделать так, чтобы игрок не мог выйти за пределы экрана.
#  Добавить кнопку "Спринт": если игрок зажимает левый Shift (pygame.K_LSHIFT), его скорость увеличивается в 2 раза.

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Управление: Спринт и Стены")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
FPS = 60

player_x = 400
player_y = 300
player_size = 50
normal_speed = 5  # Обычная скорость

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- РЕАЛИЗАЦИЯ СПРИНТА ---
    # Если зажат левый Shift, скорость = 10, иначе = 5
    if keys[pygame.K_LSHIFT]:
        current_speed = normal_speed * 2
    else:
        current_speed = normal_speed

    # --- УПРАВЛЕНИЕ С ГРАНИЦАМИ ---
    # Идем влево, только если X больше 0
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= current_speed
        
    # Идем вправо, только если X + ширина игрока меньше ширины окна
    if keys[pygame.K_RIGHT] and player_x + player_size < WIDTH:
        player_x += current_speed
        
    # Идем вверх, только если Y больше 0
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= current_speed
        
    # Идем вниз, только если Y + высота игрока меньше высоты окна
    if keys[pygame.K_DOWN] and player_y + player_size < HEIGHT:
        player_y += current_speed

    screen.fill(BLACK)
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()