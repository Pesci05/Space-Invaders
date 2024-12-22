import pygame
from costanti import *
from pygame.locals import *
from Proiettili import *
import time

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface([50,25])
        if y == 0:
            self.surf.fill((255,255,255))
        elif y == 1:
            self.surf.fill((255,000,000))
        elif y == 2:
            self.surf.fill((000,255,000))
        elif y == 3:
            self.surf.fill((000,000,255))
        elif y == 4:
            self.surf.fill((255,000,255))
            

        self.rect = self.surf.get_rect(
            topleft = (
                 5+(x*40),
                 5+(y*25)
            )
        )
        self.speed = 0.001