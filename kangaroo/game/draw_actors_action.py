from game import background
from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_background(cast)
        self._draw_clouds(cast)
        self._draw_animal(cast)
        self._draw_ground(cast)
        self._draw_coin(cast)
        self._draw_plants(cast)
        self._draw_coindisplay(cast)

        self._draw_score(cast)

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

    def _draw_score(self,cast):
        animal = cast.first_actor("animals")
        points = animal.get_score()
        coins = animal.get_coins()
        lives = animal.get_lives()
        score = cast.first_actor("score")
        score.set_coins(coins)
        score.set_lives(lives)
        score.set_points(points)
        score.draw()

    def _draw_background(self, cast):
        backgrounds = cast.get_actors("background")
        for background in backgrounds:
            background.draw()

    def _draw_labels(self, cast):
        labels = cast.get_actors("labels")
        for label in labels:
            label.draw()

    def _draw_clouds(self, cast):
        cloud = cast.get_actors("cloud")
        for cl in cloud:
            cl.draw()

    def _draw_coindisplay(self, cast):
        coindisplay = cast.get_actors("coindisplay")
        for cd in coindisplay:
            cd.draw()

