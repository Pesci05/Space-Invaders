import pygame
from costanti import *
from pygame.locals import *
import random
import asyncio
from Player import *
from pygame import font

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
clock.tick(30)

running = True
gameon = False

player = Player()
proiettili = pygame.sprite.Group()
nemici = pygame.sprite.Group()
#powerups = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            #il giocatore è uscito perchè ha schiacciato ESC
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                p = player.fire()
                proiettili.add(p)
                all_sprites.add(p)
        
        #giocatore chiude la finstra tramite la 'x'
        elif event.type == pygame.QUIT:
            running = False
        
    

    pressed_keys = pygame.key.get_pressed()
    asyncio.run(player.update(pressed_keys))

    for p in proiettili:
        p.update()

    #disegnare sulla finestra
    screen.fill((0, 0, 0))
    for s in all_sprites:
        screen.blit(s.surf, s.rect)

    pygame.display.set_caption("SPACE INVADERS")
    pygame.display.flip()

pygame.quit()