import pygame
import sys
from game import *
from load_image import *

def show_ranking():
    clock = pygame.time.Clock()
    running = True

    try:
        with open('scores.csv', 'r') as file:
            scores = [line.strip().split() for line in file.readlines()]
    except FileNotFoundError:
        scores = []
    print(scores)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False


        SCREEN.fill((0, 0, 0))
        SCREEN.blit(fondo_rankin,(500,0))
        font = pygame.font.Font(None, 36)
        y_offset = 100
        for score in scores:
            score_text = font.render(f'{score[0]}: {score[1]}', True, (255, 255, 255))
            SCREEN.blit(score_text, (100, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(60)
