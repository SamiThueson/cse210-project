from core.action import Action
from game import constants
import arcade

class MoveAnimalAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        animal = cast.first_actor("animal")
        animal.update()
    