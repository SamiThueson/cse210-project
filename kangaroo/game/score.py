from core.actor import Actor
from game import constants
import random
import arcade

class Score(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.SCORE
        self.scale = 1
        self.center_x = 780
        self.center_y = 580
        self.change_x = constants.COIN_MOVE_SPEED
      

    def update(self):
       self.center_x += self.change_x