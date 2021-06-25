from game.move_animal_action import MoveAnimalAction
from game import draw_actors_action
from core.scene import Scene
from core.cast import Cast
from game.animal import Animal
from core.script import Script
from game.draw_actors_action import DrawActorsAction
from core.cue import Cue

class GameScene(Scene):

    def __init__(self):
        animal = Animal()
        cast = Cast()
        cast.add_actor("animal", animal)
        self.set_cast(cast)

        move_animal_action = MoveAnimalAction()
        draw_actors_action = DrawActorsAction()
        script = Script()
        script.add_action(Cue.ON_UPDATE, move_animal_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        self.set_script(script)