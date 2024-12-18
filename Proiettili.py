import pygame
from costanti import *
import asyncio

class Proiettili(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Proiettili,self).__init__()
        self.surf = pygame.Surface([10,10])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (x,y))
        #self.speed = 0,5
    
    def update(self):
        self.rect.move_ip(0,-2)

        if self.rect.top <= 0:
            self.kill()