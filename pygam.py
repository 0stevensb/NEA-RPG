import pygame 
import random
import sys
from pygame.locals import *
pygame.init()
screen_width, screen_height = 1200, 500
screen = pygame.display.set_mode((screen_width, screen_height))
running=True
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
class button():
    def __init__(self,ID,x,y):
        self.colour=red
        self.selected=False
        self.ID=ID
        self.x=x
        self.y=y
        self.greened=False
    def checkifselected(self,currentselected):
        if currentselected==self.ID:
            if not self.greened:
             self.colour=blue
            self.selected=True
        else:
            if not self.greened:
             self.colour=red
        self.selected=False
        
buttons=[button(0,50,100),button(1,200,100)]
selected=0
cooldown=0
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in buttons:
        i.checkifselected(selected)
        pygame.draw.rect(screen, i.colour, (i.x,i.y,100,100), 100,)
        
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and selected>0 and cooldown==0:
                selected -= 1
                cooldown=10
            if event.key == pygame.K_RIGHT and selected<len(buttons)-1 and cooldown==0:
                selected += 1
                cooldown=10
            if event.key == pygame.K_z and i.selected:
                i.colour=green
                i.greened=True
    if cooldown>0:
        cooldown-=1
    pygame.display.flip()
    # Control the game frame rate
    pygame.time.Clock().tick(30)
    pygame.event.pump()
# Quit pygame
pygame.quit()