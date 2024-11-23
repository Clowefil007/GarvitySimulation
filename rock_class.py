import pygame

from constants import *


class Rock:
    def __init__(self, screen, x, y, vel_x, vel_y, size, mass):
        self.screen = screen
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.size = size
        self.mass = mass
        self.obj = pygame.transform.scale(pygame.image.load('images/rock.png'), (self.size*2, self.size*2)).convert_alpha()
    
    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    
    def draw(self):
        self.screen.blit(self.obj, (self.x-self.size, self.y-self.size))