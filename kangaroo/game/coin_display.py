from core.actor import Actor
from game import constants
import random
import arcade
class Coin_Display(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.COIN_PIC
        self.scale = 0.2
        self.center_x = 622
        self.center_y =588
        self.change_x = constants.COIN_MOVE_SPEED
        

    def update(self):
       self.center_x += self.change_x