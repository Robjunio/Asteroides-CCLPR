from Shot import Shot
import pygame
from util import WINDOW_HEIGHT

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, life=1):
        self.x = x
        self.y = y
        self.life = life
        self.ship_img = None
        self.shoot = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for shoot in self.shoot:
            shoot.draw(window)

    def move_shoot(self, vel, obj):
        self.cooldown()
        for shoot in self.shoots:
            shoot.move(vel)
            if shoot.off_screen(WINDOW_HEIGHT):
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
