from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game import handle_collisions_action
from game import move_actors_action
from game import control_actors_action
from game.animal import Animal
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction


class GameScene(Scene):

    def __init__(self):
        
        # create the cast
        animal = Animal()

        cast = Cast()
        cast.add_actor("animals", animal)
        self.set_cast(cast)

        # create the script
        control_actors_action = ControlActorsAction()
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        draw_actors_action = DrawActorsAction()

        script = Script()
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handle_collisions_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        self.set_script(script)