from core.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        all_actors = cast.get_all_actors()
        for actor in all_actors:
            actor.draw()
    