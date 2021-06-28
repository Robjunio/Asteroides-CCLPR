import util
from SpaceShip import SpaceShip
from random import randint
from pygame.math import Vector2


class GameController():
    def __init__(self):
        bot_ships = []
        asteroides = []
        score = 0
        wave = 1
        

    def random_spawn(self):
        pos_x, pos_y = randint(0, util.WINDOW_wIDTH), randint(0, util.WINDOW_HEIGTH)
        if SpaceShip.position[0] == pos_x or SpaceShip.position[1] == pos_y:
            return random_spawn()
        else:
            return Vector2(pos_x, pos_y)


    def create_enemy(self, bot, asteroid):
        if asteroid:
            asteroids.append(Asteroid(
        asteroid_speed=get_random_velocity(1, 3),
        asteroid_pos= random_spawn()))

        if bot:
            bot_ships.append(ShipBot( position= random_spawn(),
        velocity = get_random_velocity(1, 5))
            
        

    def start_wave(self, wave):
        pass


    def all_dead(self):
        if len(nave_bots) == 0 and len(asteroides) == 0:
            wave += 1
            start_wave(wave)
        else:
            continue

    
        

