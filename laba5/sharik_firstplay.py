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

FPS = 2
points = 0
finish = False
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

def new_ball():
    global x, y, r
    x = randint(100, 1000)
    y = randint(100, 800)
    r = randint(25,100)
    color = COLOR[randint(0,7)]
    circle(screen, color, (x,y), r)
    


def click():
    return (event.pos[0] - x)**2 + (y-event.pos[1])**2 <= r**2

new_ball()
pygame.display.update()
while not finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
           if click() == True:
               points +=1
               print(points)
    screen.fill(BLACK)
    new_ball()
    pygame.display.update()

pygame.quit()
