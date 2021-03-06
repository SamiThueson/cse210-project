
from game import animal
from game.label import Label

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

               arcade.play_sound(constants.COIN_COLLIDE_SOUND)
               cast.remove_actor("coin",c)
               animal.add_coins()
               animal.add_score()
               if animal.get_coins() % 5 == 0:
                    animal.add_lives()
                   
    def _handle_plant_animal_collisions(self, cast):
        plants = cast.get_actors("plants")
        animal = cast.first_actor("animals")
        for plant in plants:
            if not plant.has_collided() and arcade.check_for_collision(animal, plant):
                plant.set_collided()
                arcade.play_sound(constants.COLLIDE_SOUND)
                animal.remove_lives()
                if animal.get_lives() == 0:
                    label = Label("GAME OVER Press enter to start")
                    cast.add_actor("labels", label)