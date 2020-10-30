import pygame
from pygame.draw import *
from random import randint
pygame.init()

RED = (200, 10, 10)
GREEN = (10, 200, 10)
YELLOW = (200, 200, 10)
ORANGE = (255, 150, 10)
PURPLE = (150, 0, 150)
PINK = (200, 60, 150)
WHITE = (255, 255, 255)
SALAD = (200, 255, 20)
BLACK = (0, 0, 0)

COLOR = [RED,
         GREEN,
         YELLOW,
         ORANGE,
         PURPLE,
         PINK,
         WHITE,
         SALAD]

xsize, ysize = 1200, 900
FPS = 1
points = 0
finish = False
screen = pygame.display.set_mode((xsize, ysize))
clock = pygame.time.Clock()

x = randint(100, 1000)
y = randint(100, 800)
r = randint(25,100)
color = COLOR[randint(0,7)]

def click():
    return (event.pos[0] - x)**2 + (y-event.pos[1])**2 <= r**2

def new_ball(x0, y0, r0):
    circle(screen,color,(x,y),r)
    pygame.display.update()
    screen.fill(BLACK)
    x0 += 10
    y0 +=10
    
    




new_ball(x,y,r)
pygame.display.update()
while not finish:
    x += 10
    y += 10
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
           if click() == True:
               points +=1
               print(points)
    new_ball(x, y, r)

pygame.quit()

   
    


