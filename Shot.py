import pygame
import assets
from pygame.math import Vector2
from pygame.transform import rotozoom

class Shot():
    def __init__(self, bullet_speed, bullet_pos):
        self.bullet_speed = bullet_speed
        self.bullet_pos = bullet_pos
        self.sprite = pygame.image.load("assets/bullet.png")
        self.radius = self.sprite.get_width() / 2
