from core.actor import Actor
from game import constants


class SpeedTracker(Actor):

    def __init__(self):
        super().__init__()
        self._speed_factor = 1

    def get_speed(self):
        return self._speed_factor

    def increase_speed(self):
        self._speed_factor += 0.5

    def decrease_speed(self):
        self._speed_factor -= 0.5
