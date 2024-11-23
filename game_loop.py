import pygame
import math

import rock_class

from constants import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot")
clock = pygame.time.Clock()

pygame.mouse.set_visible(True)


def main():
    clock.tick(FPS)
    time = 0

    mouse_down = False

    running = True

    tmp_rock = None
    tmp_rock_size = ROCK_SIZE
    tmp_rock_mass = ROCK_MASS
    rocks = []
    tmp_rock_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                rock = rock_class.Rock(screen,t_x,t_y,1,0,tmp_rock_size,tmp_rock_mass)
                rocks.append(rock)
                mouse_down = False
                time = 0
                tmp_rock = None
                tmp_rock_size = ROCK_SIZE
                tmp_rock_mass = ROCK_MASS
                tmp_rock_pos = None
        

        if mouse_down:
            time += 1
            if time%4 == 0 and tmp_rock_pos == mouse_pos:
                tmp_rock_size += 1
                tmp_rock_mass += 1

            if tmp_rock_pos:
                t_x, t_y = tmp_rock_pos
                tmp_rock = rock_class.Rock(screen,t_x,t_y,0,0,tmp_rock_size,tmp_rock_mass)
            else:
                tmp_rock_pos = mouse_pos


        screen.blit(BACKGROUND, (0, 0))

        if tmp_rock:
            pygame.draw.line(screen, WHITE, tmp_rock_pos, mouse_pos, 2)
            tmp_rock.draw()

        for rock in rocks:
            rock.draw()
            rock.move()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
