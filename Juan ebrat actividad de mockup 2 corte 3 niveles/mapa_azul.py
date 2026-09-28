import sys
import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mapa de Bomberman - azul")
reloj = pygame.time.Clock()


TAM = 30
MAPA_X = 25
MAPA_Y = 140


mapa = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,2,0,0,2,2,2,0,0,2,2,0,2,0,2,2,0,2,0,0,0,0,1],
    [1,0,1,2,1,2,1,2,1,0,1,2,1,2,1,2,1,2,1,2,1,2,1,0,1],
    [1,2,2,2,2,2,2,2,0,2,0,2,0,0,2,2,0,0,0,2,0,0,2,2,1],
    [1,0,1,0,1,2,1,2,1,2,1,2,1,0,1,2,1,2,1,2,1,0,1,0,1],
    [1,2,2,2,0,2,2,2,2,2,0,0,2,2,2,2,0,0,2,0,2,2,0,2,1],
    [1,2,1,2,1,2,1,0,1,2,1,0,1,0,1,0,1,0,1,0,1,2,1,2,1],
    [1,2,2,0,2,2,2,2,2,2,2,0,0,2,2,2,2,2,0,0,0,0,2,0,1],
    [1,0,1,0,1,2,1,2,1,2,1,0,1,2,1,2,1,0,1,2,1,2,1,0,1],
    [1,0,0,2,2,2,2,0,2,2,2,2,2,2,2,2,0,2,2,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


COLOR_FONDO = (20, 30, 60)
COLOR_LIBRE = (205, 225, 255)
COLOR_INDESTRUCTIBLE = (60, 80, 140)
COLOR_DESTRUCTIBLE = (255, 150, 40)
COLOR_BORDE = (170, 90, 20)
COLOR_LINEA = (150, 170, 210)

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(COLOR_FONDO)

    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            x = MAPA_X + columna * TAM
            y = MAPA_Y + fila * TAM
            celda = mapa[fila][columna]

            
            pygame.draw.rect(pantalla, COLOR_LIBRE, (x, y, TAM, TAM))

            if celda == 1:
                pygame.draw.rect(pantalla, COLOR_INDESTRUCTIBLE, (x, y, TAM, TAM))
            elif celda == 2:
                pygame.draw.rect(pantalla, COLOR_DESTRUCTIBLE, (x + 3, y + 3, TAM - 6, TAM - 6))
                pygame.draw.rect(pantalla, COLOR_BORDE, (x + 3, y + 3, TAM - 6, TAM - 6), 2)

            
            pygame.draw.rect(pantalla, COLOR_LINEA, (x, y, TAM, TAM), 1)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
