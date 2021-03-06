import random
from core.action import Action
from game import constants
from game.plants import Plants
from game.coin import Coin
from game.clouds import Cloud
from game.ground import Ground


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()
        self._current_frame = 0
        self._current_coin_frame = 0
        self._current_cloud_frame = 0
        self._current_speed_frame = 0
        self._frame_for_cloud = 180
        self._frame_for_speedup = 300
        self._frame_for_plants = 180 #180 means 3 seconds
        self._frame_for_coin = 180
        
    def execute(self, cast, cue, callback):
        animal = cast.first_actor("animals")
        if animal.get_lives() != 0:
            self._move_animal(cast)
            self._move_ground(cast)
            self._move_plants(cast)
            self._move_coin(cast)
            self._move_cloud(cast)
            # self._increase_speed(cast)

    def _move_animal(self, cast):
        animal = cast.first_actor("animals")
        animal.update()

    def _move_ground(self, cast):
        ground = cast.get_actors("ground")
        for tile in ground:
            tile.update()
        if ground[0].right < 0:
            ground.pop(0)
            tile = Ground()
            tile.left = ground[-1].right
            ground.append(tile)
    

    def _move_coin(self, cast):
        coin = cast.get_actors("coin")
        for c in coin:
            c.update()
        if len(coin) != 0 and coin[0].right < 0:
            coin.pop(0)
        self._current_coin_frame += 1
        if self._current_coin_frame >= self._frame_for_coin:
            coin = Coin()
            cast.add_actor("coin", coin)
            self._current_coin_frame = 0
            self._frame_for_coin = random.randint(1, 180)

    def _move_cloud(self, cast):
        cloud = cast.get_actors("cloud")
        for cl in cloud:
            cl.update()
        if len(cloud) != 0 and cloud[0].right < 0:
            cloud.pop(0)
            
        self._current_cloud_frame += 1
        if self._current_cloud_frame >= self._frame_for_cloud:
            cloud = Cloud()
            cast.add_actor("cloud", cloud)
            self._current_cloud_frame = 0
            self._frame_for_cloud = random.randint(1, 180)

    def _move_plants(self, cast):
        plants = cast.get_actors("plants")
        for plant in plants:
            plant.update()
        if len(plants) != 0 and plants[0].right < 0:
            plants.pop(0)
            
        self._current_frame += 1
        if self._current_frame >= self._frame_for_plants:
            plants = Plants()
            cast.add_actor("plants", plants)
            self._current_frame = 0
            self._frame_for_plants = random.randint(1, 180)

    def _increase_speed(self, cast):
        self._current_speed_frame += 1
        if self._current_speed_frame >= self._frame_for_speedup:
            speed_tracker = cast.first_actor("speed_tracker")
            speed_tracker.increase_speed()
            speed_factor = speed_tracker.get_speed()
            for group in cast.get_all_actors():
                for actor in group:
                    actor.change_x *= speed_factor
                    print(group, "-", speed_factor, "-", actor.change_x)
            self._current_speed_frame = 0
