import pygame
import math

from constants import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gravitational Slingshot')
clock = pygame.time.Clock()


def main():
    clock.tick(FPS)

    running = True

    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                temp_obj_pos = mouse_pos

        screen.blit(BACKGROUND, (0, 0))

        if temp_obj_pos:
            pygame.draw.circle(screen, RED, temp_obj_pos, OBJECT_SIZE)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
