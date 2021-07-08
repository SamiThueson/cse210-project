import random
from core.action import Action
from game import constants
from game.plants import Plants


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()
        self._frame_for_plants = 180 #180 means 3 seconds
        self._current_frame = 0

    def execute(self, cast, cue, callback):
        self._move_animal(cast)
        self._move_ground(cast)
        self._move_plants(cast)

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
    

    def _move_coin(self, cast):
        coin = cast.get_actors("coin")
        for c in coin:
            c.update()
      

    def _move_plants(self, cast):
        plants = cast.get_actors("plants")
        for plant in plants:
            plant.update()
        if len(plants) != 0 and plants[0].right < 0:
            plants.pop(0)
            
        self._current_frame += 1
        print(self._current_frame)
        if self._current_frame >= self._frame_for_plants:
            print('Hello')
            plants = Plants()
            cast.add_actor("plants", plants)
            self._current_frame = 0
            self._frame_for_plants = random.randint(1, 180)

