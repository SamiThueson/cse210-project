
from game import animal

from core.action import Action
import arcade
from game import constants

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)
        self._handle_plant_animal_collisions(cast)

    def _handle_ground_collisions(self, cast):
        animal = cast.first_actor("animals")
        ground = cast.get_actors("ground")
        coin = cast.get_actors("coin")
        for tile in ground:
            if arcade.check_for_collision(animal, tile):
                animal.bottom = tile.top
                animal.walk()
        for c in coin:
            if arcade.check_for_collision(animal,c):
                c.remove_from_sprite_lists()

        # a temporary work around until the ground is finished (mm)
        # if animal.bottom <= 100:
        #     animal.bottom = 100
        #     animal.walk()

    def _handle_plant_animal_collisions(self, cast):
        plants = cast.get_actors("plants")
        animal = cast.first_actor("animals")
        for plant in plants:
            if arcade.check_for_collision(animal, plant):
                print("Ran into plant")
                arcade.play_sound(constants.COLLIDE_SOUND)