import pygame
from costanti import *
from pygame.locals import *
from Proiettili import *
import time
from proiettiliNemici import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,tf):
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
                 12+(x*60),
                 10+(y*40)
            )
        )
        self.timeFire = tf
        
        
    
    def fire(self):
        r = random.randint(0,1)
        if r == 0: 
            return ProiettiliNemici(self.rect.centerx,self.rect.centery)
        else:
            return None        
        