import pygame
from pygame.locals import *
import random
from pygame import font

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
ENEMY_FIRE = pygame.constants.USEREVENT+1
pygame.time.set_timer(ENEMY_FIRE,700)

