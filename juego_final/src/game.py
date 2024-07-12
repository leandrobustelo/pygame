import pygame
import sys
from funciones.funciones import *
from load_image import *
from load_sounds import *

SCREEN=pygame.display.set_mode((WIDHT,HEIGHT))
def game():
    pygame.mixer_music.unload()
    pygame.mixer_music.load(son_game)
    pygame.mixer_music.play()
    
    pygame.time.set_timer(NEWCOINEVENT,1000)
    clock = pygame.time.Clock()
    fuente = pygame.font.SysFont(None,48)
    is_running=True
    move_lef=False
    move_right=False
    flag_move_der=True
    flag_move_izq=False
    jumping = False
    playing_music=True
    enemis=[]
    lives=3
    score=0
    current_image = 0
    current_enemi=0
    lasers=[]
    player_direccion="right"
    personaje=crear_player(imagen_personaje_de)
    personaje["direccion"]=player_direccion
    
        
    while is_running==True:
       
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==QUIT:
                is_running=False

            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    move_lef=True
                    player_direccion="left"
                if event.key==K_RIGHT:
                    move_right=True
                    player_direccion="right"

                if event.key==K_UP and not jumping and (move_lef or move_right):
                    jumping=True
                    y_velocity = -jump_speed
                    flag_move_der=False
                    flag_move_izq=False


                if event.key==K_m:
                    if playing_music:
                        pygame.mixer_music.pause()
                        playing_music=False
                       
                    else:
                        pygame.mixer_music.unpause()
                        playing_music=True

                if event.key==K_f:
                    if len(lasers)==0:  
                        laser=crear_laser(personaje["rect"].midright)
                        laser["player_direccion"]=player_direccion
                        lasers.append(laser)
                        if(playing_music==True):
                            sound_shot.play()
                        
                if event.key==K_p:
                    pygame.mixer_music.pause()
                    pausar_game(K_p,SCREEN,"-- PAUSA --",fuente,SCREEN_CENTER)
                    if playing_music:
                        pygame.mixer_music.unpause()

            if event.type==KEYUP:
                if event.key==K_LEFT:
                    move_lef=False
                if event.key==K_RIGHT:
                    move_right=False
                
            if event.type==NEWCOINEVENT:
                nes_enemi=create_enemi()
                enemis.append(nes_enemi)

        if move_lef and  personaje["rect"].left > 0:
            personaje["rect"].x -= speed
            current_image += 1
            if current_image >= len(im_move_derecha):
                current_image = 0
            if personaje["rect"].left < 0:
                personaje["rect"].left=0

        if move_right and personaje["rect"].right < WIDHT:
            personaje["rect"].x += speed
            current_image += 1
            if current_image >= len(im_move_derecha):
                current_image = 0
                
            if personaje["rect"].right > WIDHT:
                personaje["rect"].right=WIDHT

        if jumping :
            personaje["rect"].top += y_velocity
            y_velocity += gravity
            
            if personaje["rect"].bottom >= ground_level:
                personaje["rect"].bottom = ground_level
                jumping = False
                y_velocity = 0 
            
        for enemi in enemis:
                enemi["rect"].move_ip(enemi["speed"],0)
                current_enemi += 1
                if current_enemi >= len(imagen_enemi):
                    current_enemi = 0
                if(enemi["rect"].left > WIDHT):
                    enemi["rect"].right=0

        for laser in lasers:
            if laser["player_direccion"]=="right":
                    
                laser["rect"].move_ip(laser["speed"],0)
                if(laser["rect"].left >WIDHT):
                    lasers.remove(laser)
                    
                
            elif laser["player_direccion"]=="left":
                    
                laser["rect"].move_ip(-laser["speed"],0)
                if(laser["rect"].right < 0):
                    lasers.remove(laser)
                    
        for enemi in enemis[:]:   
                if(detectar_colision(enemi["rect"],personaje["rect"])):
                    lives-=1
                    enemis.remove(enemi)
                    if(playing_music==True):
                        sound_ataque.play()
                    if(lives==0):
                        is_running=False
                        game_over.play()
        
        for enemi in enemis[:]:
            for laser in lasers: 
                if laser:
                    if(detectar_colision(enemi["rect"],laser["rect"])):
                        enemis.remove(enemi)
                        lasers.remove(laser)
                        score+=1

        if(move_right==True):
            SCREEN.blit(im_move_derecha[current_image],personaje["rect"] )
            flag_move_der=True
            flag_move_izq=False

        elif flag_move_der==True:
            SCREEN.blit(imagen_personaje_de,personaje["rect"])
        
        if(move_lef==True):
            SCREEN.blit(im_move_izquierda[current_image],personaje["rect"])
            flag_move_izq=True
            flag_move_der=False
            
        elif flag_move_izq==True:
            SCREEN.blit(imagen_personaje_iz,personaje["rect"]) 
    
        for enemi in enemis:
            
            SCREEN.blit(imagen_enemi[current_enemi],enemi["rect"])
        
        for laser in lasers:
            SCREEN.blit(bala,laser["rect"])

        if(playing_music==False):
            mostrar_texto(SCREEN,"Mute",fuente,(50,HEIGHT-50)) 

        mostrar_texto(SCREEN,f"Score: {score}",fuente,POS_SCORE_TITLE)
        mostrar_texto(SCREEN,f"Lives: {lives}",fuente,POS_HIGH_TITLE)
        pygame.display.flip()  
        SCREEN.blit(fondo_juego,(0,0))
        
    from game_over import game_over_screen
    game_over_screen(SCREEN, score)