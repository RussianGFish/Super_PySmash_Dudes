# Import Libaries
import pygame
import os

# Colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

# Setting Screen/Player Variables
p1x = 0
p1y = 0
screen_x = 1280
screen_y = 640

# Initialization Commands
running = True
player_dir = 0
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption('Super Python Bros.')

# Classes


class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([750, 100])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()


class Brawler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
       self.rect.x += p1x
       self.rect.y += p1y


# Adding sprites to group
platform = Platforms()
platform.rect.x = 200
platform.rect.y = 350

brawler = Brawler()
brawler.rect.x = 500
brawler.rect.y = 200

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
all_sprites.add(brawler)
all_sprites.add(platform)

# Event Tracker
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1y -= 4
            elif event.key == pygame.K_s:
                p1y += 4
            elif event.key == pygame.K_a:
                p1x -= 4
            elif event.key == pygame.K_d:
                p1x += 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1y = 0
            elif event.key == pygame.K_s:
                p1y = 0
            elif event.key == pygame.K_a:
                p1x = 0
            elif event.key == pygame.K_d:
                p1x = 0

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
