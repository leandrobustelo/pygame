
import pygame
from pygame.locals import *


block_widht=100
block_height=100
WIDHT=1000
HEIGHT=500
speed=3
minimo_number=1
maximo_number=10
FPS=70
score=0
high_score=0
SCREEN_SIZE=(WIDHT,HEIGHT)
SCREEN_CENTER=(WIDHT//2,HEIGHT//2)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
CUSTOM=(157,208,230)
YELLOW=(255,255,0)
BLUE=(0,0,255)
enemi_width=50
enemi_height=80
jump_speed = 20
gravity = 1
y_velocity = None
y_pos=480
ground_level = y_pos
lase_heigth=20
laser_width=30
laser_speed=15
SCREEN_LASER=(laser_width,lase_heigth)
POS_TITLE=(WIDHT//2,100)
POS_SCORE_TITLE=(150,50)
POS_HIGH_TITLE=(WIDHT-150,50)
NEWCOINEVENT=USEREVENT+1