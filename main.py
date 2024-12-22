import pygame
from costanti import *
from pygame.locals import *
import random
import time
from Player import *
from pygame import font
from nemico import *

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
clock.tick(30)

running = True
gameon = False

player = Player()
proiettiliP = pygame.sprite.Group()
proiettiliN = pygame.sprite.Group()
nemici = pygame.sprite.Group()
#powerups = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemies = []

screen.fill((0, 0, 0))
for y in range(0,5):
    row = []
    for x in range(0,8):
        tf = random.randint(0,y+3)
        e = Enemy(x,y,tf)
        nemici.add(e)
        all_sprites.add(e)
        row.append(e)
    enemies.append(row)
    
enemies.reverse()
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            #il giocatore è uscito perchè ha schiacciato ESC
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                p = player.fire()
                proiettiliP.add(p)
                all_sprites.add(p)
        elif event.type == ENEMY_FIRE:
            r = enemies[0]
            i= 0
            c = 0

            while c < 4 and i < len(r):
                p = r[i].fire()
                if p is not None:
                    proiettiliN.add(p)
                    all_sprites.add(p)
                    c+=1
                i+=1
                
            #for e in r:
            #    p=e.fire()
            #   if p is not None:
            #        proiettiliN.add(p)
            #        all_sprites.add(p)


        #giocatore chiude la finstra tramite la 'x'
        elif event.type == pygame.QUIT:
            running = False
        
    
    
    pressed_keys = pygame.key.get_pressed()

    if pygame.sprite.spritecollideany(player,proiettiliN):
        player.kill()
        pygame.quit()
    
    for j,r in enumerate(enemies,0):
        for i,e in enumerate(r,0): 
            if pygame.sprite.spritecollideany(e,proiettiliP):
                
                enemies[j].pop(i)
                e.kill()
     
    player.update(pressed_keys)

    for p in proiettiliN:
        p.update()
    for p in proiettiliP:
        p.update()
    #disegnare sulla finestra
    screen.fill((0, 0, 0))
    for s in all_sprites:
        screen.blit(s.surf, s.rect)

    pygame.display.set_caption("SPACE INVADERS")
    pygame.display.flip()

pygame.quit()