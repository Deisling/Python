import pygame
import random

MAX_X = 1920
MAX_Y = 1024
MAX_SNOW = 100 
SNOW_SIZE = 64

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0-SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:     #Move RIGHT
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i ==2:    #Move LEFT  
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))      


def initialize_snow(MAX_SNOW, SNOW_SIZE)

      



     

# ----------------------------MAIN-------------------------
def initialize_pygame(MAX_X, MAX_Y):
    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []




initialize_snow(MAX_SNOW, SNOW_SIZE)

while True:
    check_for_exit()
    move_snow()
    draw_snow()