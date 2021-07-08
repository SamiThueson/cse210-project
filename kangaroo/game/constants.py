import arcade
import random

# GAME CONSTANTS
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
GRAVITY = 0.5

# ANIMAL CONSTANTS
ANIMAL_JUMP_SPEED = 15
ANIMAL_ANIMATION_RATE = 3
ANIMAL_PATH = ":resources:images/animated_characters/female_person"
ANIMAL_FALLING = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_fall.png")
ANIMAL_IDLE = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_idle.png")
ANIMAL_JUMPING = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_jump.png")
ANIMAL_WALKING = [None] * 8 
ANIMAL_WALKING[0] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk0.png")
ANIMAL_WALKING[1] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk1.png")
ANIMAL_WALKING[2] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk2.png")
ANIMAL_WALKING[3] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk3.png")
ANIMAL_WALKING[4] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk4.png")
ANIMAL_WALKING[5] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk5.png")
ANIMAL_WALKING[6] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk6.png")
ANIMAL_WALKING[7] = arcade.load_texture(f"{ANIMAL_PATH}/femalePerson_walk7.png")

# GROUND CONSTANTS
GROUND_MOVE_SPEED = -10
GROUND_PATH = ":resources:images/tiles"


#COIN
COIN_MOVE_SPEED = -10
COIN_PATH = ":resources:images/items"
COIN_PIC =  arcade.load_texture(f"{COIN_PATH}/coinGold.png")
COIN_COUNT = 1

GROUND_GRASS = arcade.load_texture(f"{GROUND_PATH}/grassMid.png")

# PLANT CONSTANTS
PLANT_MOVE_SPEED = -10
PLANT_PATH = ":resources:images/tiles"
#PLANT_IMAGE = [None] * random.randint(1, 4)
PLANT_CACTUS = arcade.load_texture(f"{PLANT_PATH}/cactus.png")
# PLANT_IMAGE[0] = arcade.load_texture(f"{PLANT_PATH}/cactus.png")
# PLANT_IMAGE[1] = arcade.load_texture(f"{PLANT_PATH}/bush.png")
# PLANT_IMAGE[2] = arcade.load_texture(f"{PLANT_PATH}/rock.png")
# PLANT_IMAGE[3] = arcade.load_texture(f"{PLANT_PATH}/mushroomRed.png")

COLLIDE_SOUND = arcade.load_sound(":resources:sounds/jump5.wav")

