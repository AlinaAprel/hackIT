#Проблема: Круг улетел и не вернулся. Как сделать скринсейвер (как в старых DVD-плеерах), чтобы он отталкивался от стен?
#Решение: Использовать условия if. Если координата Х стала больше ширины экрана, нужно изменить направление скорости (speed_x = -speed_x).
#Задание: Дописать логику отскока от всех четырех стен в предыдущий код.

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация: Полет")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

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

    # Сокращаем запись
    circle_x += speed_x  
    circle_y += speed_y

    # Проверка столкновения с ПРАВЫМ И ЛЕВЫМ краями экрана
    # Если x + радиус > ширины (улетели вправо) ИЛИ x - радиус < 0 (улетели влево)
    if circle_x + circle_radius >= WIDTH or circle_x - circle_radius <= 0:
        speed_x = -speed_x  # Инвертируем скорость (была 5, стала -5; была -5, стала 5)

    # Проверка столкновения с НИЖНИМ И ВЕРХНИМ краями экрана
    # Если y + радиус > высоты (упали вниз) ИЛИ y - радиус < 0 (улетели вверх)
    if circle_y + circle_radius >= HEIGHT or circle_y - circle_radius <= 0:
        speed_y = -speed_y  # Инвертируем скорость по вертикали

    screen.fill(BLACK)
    
    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), circle_radius)

    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()