import pygame
import assets
from pygame.math import Vector2
from pygame.transform import rotozoom


class Asteroid:
    def __init__(self, asteroid_speed, asteroid_pos):
        self.asteroid_speed = asteroid_speed
        self.asteroid_pos = asteroid_pos
        self.sprite = pygame.image.load("assets/asteroid.png")
        self.radius = self.sprite.get_width() / 2

    def draw(self, surface):
        blit_position = self.asteroid_pos - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)