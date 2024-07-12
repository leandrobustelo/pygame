import pygame
import sys
from load_image import *

def game_over_screen(screen, score):
    clock = pygame.time.Clock()
    running = True

    # Guardar el puntaje en el archivo
    nombre = input("Ingresa tus iniciales: ")

    with open('scores.csv', 'a') as file:
        file.write(f'{nombre} {score}\n')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False
                from main import main_menu
                main_menu()

        
        screen.fill((0,0,0))
        screen.blit(fondo_game_over,(0,0))
        font = pygame.font.Font("./src/funciones/dash-horizon.otf",48)
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        prompt_text = font.render('Press Enter', True, (255, 255, 255))

        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 150))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 250))
        screen.blit(prompt_text, (screen.get_width() // 2 - prompt_text.get_width() // 2, 350))

        pygame.display.flip()
        clock.tick(60)
