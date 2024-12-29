import pygame
from costanti import *
from pygame.locals import *
import random
import time
import time
from Player import *
from pygame import font
from nemico import *
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

for y in range(0,5):
    row = []
    for x in range(0,8):
        e = Enemy(x,y)
        nemici.add(e)
        all_sprites.add(e)
        row.append(e)
    enemies.append(row)
        
screen.fill((0, 0, 0))


killRemain = 8
rowKill = 4

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

            for e in range(len(enemies[rowKill])):
                for r in range(len(enemies)-1):
                    #print(len(enemies))
                    if enemies[r+1][e] is None:
                        p = enemies[r][e].fire()
                        if p is not None:
                            proiettiliN.add(p)
                            all_sprites.add(p)
                    elif r+1 == len(enemies)-1:
                        
                        p = enemies[r+1][e].fire()
                        if p is not None:
                            proiettiliN.add(p)
                            all_sprites.add(p)
                     

                
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
    
    for i,r in enumerate(enemies,0):
        for j,e in enumerate(r,0): 
            for p in proiettiliP:
                if pygame.sprite.collide_rect(e,p):
                    if i == rowKill:
                        e.kill()
                        p.kill()
                        enemies[i].pop(j)
                        killRemain -= 1
     

    if killRemain <= 0:
        killRemain = 7
        enemies.pop(rowKill)
        if rowKill-1 >= 0:
            rowKill -= 1
            killRemain = len(enemies[rowKill])
        else:
            pygame.quit()


    
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