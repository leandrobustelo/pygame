import pygame
from funciones.seting import SCREEN_SIZE,SCREEN_LASER

fondo_game_over=pygame.image.load("./src/imagenes/zombies1.png")
fondo_game_over=pygame.transform.scale(fondo_game_over,SCREEN_SIZE)

fondo_rankin=pygame.image.load("./src/imagenes/zombies2.png")
fondo_rankin=pygame.transform.scale(fondo_rankin,(500,500))

fondo_menu=pygame.image.load("./src/imagenes/ultimafo.png")
fondo_menu=pygame.transform.scale(fondo_menu,SCREEN_SIZE)
icono=pygame.image.load("./src/imagenes/foto.png")

fondo_juego=pygame.image.load("./src/imagenes/nivel1.png")
fondo_juego=pygame.transform.scale(fondo_juego,SCREEN_SIZE)

bala=pygame.image.load("./src/imagenes/bala.png")
bala=pygame.transform.scale(bala,SCREEN_LASER)

imagen_personaje_de=pygame.image.load("./src/imagenes/personaje.png")
imagen_enemi=[pygame.image.load("./src/imagenes/animacion_enemi/enemi1.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi2.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi3.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi4.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi5.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi6.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi7.png"),
              pygame.image.load("./src/imagenes/animacion_enemi/enemi8.png"),]

imagen_personaje_iz=pygame.image.load("./src/imagenes/personajeiz.png")
imagen_personaje_salto=pygame.image.load("./src/imagenes/salto.png")

im_move_derecha=[pygame.image.load("./src/imagenes/animacion_der/an1.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an2.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an3.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an4.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an5.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an6.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an7.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an8.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an9.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an10.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an11.png"),
                 pygame.image.load("./src/imagenes/animacion_der/an12.png")]

im_move_izquierda=[pygame.image.load("./src/imagenes/animacion_izq/an1.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an2.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an3.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an4.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an5.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an6.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an7.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an8.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an9.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an10.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an11.png"),
                 pygame.image.load("./src/imagenes/animacion_izq/an12.png")]


# rutas_imagenes=leer_rutas_imagenes()

# fondo_game_over=cargar_imagenes(rutas_imagenes["fondo_game_over"])
# fondo_game_over=pygame.transform.scale(fondo_game_over,SCREEN_SIZE)

# fondo_menu=cargar_imagenes(rutas_imagenes["fondo_menu"])
# fondo_menu=pygame.transform.scale(fondo_menu,SCREEN_SIZE)
# icono=cargar_imagenes(rutas_imagenes["icono"])

# fondo_juego=cargar_imagenes(rutas_imagenes["fondo_juego"])
# fondo_juego=pygame.transform.scale(fondo_juego,SCREEN_SIZE)

# bala=cargar_imagenes(rutas_imagenes["bala"])
# bala=pygame.transform.scale(bala,SCREEN_LASER)

# imagen_personaje_de=cargar_imagenes(rutas_imagenes["imagen_personaje_de"])
# imagen_enemi=cargar_imagenes(rutas_imagenes["imagen_enemi"])

# imagen_personaje_iz=cargar_imagenes(rutas_imagenes["imagen_personaje_iz"])
# imagen_personaje_salto=cargar_imagenes(rutas_imagenes["imagen_personaje_salto"])

# im_move_derecha=cargar_imagenes(rutas_imagenes["im_move_derecha"])

# im_move_izquierda=cargar_imagenes(rutas_imagenes["im_move_izquierda"])