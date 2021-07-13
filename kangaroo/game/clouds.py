from core.actor import Actor
from game import constants
import random
import arcade
class Cloud(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.CLOUD_PIC
        self.scale = 1
        self.center_x = constants.SCREEN_WIDTH + (self.width / 2)
        self.center_y = random.randint(300,500)
        self.change_x = constants.CLOUD_MOVE_SPEED
        self.cloud_list = arcade.SpriteList()

    def update(self):
       self.center_x += self.change_x