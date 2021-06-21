import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

from SpaceShip import SpaceShip

class playershot():
    def __init__(self, bullet_speed, bullet_pos, bullet_angle):
        self.bullet_speed = [8]
        self.angle =
        self.bullet_pos = SpaceShip.wrap_position