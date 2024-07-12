import pygame
from funciones.seting import *
from pygame.locals import *

def comenzar_game(tecla):
    """
    Espera a que se presione una tecla específica para comenzar el juego.

    Args:
        tecla (int): Código de la tecla que debe ser presionada para continuar.
    """
    continuar=True
    while continuar:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==tecla:
                    continuar=False

def random_color()->tuple[int,int,int]:
    from random import randint
    """
    Genera un color aleatorio.

    Returns:
        tuple[int, int, int]: Una tupla con valores RGB aleatorios.
    """
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return (r,g,b)

def crear_block(imagen=None ,left=0,top=0,widht=50,height=80,color=WHITE,dir=3,borde=0,radio=-1):
    """
    Crea un bloque con atributos específicos.

    Args:
        imagen (pygame.Surface): Imagen opcional para el bloque.
        left (int): Posición izquierda del bloque.
        top (int): Posición superior del bloque.
        widht (int): Ancho del bloque.
        height (int): Altura del bloque.
        color (tuple): Color del bloque.
        dir (int): Dirección del bloque.
        borde (int): Grosor del borde.
        radio (int): Radio de redondeo de las esquinas del bloque.

    Returns:
        dict: Diccionario con las propiedades del bloque.
    """
    return {"rect":pygame.Rect(left,top,widht,height),"color":color,"dir":dir,"borde":borde,"radio":radio,"img":imagen}

def crear_player(imagen:None):
    """
    Crea el jugador con una imagen opcional.

    Args:
        imagen (pygame.Surface): Imagen opcional para el jugador.

    Returns:
        dict: Diccionario con las propiedades del jugador.
    """
    if imagen:
        imagen=pygame.transform.scale(imagen,(block_widht,block_widht))
    
    return crear_block(imagen,550,400,color=random_color())


def create_enemi(imagen=None,visible=True):
    from random import randint
    """
    Crea un enemigo con una imagen opcional y velocidad aleatoria.

    Args:
        imagen (pygame.Surface): Imagen opcional para el enemigo.
        visible (bool): Si el enemigo es visible o no.

    Returns:
        dict: Diccionario con las propiedades del enemigo.
    """ 
    a=crear_block(imagen,-150,400,enemi_width,enemi_height,YELLOW,radio=enemi_width //2)
    a["speed"]=randint(minimo_number,maximo_number)
    return a

def detectar_colision(rect1,rect2)->bool:
    """
    Detecta si hay colisión entre dos rectángulos.

    Args:
        rect1 (pygame.Rect): Primer rectángulo.
        rect2 (pygame.Rect): Segundo rectángulo.

    Returns:
        bool: Verdadero si hay colisión, falso en caso contrario.
    """
    if  punto_en_rectangulo(rect1.topleft,rect2) or punto_en_rectangulo(rect1.topright,rect2) or punto_en_rectangulo(rect1.bottomleft,rect2) or punto_en_rectangulo(rect1.bottomright,rect2) or \
        punto_en_rectangulo(rect2.topleft,rect1) or punto_en_rectangulo(rect2.topright,rect1) or punto_en_rectangulo(rect2.bottomleft,rect1) or punto_en_rectangulo(rect2.bottomright,rect1):
        return True
    else:
        return False
    
def punto_en_rectangulo(punto,rectangulo):
    """
    Determina si un punto está dentro de un rectángulo.

    Args:
        punto (tuple): Coordenadas del punto en formato (x, y).
        rectangulo (Rect): Rectángulo con atributos top, bottom, left y right.

    Returns:
        bool: True si el punto está dentro del rectángulo, False en caso contrario.
    """
    x,y=punto
    if y >=rectangulo.top and y <=rectangulo.bottom and  x >=rectangulo.left and x <=rectangulo.right:
        return True
    else:
        return False

def mostrar_texto(superficie,texto,fuente,cordenada,color=WHITE,color_fondo=BLACK):
    """
    Muestra un texto en una superficie.

    Args:
        superficie: Superficie donde se mostrará el texto.
        texto (str): Texto a mostrar.
        fuente: Fuente del texto.
        cordenada: Coordenadas donde se posicionará el texto.
        color: Color del texto (por defecto WHITE).
        color_fondo: Color de fondo del texto (por defecto BLACK).
    """
    surface=fuente.render(texto,True,color,color_fondo)
    rect=surface.get_rect()
    rect.center=cordenada
    superficie.blit(surface,rect)

def crear_laser(midbottom=(0,0),color=RED):
    """
    Crea un objeto láser con ciertas propiedades.

    Args:
        midbottom (tuple): Coordenadas del láser en formato (x, y).
        color: Color del láser (por defecto RED).

    Returns:
        dict: Diccionario con las propiedades del láser.
    """
    rect=pygame.Rect(0,0,laser_width,lase_heigth)
    rect.midbottom=midbottom

    return {"rect":rect,"color":color,"speed":laser_speed}

def comenzar_game_click(rect_imagen:pygame.Rect):
    """
    Función que controla el inicio del juego al hacer click en una determinada área.

    Args:
        rect_imagen (Rect): Rectángulo de la imagen donde se puede hacer clic.
    """
    continuar=True
    while continuar:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if punto_en_rectangulo(event.pos,rect_imagen):
                        continuar=False
                        
def draw_button(screen,fuente,text, rect, color, hover_color, action=None):
    """
    Dibuja un botón interactivo en la pantalla.

    Args:
        screen: Pantalla donde se dibujará el botón.
        fuente: Fuente del texto en el botón.
        text (str): Texto en el botón.
        rect (Rect): Dimensiones y posición del botón.
        color: Color normal del botón.
        hover_color: Color del botón al pasar el ratón sobre él.
        action: Acción a realizar al hacer clic en el botón (por defecto None).

    Returns:
        bool: True si el botón está siendo señalado, False en caso contrario.
    """
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hovered = rect.collidepoint(mouse_pos)
    
    if hovered:
        pygame.draw.rect(screen, hover_color, rect)
        if click[0] == 1 and action:
            pygame.time.delay(200)
            action()
    else:
        pygame.draw.rect(screen, color, rect)
    
    text_surf = fuente.render(text, True, BLACK)
    screen.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, rect.y + (rect.height - text_surf.get_height()) // 2))
    
    return hovered

def quit_game():
    import sys  
    """
    Función para salir del juego.
    """
    pygame.quit()
    sys.exit()

def pausar_game(tecla,superficie,texto,fuente,cordenada:tuple):
    """
    Pausa el juego y muestra un texto en la pantalla.

    Args:
        tecla: Tecla que reanudará el juego.
        superficie: Superficie donde se mostrará el texto.
        texto (str): Texto a mostrar durante la pausa.
        fuente: Fuente del texto.
        cordenada (tuple): Coordenadas donde se posicionará el texto.
    """
    continuar=True
    mostrar_texto(superficie,texto,fuente,cordenada) 
    pygame.display.flip()  
    while continuar:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==tecla:
                    continuar=False
                    
def leer_rutas_imagenes():
    import json
    """
    Lee las rutas de imágenes desde un archivo JSON.

    Returns:
        dict: Diccionario con las rutas de las imágenes.
    """
    with open('sounds.json', 'r') as file:
            rutas = json.load(file)
    return rutas


