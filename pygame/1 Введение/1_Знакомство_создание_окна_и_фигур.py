import pygame

pygame.init()

WIDTH = 800
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#set_mode аргументы: set_mode(size=(0, 0), flags=0, depth=0 (глубина цвета), display=0 (индекс дисплея))
# Это целое число, которое управляет свойствами и типом отображения окна. 
# Можно комбинировать несколько флагов с помощью побитового «ИЛИ» (символ |).
# • pygame.FULLSCREEN — включает полноэкранный режим.
# • pygame.RESIZABLE — позволяет пользователю изменять размер окна вручную.
# • pygame.NOFRAME — создает окно без рамки и кнопок управления («свернуть», «закрыть»).
# • pygame.SCALED — автоматически масштабирует разрешение под размеры экрана 
# (полезно для пиксель-арта).
# • pygame.HIDDEN — создает окно в скрытом режиме (появится только после вызова .show()).
# • pygame.OPENGL — подготавливает окно для работы с графикой OpenGL 
# вместо стандартного рендеринга Pygame.

pygame.display.set_caption("Моя первая игра")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    pygame.display.flip()

pygame.quit()

