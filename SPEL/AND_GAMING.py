import pygame, sys, math
from pygame.locals import *
from random import randint

pygame.init()

width, height = 1000, 600
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAMING")

fpsClock = pygame.time.Clock()
FPS = 144

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (50, 100, 0)

#pixeldimension = 10
#for x in range(pixeldimension, width-pixeldimension, 2*pixeldimension):
#    for y in range(pixeldimension, height-pixeldimension, 2*pixeldimension):
#       pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, pixeldimension, pixeldimension))

upperEnviormentArray = []
lowerEnviormentArray = []

class enviormentRect:
    def __init__(self, x, y, dimensions):
        self.x = x
        self.y = y
        self.dx = -2
        self.dimensions = dimensions
        self.color = DARK_GREEN

    def draw(self):

        pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.dimensions, self.dimensions))

    def update(self, array):
        self.x += self.dx

        if self.x + 2*self.dimensions <= 0:
            array.pop(0)
            array.append(enviormentRect(array[len(array)-1].x + array[len(array)-1].dimensions, array[len(array)-1].y + randint(-1, 1)*array[len(array)-1].dimensions, array[len(array)-1].dimensions))

def buildTerrainLayer(startX, startY, dimensions, array):
    array.append(enviormentRect(startX, startY, dimensions))

    for i in range(1, int(width/dimensions) + 2):
        array.append(enviormentRect(array[i-1].x + array[i-1].dimensions, array[i-1].y + randint(-1, 1)*array[i-1].dimensions, array[i-1].dimensions))

buildTerrainLayer(0, int(height*0.8), 5, upperEnviormentArray)
buildTerrainLayer(0, int(height*0.2), 5, lowerEnviormentArray)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    for i in lowerEnviormentArray:
        i.draw()
        i.update(lowerEnviormentArray)

    for i in upperEnviormentArray:
        i.draw()
        i.update(upperEnviormentArray)

    pygame.display.update()
    fpsClock.tick(FPS)
