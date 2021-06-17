import pygame
import random
from models import Asteroid, Spaceship
from pygame.image import load
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import get_random_velocity, load_sprite, wrap_position


def __init__(self):
    self._init_pygame()
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", False)
    self.clock = pygame.time.Clock()
    self.asteroids = []
    self.spaceship = Spaceship((400, 300))
    for _ in range(6):
        while True:
            position = get_random_position(self.screen)
            if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
            ):
                break
        self.asteroids.append(Asteroid(position))


def get_game_objects(self):
    game_objects = [*self.asteroids]
    if self.spaceship:
        game_objects.append(self.spaceship)
    return game_objects


def process_game_logic(self):
    for game_object in self._get_game_objects():
        game_object.move(self.screen)


def draw(self):
    self.screen.blit(self.background, (0, 0))
    for game_object in self._get_game_objects():
        game_object.draw(self.screen)
    pygame.display.flip()
    self.clock.tick(60)


def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )


def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)


def __init__(position):
    super().__init__(
        position, load_sprite("asteroid"), get_random_velocity(1, 3)
    )


def process_game_logic(self):
    for game_object in self._get_game_objects():
        game_object.move(self.screen)
    if self.spaceship:
        for asteroid in self.asteroids:
            if asteroid.collides_with(self.spaceship):
                self.spaceship = None
                break


def _handle_input(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            quit()
    is_key_pressed = pygame.key.get_pressed()
    if self.spaceship:
        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()


class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("asteroid"), (0, 0))


class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250
