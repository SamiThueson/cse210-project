from game.speed_tracker import SpeedTracker
from game.clouds import Cloud
from game.constants import BACKGROUND_IMAGE
from game.background import Background
import arcade
import pyglet
from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game.animal import Animal
from game.ground import Ground

from game.clouds import Cloud

from game.score import Score

from game.coin import Coin

from game.plants import Plants
from game.coin_display import Coin_Display

from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction


class GameScene(Scene):

    def __init__(self):
        self.reset()
        
    def reset(self):
        # create the cast
        cast = Cast()
        animal = Animal()
        plants = Plants()
        clouds = Cloud()
        coindisplay = Coin_Display()

        score = Score()
        speed_tracker = SpeedTracker()

        cast.add_actor("animals", animal)
        for i in range(10):
            ground = Ground()
            ground.left = (i * ground.width)
            cast.add_actor("ground", ground)
        background = Background()
        cast.add_actor("background", background)

        self.coin_list = arcade.SpriteList()
        for i in range(1):
            coin = Coin()
            self.coin_list.append(coin)
            cast.add_actor("coin", coin)
        cast.add_actor("plants", plants)
        cast.add_actor("clouds", clouds)
        cast.add_actor("score", score)
        cast.add_actor("coindisplay", coindisplay)

        cast.add_actor("speed_tracker", speed_tracker)
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

    '''def get_window() -> pyglet.window.window:*/'''
        
