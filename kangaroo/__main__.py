import arcade
from core.director import Director
from game import constants
from game.game_scene import GameScene


def main():
    game_scene = GameScene()
    director = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    director.direct_scene(game_scene)
    arcade.run()


if __name__ == "__main__":
    main()