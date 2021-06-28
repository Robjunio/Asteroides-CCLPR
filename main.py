import pygame
import random
from Asteroid import Asteroid
from pygame.constants import K_SPACE, QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.math import Vector2
from util import get_random_position, get_random_velocity
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
    asteroids = []
    asteroids.append(Asteroid(
        asteroid_speed = get_random_velocity(1,3),
        asteroid_pos = get_random_position(screen)
    ))
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

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)
            if ship.collides_with(asteroid) is True:
                is_running = False
            for bullet in ship_bullets:
                if asteroid.collides_with(bullet) is True:
                    asteroids.remove(asteroid)

        for bullet in ship_bullets:
            bullet.move()
            bullet.draw(screen)
            if(bullet.is_colliding_with_wall() == True):
                ship_bullets.remove(bullet)

        ship.move(surface=screen)
        ship.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
