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
import random

# --------------------------------------------------------
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
black = (0  , 0  ,0   )
green = (0, 255, 0)
blue  = (0, 0, 128)
red   = (255, 0, 0)
aquamarine = (0, 140, 255)
colors = [(119,136,153),(220,20,60),(138,43,226),(205,92,92)]
color_blinking = [(119,136,153),(119,136,153),(119,136,153),red, red,red]
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
        self.thickness = 3 # 1 to not fill, and 0 to fill
        self.VELOCITY_X = VELOCITY_X
        self.VELOCITY_Y = VELOCITY_Y


    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, 0)
        pygame.draw.circle(screen, black, (int(self.x), int(self.y)), self.size, self.thickness)
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

class Environment():
    def centerlines():
        for i in range(100):
            #pygame.draw.line(screen, black, (0, i*100), (i*100, HEIGHT), 5)
            pygame.draw.line(screen,black, (0,i*100), (WIDTH,i*100),1)
            pygame.draw.line(screen,black, (i*100,0), (i*100,HEIGHT),1)
            x_label = myfont.render(f"{int(i*100)} m.", True, black)
            y_label = myfont.render(f"{int(i*100)} m.", True, black)
            screen.blit(x_label,(0,i*100))
            screen.blit(y_label,((i*100,HEIGHT-30)))
        pygame.draw.line(screen,red, (0,HEIGHT/2), (WIDTH,HEIGHT/2),5)
        pygame.draw.line(screen,red, (WIDTH/2,0), (WIDTH/2, HEIGHT),5)



WIDTH = 2000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#screen.fill(colors[0])
#background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert()


def Engine():
    # --------------------------------------------------------
    # Our clock object
    clock = pygame.time.Clock()
    vxa,vya  = [50,40]
    vxb,vyb  = [30,25]
    vxc,vyc  = [60,40]
    xa = ya =  500 * random.random()
    xb = yb =  1000 * random.random()
    xc = yc =  200 * random.random()
    # Creating your particles with initial conditions

    b = Particle(xb,yb, 50, colors[2],vxb,vyb)
    c = Particle(xc,yc, 100, colors[3],vxc,vyc)

    # --------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill(colors[0])
        Environment.centerlines()
        # screen.set_colorkey((255,0,255))
        # screen.set_alpha(1)
        time_passed = clock.tick(60)  # This is a timer ,In a 1000 millesecond / 60 (max frame) = no. of
        a = Particle(xa, ya, 20,random.choice(color_blinking) ,vxa,vya)
        a.display()
        b.display()
        c.display()

        xa,ya,vxa,vya  = a.move(time_passed)
        xb,yb,vxb,vyb  = b.move(time_passed)
        xc,yc,vxc,vyc  = c.move(time_passed)

        pygame.display.update()



# --------------------------------------------------------
if __name__ == "__main__":
    Engine()

