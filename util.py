import pygame
import random
from pygame.math import Vector2


def collision(pos1, pos2):
    pass


def quit():
    pygame.quit()
    exit()


def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )
        # Color's
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initial Position of the ship
starting_pos = (0, 0)

# Reset Values
new_score = 0

# Screen Size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600