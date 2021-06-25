from core.action import Action


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._move_animal(cast)

    def _move_animal(self, cast):
        animal = cast.first_actor("animals")
        animal.update()
    