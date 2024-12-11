import pygame
import random

# Константы
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 100
GRID_ROWS = 5
GRID_COLS = 8
PLANT_COST = 50
ZOMBIE_HEALTH = 100
PLANT_DAMAGE = 10
SUN_GAIN = 25
FPS = 60

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs Zombies")
clock = pygame.time.Clock()

# Загрузка изображений
plant_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
plant_img.fill(GREEN)

zombie_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
zombie_img.fill(RED)

# Классы
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = plant_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.damage = PLANT_DAMAGE

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = zombie_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = ZOMBIE_HEALTH
        self.speed = 1

    def update(self):
        self.rect.x -= self.speed

class Game:
    def __init__(self):
        self.plants = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.sun = 100
        self.round_timer = 0
        self.running = True

    def spawn_zombie(self):
        row = random.randint(0, GRID_ROWS - 1)
        x = WIDTH - CELL_SIZE
        y = row * CELL_SIZE
        zombie = Zombie(x, y)
        self.zombies.add(zombie)

    def place_plant(self, x, y):
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        grid_x = col * CELL_SIZE
        grid_y = row * CELL_SIZE
        if self.sun >= PLANT_COST:
            plant = Plant(grid_x, grid_y)
            self.plants.add(plant)
            self.sun -= PLANT_COST

    def plants_attack(self):
        for plant in self.plants:
            for zombie in self.zombies:
                if plant.rect.y == zombie.rect.y and plant.rect.x < zombie.rect.x <= plant.rect.x + 200:
                    zombie.health -= plant.damage
                    if zombie.health <= 0:
                        zombie.kill()

    def update(self):
        self.zombies.update()
        self.plants_attack()
        self.round_timer += 1
        if self.round_timer % (FPS * 2) == 0:  # Зомби появляются каждые 2 секунды
            self.spawn_zombie()
        self.sun += SUN_GAIN // FPS  # Медленно добавляем солнце

    def draw(self):
        screen.fill(WHITE)
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLUE, rect, 1)
        self.plants.draw(screen)
        self.zombies.draw(screen)

        # Отображение ресурсов
        font = pygame.font.SysFont(None, 36)
        sun_text = font.render(f"Sun: {self.sun}", True, (0, 0, 0))
        screen.blit(sun_text, (10, 10))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # ЛКМ
                        x, y = event.pos
                        self.place_plant(x, y)

            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(FPS)

# Основной запуск
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
