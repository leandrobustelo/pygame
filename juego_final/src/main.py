import pygame
import sys
from game import *
from ranking import show_ranking
from funciones.funciones import *


pygame.init()

pygame.display.set_caption('Ciudad Zombie')
pygame.display.set_icon(icono)
fuente = pygame.font.Font("./src/funciones/dash-horizon.otf",48)
texto_principal=fuente.render(f"CIUDAD ZOMBIE ",True,WHITE,BLACK)
pygame.mixer_music.load(son_P)

def main_menu():
    import sys
    pygame.mixer_music.play()
    
    while True:
        SCREEN.blit(fondo_menu,(0,0))
        mouse_over_button = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        SCREEN.blit(texto_principal,(340,50))

        if draw_button(SCREEN,fuente,"Start Game", pygame.Rect(340, 200, 300, 50), RED, YELLOW,game):
            mouse_over_button = True
        if draw_button(SCREEN,fuente,"Ranking", pygame.Rect(340, 300, 300, 50), RED, YELLOW,show_ranking):
            mouse_over_button = True
        if draw_button(SCREEN,fuente,"Exit", pygame.Rect(340, 400, 300, 50), RED, YELLOW,quit_game):
            mouse_over_button = True
        
        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
