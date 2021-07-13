import arcade
from core.action import Action



class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._control_player(cue, cast)
        self._restart_game(cue, cast, callback)
       
    def _control_player(self, cue, cast):
        cue_info = cue.get_info()
        if cue_info["key"] == arcade.key.SPACE:
            animal = cast.first_actor("animals")
            animal.jump()

        # example code for resetting game
        # if key is "enter" or whatever then do this...
        # if animal is dead restart
        # scene = callback.get_current_scene()
        # scene.reset()
    def _restart_game(self, cue, cast, callback):
        cue_info = cue.get_info()
        animal = cast.first_actor("animals")
        if animal.get_lives() == 0 and cue_info["key"] == arcade.key.ENTER:
            scene = callback.get_current_scene()
            scene.reset()