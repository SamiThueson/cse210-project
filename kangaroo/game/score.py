from core.actor import Actor
from game import constants
import random
import arcade

class Score(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = 580
        self.center_y = 580
        self._points = 0
        self._coins = 0
        self._lives = 0
    
    def set_coins(self, coins):
        self._coins = coins

    def set_lives(self, lives):
        self._lives = lives

    def set_points(self, points):
        self._points = points

    def draw(self):
        arcade.draw_text(f"Score: {self._points}", 500, self.center_y, arcade.color.WHITE)
        arcade.draw_text(f"{self._coins}", 600, self.center_y, arcade.color.WHITE)
        arcade.draw_text(f"Lives: {self._lives}", 700, self.center_y, arcade.color.WHITE)
        