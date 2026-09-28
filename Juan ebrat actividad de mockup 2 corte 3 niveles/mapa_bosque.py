import sys
import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mapa de Bomberman - bosque")
reloj = pygame.time.Clock()


TAM = 30
MAPA_X = 25
MAPA_Y = 140


mapa = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,2,0,2,0,0,2,2,0,2,2,0,0,0,0,0,2,0,0,0,0,0,1],
    [1,0,0,0,2,0,0,2,2,0,1,1,0,1,1,0,0,0,0,0,2,0,0,0,1],
    [1,0,0,2,2,2,0,0,1,1,0,2,2,0,2,1,1,0,2,0,2,2,0,0,1],
    [1,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,2,1,1,0,2,0,0,0,1],
    [1,0,0,2,1,1,0,0,2,2,2,2,0,2,2,2,0,2,2,1,1,0,0,2,1],
    [1,2,0,0,2,0,1,1,2,2,2,2,2,0,2,2,0,1,1,0,2,2,0,0,1],
    [1,2,0,2,0,2,0,0,1,1,0,2,0,0,0,1,1,0,0,2,2,0,2,2,1],
    [1,0,0,0,2,2,0,2,0,0,1,1,2,1,1,2,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,2,2,0,0,0,2,0,0,2,0,0,2,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


COLOR_FONDO = (25, 55, 40)
COLOR_LIBRE = (225, 240, 205)
COLOR_INDESTRUCTIBLE = (110, 75, 45)
COLOR_DESTRUCTIBLE = (200, 55, 55)
COLOR_BORDE = (120, 30, 30)
COLOR_LINEA = (170, 195, 150)

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
                centro = (x + TAM // 2, y + TAM // 2)
                pygame.draw.circle(pantalla, COLOR_DESTRUCTIBLE, centro, TAM // 2 - 3)
                pygame.draw.circle(pantalla, COLOR_BORDE, centro, TAM // 2 - 3, 2)

           
            pygame.draw.rect(pantalla, COLOR_LINEA, (x, y, TAM, TAM), 1)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
