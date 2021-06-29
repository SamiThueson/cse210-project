from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        animal = cast.first_actor("animals")
        ground = cast.get_actors("ground")
        for tile in ground:
            if arcade.check_for_collision(animal, tile):
                animal.bottom = tile.top
                animal.walk()
        # a temporary work around until the ground is finished (mm)
        # if animal.bottom <= 100:
        #     animal.bottom = 100
        #     animal.walk()

    

    