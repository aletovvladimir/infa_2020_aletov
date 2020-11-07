from random import randint
import math

import pygame
from pygame.draw import *

FPS = 30
BLACK = (0,0,0)

time = 25
player_time = 0
frames = 0
score = 0
finished = False

size = 10
width = 160*size
length = 90* size
clock = pygame.time.Clock()

number_of_balls =  randint(5,50)
number_of_flowers = randint(0,25)

print('введите ваше имя')
player = input()

pygame.init()

screen = pygame.display.set_mode((width, length))
    

def text() :
    f1 = pygame.font.Font(None, 15*size )
    text1 = f1.render('victory', 1, (180, 0, 0))
    screen.blit(text1, (int(width/2 - 25*size), int(length/2 - 15*size)))
        
    f2 = pygame.font.Font(None, 15*size )
    text2 = f2.render('Your score is:' , 1, (0, 0, 180))
    screen.blit(text2, (int(width/2 - 45*size), int(length/2 )))
    
    f3 = pygame.font.Font(None, 15*size )
    text3 = f3.render( str(score) , 1, (0, 180, 0))
    screen.blit(text3, (int(width/2 + 27*size) , int(length/2)))

    f4 = pygame.font.Font(None, 10*size )
    text4 = f4.render( 'your time is:'  , 1, (180, 180, 180))
    screen.blit(text4, (int(width/2 - 45*size ) , int(length/2 + 15*size)))

    f5 = pygame.font.Font(None, 10*size )
    text5 = f5.render( str(player_time) , 1, (180, 180, 180))
    screen.blit(text5, (int(width/2 - 2*size) , int(length/2 + 15*size)))

    
class Ball:
    
    def __init__(self, width, length):
        self.r = randint(10, 75)
        self.x = randint(self.r, width - self.r)
        self.y = randint(self.r, length - self.r)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255)) 
        
        
    def draw(self):   
        circle(screen, self.color, (self.x, self.y), self.r)
        
       
    def border_hit(self):
        if self.x < self.r or self.x > width - self.r :
            self.vx = - self.vx 
            
        if self.y < self.r or self.y > length - self.r:
            self.vy = -self.vy                    
    
            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.border_hit()


    def delete(self):
        self.r = 0

class Flower:
        
    def __init__(self, width, length):
        self.r = randint(8, 25)
        self.x = randint(self.r, width - self.r)
        self.y = randint(self.r, length - self.r)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255)) 
        self.r  = int(self.r/2)
        
        
    def draw(self):   
        circle(screen, self.color, (self.x + self.r, self.y), self.r)
        circle(screen, self.color, (self.x - self.r, self.y), self.r)
        circle(screen, self.color, (self.x, self.y + self.r), self.r)
        circle(screen, self.color, (self.x, self.y - self.r), self.r)
        circle(screen, (255-self.color[0], 255 - self.color[1], 255 - self.color[2]), (self.x, self.y ), self.r)
        
       
    def border_hit(self):
        if self.x < 2*self.r or self.x > width - 2*self.r :
            self.vx = -int(self.vx / 2)
            
        if self.y < 2*self.r or self.y > length - 2*self.r:
            self.vy = -int(self.vy / 2)   

            
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.border_hit()

        
    def special_move_0(self):
        self.vx = - self.vx
        self.vy = - self.vy
        self.border_hit()

    def special_move_1(self):
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.border_hit()

        
balls = [Ball(width, length) for i in range(number_of_balls)]
flowers = [Flower(width, length) for i in range(number_of_flowers)]

pygame.display.update()

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
                    
    for b in balls:    
        b.draw()
        b.move()

    for f in flowers:
        randfactor = randint(0, 10)
        f.draw()
        f.move()
        if randfactor == 1:
            f.special_move_0()
        elif randfactor == 2:
            f.special_move_1()
            

    
    for j, b in enumerate(balls):    
        if event.type == pygame.MOUSEBUTTONDOWN and ((b.x - event.pos[0])**2 + (b.y - event.pos[1])**2) < b.r**2:
            balls.pop(j)
            score += 5

    for j, f in enumerate(flowers):    
        if event.type == pygame.MOUSEBUTTONDOWN and((f.x +f.r - event.pos[0])**2 + (f.y - event.pos[1])**2 < f.r**2 or
                                                    (f.x -f.r - event.pos[0])**2 + (f.y - event.pos[1])**2 < f.r**2 or
                                                    (f.x - event.pos[0])**2 + (f.y + f.r - event.pos[1])**2 < f.r**2 or
                                                    (f.x - event.pos[0])**2 + (f.y - f.r- event.pos[1])**2 < f.r**2 ):
            flowers.pop(j)
            score += 10   
    
    pygame.display.update()
    screen.fill(BLACK)



    if frames < time*FPS and not(not balls and not flowers):
        frames += 1
    if  frames >= time*FPS or (not balls and not flowers) :  
        balls = []
        flowers = []
        player_time = round(frames/FPS, 2)
       
        text()

with open('results.txt', 'a') as bp:
    bp.write(player + "'s score is " + str(score) + 'in ' + str(player_time) + ' seconds' + '\n\n')
    bp.close()
                

pygame.quit()            
        
        
