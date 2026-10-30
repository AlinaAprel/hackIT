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

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    pygame.draw.rect(screen, PINK, (100, 100, 200, 400))
    pygame.draw.circle(screen, GREEN, (100, 100), 50)
    pygame.draw.line(screen, VIOLET, (0, 900), (800, 500), 20)
    pygame.display.flip()

pygame.quit()

