from core.actor import Actor
from game import constants
import random
import arcade
class Coin(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.COIN_PIC
        self.scale = 1
        self.center_x = random.randrange(300,600)
        self.center_y = 400
        self.change_x = constants.COIN_MOVE_SPEED
        self.coin_list = arcade.SpriteList()

    def update(self):
       self.center_x -= 1