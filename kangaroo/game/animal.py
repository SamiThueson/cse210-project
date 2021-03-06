from core.actor import Actor
from game import constants


class Animal(Actor):

    def __init__(self):
        super().__init__()
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y
        self.texture = constants.ANIMAL_IDLE
        self._is_jumping = False
        self._is_walking = False
        self._current_frame = 0
        self._texture_index = 0
        self._num_jumps = 0
        self._lives = 3
        self._coins = 0
        self._score = 0
        self._number_of_jumps = 0
        
    def jump(self):
        if self._number_of_jumps < 2:
            self._number_of_jumps += 1
            self._is_jumping = True
            self._is_walking = False
            self.change_y = constants.ANIMAL_JUMP_SPEED
    
    def walk(self):
        self._is_jumping = False
        self._is_walking = True
        self.change_y = 0
        self._number_of_jumps = 0
        
    def update(self):
        self._update_position()
        self._check_jumping()
        self._check_walking()
        self._check_falling()
        
    def _check_falling(self):
        if self.change_y < -1:
            self.texture = constants.ANIMAL_FALLING

    def _check_jumping(self):
        if self.change_y > 0:
            self.texture = constants.ANIMAL_JUMPING

    def _check_walking(self):
        if self._is_walking:
            self._current_frame += 1
            if self._current_frame >= constants.ANIMAL_ANIMATION_RATE:
                num_textures = len(constants.ANIMAL_WALKING)
                self._current_frame = 0
                self._texture_index = (self._texture_index + 1) % num_textures
                self.texture = constants.ANIMAL_WALKING[self._texture_index]
    
    def get_lives(self):
        return self._lives

    def add_lives(self):
        self._lives += 1

    def remove_lives(self):
        self._lives -= 1
        if self._lives < 0:
            self._lives = 0

    def get_coins(self):
        return self._coins

    def add_coins(self):
        self._coins += 1
    
    def remove_coins(self):
        self._coins -= 1
        if self._coins < 0:
            self._coins = 0

    def get_score(self):
        return self._score
    
    def add_score(self):
        self._score += 5

    def _update_position(self):
        self.change_y -= constants.GRAVITY   
        self.center_y += self.change_y