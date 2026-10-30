#Задание 1 (Легкое): "Цветомузыка"
#Сделайте так, чтобы каждый раз, когда мяч ударяется о любую стену, он менял цвет на случайный.
#Подсказка: Нужно импортировать библиотеку random в самом начале файла (import random) и создать переменную circle_color.

import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация: Полет")

BLACK = (0, 0, 0)
# Убираем переменную GREEN
circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


clock = pygame.time.Clock()
FPS = 60


circle_x = 400
circle_y = 300
circle_radius = 40 

speed_x = 5
speed_y = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    circle_x += speed_x  
    circle_y += speed_y


    if circle_x + circle_radius >= WIDTH or circle_x - circle_radius <= 0:
        speed_x = -speed_x
        # Меняем цвет на рандоме
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if circle_y + circle_radius >= HEIGHT or circle_y - circle_radius <= 0:
        speed_y = -speed_y
        # Меняем цвет на рандоме
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    screen.fill(BLACK)

    # Передаем аргумент
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()