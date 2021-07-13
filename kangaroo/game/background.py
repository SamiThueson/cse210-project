from core.actor import Actor
from game import constants
import random
import arcade
class Background(Actor):

    def __init__(self):
        super().__init__()
        self.texture = constants.BACKGROUND_IMAGE
        self.scale = 1
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y