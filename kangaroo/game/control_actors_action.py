import arcade
from core.action import Action



class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._control_player(cue, cast)
       
    def _control_player(self, cue, cast):
        cue_info = cue.get_info()
        if cue_info["key"] == arcade.key.SPACE:
            animal = cast.first_actor("animals")
            animal.jump()