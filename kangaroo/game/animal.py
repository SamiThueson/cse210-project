from core.actor import Actor
from game import constants

class Animal(Actor):

    def __init__(self):
        img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        super().__init__(filename=img)
        self.center_x = constants.CENTER_X
        self.center_y = constants.CENTER_Y
        
    def jump(self):
        self.change_y = 7

    def update(self):
        self.change_y -= constants.GRAVITY
        self.center_y += self.change_y