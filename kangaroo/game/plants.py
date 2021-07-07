from core.actor import Actor
from game import constants
import random


class Plants(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.PLANT_CACTUS
        self.scale = 0.85
        self.center_x = random.randint(0, 700) + (self.width / 2)
        self.center_y = 100 + (self.height / 2)
        self.change_x = constants.PLANT_MOVE_SPEED

    def update(self):
        self.center_x += self.change_x