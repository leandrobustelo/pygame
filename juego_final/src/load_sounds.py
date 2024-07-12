import pygame
from funciones.funciones import *
pygame.init()

rutas_sonidos=leer_rutas_imagenes()
sound_shot=pygame.mixer.Sound(rutas_sonidos["sound_shot"])
sound_ataque=pygame.mixer.Sound(rutas_sonidos["sound_ataque"])
game_over=pygame.mixer.Sound(rutas_sonidos["game_over"])
son_P=(rutas_sonidos["son_P"])
son_game=(rutas_sonidos["son_game"])



