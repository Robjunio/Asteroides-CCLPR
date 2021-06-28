import util
from SpaceShip import SpaceShip
from random import randint


class GameController():
    def __init__(self):
        nave_bots = []
        asteroides = []
        score = 0
        wave = 1

    def random_spawn(self):
        pos_x, pos_y = randint(0, util.WINDOW_wIDTH), randint(0, util.WINDOW_HEIGTH)
        if SpaceShip.position[0] == pos_x or SpaceShip.position[1] == pos_y:
            return random_spawn()
        else:
            return pos_x, pos_y


    def start_wave(self, num_horda):
        pass


    def all_dead(self):
        if len(nave_bots) == 0 and len(asteroides) == 0:
            wave += 1
            start_wave(wave)
        else:
            continue

    def create_enemy(self)
        

