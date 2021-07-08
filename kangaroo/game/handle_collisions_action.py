
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
        self._handle_coin_animal_collisions(cast)

    def _handle_ground_collisions(self, cast):
        animal = cast.first_actor("animals")
        ground = cast.get_actors("ground")
        for tile in ground:
            if arcade.check_for_collision(animal, tile):
                animal.bottom = tile.top
                animal.walk()

    def _handle_coin_animal_collisions(self,cast):
        animal = cast.first_actor("animals")
        coin = cast.get_actors("coin")
        for c in coin:
            if arcade.check_for_collision(animal,c):
               cast.remove_actor("coin",c)
               animal.add_coins()
               if animal.get_coins() % 5 == 0:
                   animal.add_lives()
                   print(animal.get_lives())

        # a temporary work around until the ground is finished (mm)
        # if animal.bottom <= 100:
        #     animal.bottom = 100
        #     animal.walk()

    def _handle_plant_animal_collisions(self, cast):
        plants = cast.get_actors("plants")
        animal = cast.first_actor("animals")
        for plant in plants:
            if arcade.check_for_collision(animal, plant):
                arcade.play_sound(constants.COLLIDE_SOUND)
                animal.remove_lives()
                if animal.get_lives() == 0:
                    print('GAME OVER')