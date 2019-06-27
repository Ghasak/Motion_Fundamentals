import pygame
import math

def move_coords(angle, radius, coords):
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)

def main():
    pygame.display.set_caption("Oribit")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    coords = 400, 200
    angle = 0
    rect = pygame.Rect(*coords,20,20)
    speed = 50
    next_tick = 100

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ticks = pygame.time.get_ticks()
        if ticks > next_tick:
            next_tick += speed
            angle += 1
            coords = move_coords(angle, 3, coords)
            rect.topleft = coords

        screen.fill((0,0,30))
        screen.fill((0,150,0), rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


# Drawing Curves with Midpt Circle Theorem
import pygame, sys, random, math
from pygame.locals import *

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,400))


        self.screen.fill((255, 255, 255))
        self.jom = pygame.Rect(100,100,2,2)

    def run(self):


        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False


            pygame.draw.rect(self.screen, (0,0,0), self.jom)



            ## Center of Curvature
            centercurv = (104,103)


            ## Update Position
                ## eqn of circle (x-104)**2 + (y-103)**2 - r**2 = 0, r == 5
            #circleeqn = (self.jom.x-centercurv[0])**2 + (self.jom.y-centercurv[1])**2
            #goright = (self.jom.x+1
            eR = -2*self.jom.x+2*centercurv[0]+1
            eD1 = -2*self.jom.x - 2*self.jom.y + 2*centercurv[0] + 2*centercurv[1] + 2
            print(eR,eD1)
            if abs(eR)-abs(eD1) > 0:
                #self.jom.x += 2
                self.jom.y -= 1
                print('1')
            elif abs(eR)-abs(eD1) < 0:
                #self.jom.x+=2
                print('2')
            else:
                if eR < 0 and eD1 < 0:
                    #self.jom.x+=2
                    print('3')
                elif eR > 0 and eD1 > 0:
                    self.jom.y -= 1
                    print('4')
            self.jom.x += 1

            pygame.display.flip()

        print('Quitting')
        pygame.quit()
        sys.exit()







if __name__ == '__main__':
    main()
    game = Game()
    game.run()
