import pygame
from pygame.math import Vector2

from Shot import Shot


class ShipBot:
    COOLDOWN = 30

    def __init__(self, position, velocity, life=1):
        self.position = Vector2(position)
        self.sprite = pygame.image.load("assets/space_ship.png")
        self.velocity = Vector2(velocity)
        self.radius = self.sprite.get_width() / 2
        self.life = life
        self.ship_img = None
        self.shoots = []
        self.cool_down_counter = 0

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position += self.velocity

    def move_shoot(self, vel, obj):
        self.cooldown()
        for shoot in self.shoots:
            shoot.move(vel)
            if shoot.is_colliding_with_wall():
                self.shoots.remove(shoot)
            elif shoot.collision(obj):
                obj.life -= 1
                self.shoots.remove(shoot)


    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            shoot = Shot(self.x, self.y)
            self.shoots.append(shoot)
            self.cool_down_counter = 1
