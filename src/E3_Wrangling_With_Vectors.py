''' Wrangling with Vectors.
    - We used tow values to generate diagonal movement as speed for the x component of thepostion and another fof the y- component. These two values combined form is what is known as a vector.
'''

import pygame
from pygame.locals import *
import pygame.math as pymath
import sys
import os
from sys import exit
import math
import time

'''
   Import Ghasak Tools that I have developed for learnign purposes
'''
sys.path.append(os.getcwd())
from GTools.add_line_function import *
# print(os.getcwd())
# print("--------")
# print(sys.path)
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
gray  = (128,128,128)
black = (0,0,0)
green = (0,255,0)
blue  = (0,0,128)
red   = (255,0,0)
aquamarine = (0,140,255)
pink = (138,43,226)
lightgreen = (94,196,229)

grid_color   = (18,48,59)
lightred     = (255,124,104)
yellow       = (255,255,0)

colors = [(119,136,153),(220,20,60),(138,43,226),(205,92,92)]
color_blinking = [(119,136,153),(119,136,153),(119,136,153),red, red,red]
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('SF Mono', 33)
# --------------------------------------------------------
class Particle:
    def __init__(self, x, y, size,color,VELOCITY_X, VELOCITY_Y):
        self.x = x
        self.y = y
        self.point = (x,y)
        self.size = size
        self.color = color
        self.thickness = 3 # 1 to not fill, and 0 to fill
        self.VELOCITY_X = VELOCITY_X
        self.VELOCITY_Y = VELOCITY_Y
        self.SwitchOne = True



    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, 0)
        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), self.size+10, self.thickness)
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



    def move_sequence(self,time_passed,P1x,P1y,P2x,P2y):
        self.P1x = P1x
        self.P1y = P1y
        self.P2x = P2x
        self.P2y = P2y

        self.time_passed = time_passed
        self.time_passed_seconds = self.time_passed /1000

        if self.SwitchOne == True:
            self.magnitude = (((self.x - self.P1x)**2)+((self.y - self.P1y)**2))**(0.5)
            self.heading_Vector_x = (P1x-self.x)/self.magnitude
            self.heading_Vector_y = (P1y-self.y)/self.magnitude
            self.x += self.VELOCITY_X * self.heading_Vector_x * self.time_passed_seconds
            self.y += self.VELOCITY_Y * self.heading_Vector_y * self.time_passed_seconds
            print(self.x,self.P1x)

            if int(self.x) == int(self.P1x) or int(self.y) == int(self.P1y):
                self.SwitchOne = False

        elif self.SwitchOne == False:
            self.magnitude = (((self.x - self.P2x)**2)+((self.y - self.P2y)**2))**(0.5)
            self.heading_Vector_x = (P2x-self.x)/self.magnitude
            self.heading_Vector_y = (P2y-self.y)/self.magnitude

            self.x += self.VELOCITY_X * self.heading_Vector_x * self.time_passed_seconds
            self.y += self.VELOCITY_Y * self.heading_Vector_y * self.time_passed_seconds
            print(self.x,self.P2x)

            if int(self.x) == int(self.P2x) or int(self.y) == int(self.P2y):
                self.VELOCITY_X = 0.0
                self.VELOCITY_Y = 0.0

        return self.x, self.y, self.VELOCITY_X,self.VELOCITY_Y






