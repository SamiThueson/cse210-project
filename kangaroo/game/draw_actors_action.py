from game import background
from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_background(cast)
        self._draw_animal(cast)
        self._draw_ground(cast)
        self._draw_coin(cast)
        self._draw_plants(cast)
        self._draw_labels(cast)
        

    def _draw_animal(self, cast):
        animals = cast.get_actors("animals")
        for animal in animals:
            animal.draw()

    def _draw_ground(self, cast):
        ground = cast.get_actors("ground")
        for tile in ground:
            tile.draw()


    def _draw_coin(self,cast):
        coin = cast.get_actors("coin")
        for c in coin:
            c.draw()

    
    def _draw_plants(self, cast):
        plants = cast.get_actors("plants")
        for plant in plants:
            plant.draw()

    def _draw_background(self, cast):
        backgrounds = cast.get_actors("background")
        for background in backgrounds:
            background.draw()

    def _draw_labels(self, cast):
        labels = cast.get_actors("labels")
        for label in labels:
            label.draw()