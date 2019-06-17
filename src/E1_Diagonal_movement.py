''' Diagonal Movement
    Straight-line motion is useful, but a game would likely get pretty dull if everying moved horizontally or vertically. We need to be able to move a sprite in any direction we choose,
    - Rule to remember, the Class creating objects with variables and methods, look at
        updating any event what will happen to the values of the variables and each method in the
        class.
'''

import pygame
from pygame.locals import *
import pygame.math as pymath
import sys
import os
from sys import exit

'''
    Added the Class object - Movement is in one direction only.
'''

# --------------------------------------------------------
# CURRENT_DIR = os.getcwd()
# BACKGROUND_IMAGE_FILENAME =  os.path.join(CURRENT_DIR,"resources/background.png")
# CAR_FILENAME = os.path.join(CURRENT_DIR,"resources/car3.png")
# print(os.listdir())
# --------------------------------------------------------
import pygame
from pygame.locals import *
from sys import exit

# --------------------------------------------------------
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue  = (0, 0, 128)
red   = (255, 0, 0)
aquamarine = (0, 140, 255)
colors = [(119,136,153),(220,20,60),(138,43,226),(205,92,92)]
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('SF Mono', 30)
# --------------------------------------------------------
class Particle:
    def __init__(self, x, y, size,color,VELOCITY_X, VELOCITY_Y):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.thickness = 0 # 1 to not fill, and 0 to fill
        self.VELOCITY_X = VELOCITY_X
        self.VELOCITY_Y = VELOCITY_Y


    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        self.distance_traveled_label = myfont.render(f"Distance {int(self.x)} m.", True, green, blue)
        screen.blit(self.distance_traveled_label,(self.x,self.y))

    def move(self, time_passed):
        self.time_passed = time_passed
        self.time_passed_seconds = self.time_passed /1000
        self.x += self.VELOCITY_X * self.time_passed_seconds
        self.y += self.VELOCITY_Y * self.time_passed_seconds
        # If the particle goes off the edge of teh screen,
        # Make it move in the opposite direction
        if (self.x + self.size) > WIDTH or self.x < 0:
            self.VELOCITY_X = -1 * self.VELOCITY_X
        if (self.y + self.size) > HEIGHT or self.y < 0:
            self.VELOCITY_Y = -1 * self.VELOCITY_Y
        return self.x, self.y,self.VELOCITY_X,self.VELOCITY_Y


WIDTH = 1800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(colors[0])
#background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert()


def Engine():
    # --------------------------------------------------------
    # Our clock object
    clock = pygame.time.Clock()
    vxa,vya  = [130,200]
    vxb,vyb  = [200,300]
    vxc,vyc  = [323,100]
    xa = ya = xb = yb = xc = yc = 0

    # --------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill(colors[0])
        # screen.set_colorkey((255,0,255))
        # screen.set_alpha(1)
        time_passed = clock.tick(60)  # This is a timer ,In a 1000 millesecond / 60 (max frame) = no. of
        a = Particle(xa, ya, 20,colors[1],vxa,vya)
        b = Particle(xb,yb, 50, colors[2],vxb,vyb)
        c = Particle(xc,yc, 100, colors[3],vxc,vyc)
        a.display()
        b.display()
        c.display()
        xa,ya ,vxa,vya = a.move(time_passed)
        xb,yb,vxb,vyb  = b.move(time_passed)
        xc,yc,vxc,vyc  = c.move(time_passed)

        pygame.display.update()



# --------------------------------------------------------
if __name__ == "__main__":
    Engine()

