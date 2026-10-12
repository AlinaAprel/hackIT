import pygame

pygame.init()

WIDTH = 800
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя первая игра")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
PINK = (231,157,157)
GREEN = (204,231,157)
VIOLET = (85,30,194)
HOUSE_COLOR = (255, 228, 196)  # Бежевый цвет
YELLOW = (255, 255, 0)  # Желтый цвет
ROOF_COLOR = (205, 92, 92)  # Красный цвет

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    pygame.draw.rect(screen, HOUSE_COLOR, (300, 250, 150, 150))
    pygame.draw.rect(screen, YELLOW, (340, 290, 70, 70))
    pygame.draw.polygon(screen, ROOF_COLOR, [(280, 250), (470, 250), (375, 150)])
    pygame.display.flip()

pygame.quit()

