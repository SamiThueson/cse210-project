from core.action import Action


class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        animal = cast.first_actor("animals")
        # a temporary work around until the ground is finished (mm)
        if animal.bottom <= 100:
            animal.bottom = 100
            animal.walk()

    