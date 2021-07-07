from core.action import Action
from game import constants


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._move_animal(cast)
        self._move_ground(cast)

    def _move_animal(self, cast):
        animal = cast.first_actor("animals")
        animal.update()

    def _move_ground(self, cast):
        ground = cast.get_actors("ground")
        for tile in ground:
            tile.update()
        if ground[0].right < 0:
            tile = ground.pop(0)
            tile.left = ground[-1].right
            ground.append(tile)
    
    def _move_plants(self, cast):
        plants = cast.get_actors("plants")
        for plant in plants:
            plant.update()