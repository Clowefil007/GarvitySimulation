import pygame


# screen
WIDTH = 1000
HEIGHT = 800
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLANET_MASS = 100
ROCK_MASS = 5
G = 6.674
PLANET_SIZE = 50
ROCK_SIZE = 5
VEL_SCALE = 100

# images
BACKGROUND = pygame.transform.scale(pygame.image.load('images/background.png'), (WIDTH, HEIGHT))
SATURN = pygame.transform.scale(pygame.image.load('images/jupiter.jpg'), (PLANET_SIZE*2, PLANET_SIZE*2))
