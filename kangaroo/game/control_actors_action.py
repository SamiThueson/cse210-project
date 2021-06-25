import arcade
from core.action import Action


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        cue_info = cue.get_info()
        if cue_info["key"] == arcade.key.SPACE:
            animal = cast.first_actor("animals")
            animal.jump()
    