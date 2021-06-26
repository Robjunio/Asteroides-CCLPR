import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

from Shot import playershot


class SpaceShip(object):
    def __init__(self, position, velocity):
        self.maneuverability = 3
        self.acceleration = 0.75
        self.position = Vector2(position)
        self.sprite = pygame.image.load("assets/space_ship.png")
        self.direction = Vector2(0, -1)
        self.radius = self.sprite.get_width() / 2
        self.angle = 90
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        angle = self.direction.angle_to(Vector2(0, -1))
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.acceleration

    def move(self, surface):
        self.position = self.wrap_position((self.position + self.velocity), surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

    def shot_bullet(self):
        return playershot(bullet_angle=self.angle, bullet_pos=self.position)

    def rotate(self, clockwise=True):
        sign = 15 if clockwise else -15
        angle_to_rotate = self.maneuverability * sign

        self.angle -= angle_to_rotate

        if self.angle == 360 and clockwise == False:
            self.angle = 0
        elif self.angle == 0 and clockwise == True:
            self.angle = 360

        self.direction.rotate_ip(angle_to_rotate)

    def stop(self):
        self.velocity -= self.direction * self.acceleration

    def wrap_position(self, position, surface):
        x, y = position
        w, h = surface.get_size()
        return Vector2(x % w, y % h)
