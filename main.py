import pygame
from pygame.constants import K_SPACE, QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.math import Vector2

from SpaceShip import SpaceShip
from util import WINDOW_WIDTH, WINDOW_HEIGHT

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    ship = SpaceShip(
        position=Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
        velocity=Vector2(0, 0)
    )

    ship_bullets = []

    is_running = True

    while is_running:
        clock.tick(60)
        for event in pygame.event.get():

            # defining a way out of the game
            if event.type == QUIT:
                is_running = False

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ship.rotate(clockwise=True)
                elif event.key == K_LEFT:
                    ship.rotate(clockwise=False)
                elif event.key == K_UP:
                    ship.accelerate()
                elif event.key == K_DOWN:
                    ship.stop()
                elif event.key == K_SPACE:
                    ship_bullets.append(ship.shot_bullet())


        ship.move(surface=screen)
        ship.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