class Environment():
    def __init__(self, x, y, size, thickness):
        self.x = x
        self.y = y
        self.point = (x,y)
        self.size = size
        self.thickness = thickness

    def centerlines(self):
        for i in range(100):
            #pygame.draw.line(screen, black, (0, i*100), (i*100, HEIGHT), 5)
            pygame.draw.line(screen,grid_color, (0,i*100), (WIDTH,i*100),4)
            pygame.draw.line(screen,grid_color, (i*100,0), (i*100,HEIGHT),4)

            x_label = myfont.render(f"{int(i*100)} m.", True, lightgreen)
            y_label = myfont.render(f"{int(i*100)} m.", True, lightgreen)
            screen.blit(x_label,(0,i*100))
            screen.blit(y_label,((i*100,HEIGHT-30)))
        for i in range(100):
            if (i%100 == 0):
                continue
            else:
                pygame.draw.line(screen,grid_color, (0,i*50), (WIDTH,i*50),1)
                pygame.draw.line(screen,grid_color, (i*50,0), (i*50,HEIGHT),1)

        pygame.draw.line(screen,lightgreen, (0,HEIGHT/2), (WIDTH,HEIGHT/2),7)
        pygame.draw.line(screen,lightgreen, (WIDTH/2,0), (WIDTH/2, HEIGHT),7)


    def draw_point(self):
        # Vector is a point in space relative the
        pygame.draw.circle(screen, pink, (int(self.x), int(self.y)), self.size, self.thickness)
        pygame.draw.circle(screen, random.choice(colors), (int(self.x), int(self.y)), self.size+10, 3)
        #pygame.draw.polygon(screen, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        point_label = myfont.render(f"----P({(self.x)},{self.y})", True, lightred)
        screen.blit(point_label,(self.x,self.y))
        #pass
    def point_to_point(self,P2):
        self.P2 = P2
        '''- Creating an arrow to connect between the two points'''
        pygame.draw.line(screen,lightred, (self.x,self.y), (self.P2[0],self.P2[1]),5)

# --------------------------------------------------------------------------------
# Adding a semi class for vectors for teaching purposes, once mastered we can use
#   - Vector class offered by pygame library.
# --------------------------------------------------------------------------------
class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def from_points(P1,P2):
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)



def Test_Vector():

    A = (10.0, 20.0)
    B = (30.0, 35.0)
    add_line("P1- Create a vector from point A to Point B ")
    # --------------------------------------------------------
    AB = Vector2.from_points(A,B)
    print(AB)
    add_line("P2- Vector magnitude calculation")
    print(AB.get_magnitude())
    # --------------------------------------------------------


# --------------------------------------------------------------------------------


WIDTH = 1800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#screen.fill(colors[0])
#background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert()


def Engine():
    # --------------------------------------------------------
    # Our clock object
    clock = pygame.time.Clock()

    # Draw Vectors here

    A = Environment(100,200,10,0)
    B = Environment(30.0, 35.0, 10, 0)
    C = Environment(1700,400, 10,0)
    D = Environment(1400,700, 10,0)
    E = Environment(600,400,10,0)

    ParticleX = Particle(1700,400,50,yellow,100,100)
    ParticleY = Particle(600,400,50,lightred,100,100)
    ParticleZ = Particle(100,200,50,pink,100,100)
    # --------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill(black)
        Environment.centerlines(screen)
        # screen.set_colorkey((255,0,255))
        # screen.set_alpha(1)
        time_passed = clock.tick(60)  # This is a timer ,In a 1000 millesecond / 60 (max frame) = no. of


        A.point_to_point((B.x,B.y))
        C.point_to_point(D.point)
        D.point_to_point(E.point)


        A.draw_point()
        B.draw_point()
        C.draw_point()
        D.draw_point()
        E.draw_point()

        #ParticleA.move(time_passed)
        #ParticleA.move_to(time_passed,D.x,D.y)
        #ParticleA.move_to(time_passed,A.x,A.y)
        #ParticleX.move_to(time_passed,E.x,E.y)
        ParticleX.move_sequence(time_passed,D.x,D.y,E.x,E.y)
        ParticleY.move_sequence(time_passed,D.x,D.y,C.x,C.y)
        ParticleZ.move_sequence(time_passed,D.x,D.y,B.x,B.y)




        ParticleX.display()
        ParticleY.display()
        ParticleZ.display()

        pygame.display.update()



# --------------------------------------------------------
if __name__ == "__main__":
    Engine()
    Test_Vector()

