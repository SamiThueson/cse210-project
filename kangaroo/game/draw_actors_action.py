from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self):
        pass

    def execute(self, scene, cue, callback):
        cast = scene.get_cast()
        all_actors = cast.get_all_actors()
        for actor in all_actors:
            actor.draw()
    