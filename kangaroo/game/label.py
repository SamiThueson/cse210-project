from core.actor import Actor
from game import constants
import arcade


class Label(Actor):

    def __init__(self, message):
        super().__init__()
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y
        self.width = constants.SCREEN_WIDTH * .65
        self.height = constants.SCREEN_HEIGHT * .25
        self.message = message
        
    def draw(self):
        # arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.BLACK, 10)
        # arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
        # arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.BLANCHED_ALMOND)
        arcade.draw_text(self.message, self.center_x, self.center_y, arcade.color.BLUE_SAPPHIRE, align="center", anchor_x="center", anchor_y="center")