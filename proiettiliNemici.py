import pygame
from costanti import *
import asyncio

class ProiettiliNemici(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(ProiettiliNemici,self).__init__()
        self.surf = pygame.Surface([10,10])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (x,y))
        #self.speed = 0,5
    
    def update(self):
            self.rect.move_ip(0,1)
            if self.rect.top >= SCREEN_HEIGHT:
                self.kill()