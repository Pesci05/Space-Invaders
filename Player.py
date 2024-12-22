import pygame
from costanti import *
from pygame.locals import *
from Proiettili import *
import time

class Player(pygame.sprite.Sprite):
    def __init__(self,):
        super(Player,self).__init__()
        self.surf = pygame.Surface([40,25])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = ((SCREEN_WIDTH-self.surf.get_width())/2,
                      SCREEN_HEIGHT-20
                      )
        )
        self.speed = 0.001
        self.point = 0
    
    def update(self, pressedKeys):
        time.sleep(self.speed)
        if pressedKeys[K_d]:
            self.rect.move_ip(1,0)
       
        if pressedKeys[K_a]:
            self.rect.move_ip(-1,0)

        if self.rect.right >= SCREEN_WIDTH-5:
            self.rect.right = SCREEN_WIDTH -5
        if self.rect.left <= 5:
            self.rect.left = 5
    
    def fire(self):
        return Proiettili(self.rect.centerx,self.rect.centery)