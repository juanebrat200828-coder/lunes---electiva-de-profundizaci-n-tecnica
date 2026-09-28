import sys
import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mapa de Bomberman - morado")
reloj = pygame.time.Clock()


TAM = 30
MAPA_X = 25
MAPA_Y = 140


mapa = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,2,0,0,2,2,2,0,0,1],
    [1,0,0,0,2,0,2,0,2,2,0,2,2,0,0,2,0,0,0,2,0,0,0,0,1],
    [1,0,2,1,2,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,0,2,1],
    [1,0,2,2,0,0,1,2,2,2,2,2,2,0,2,2,2,2,1,2,0,0,2,0,1],
    [1,2,0,1,0,2,0,2,2,2,2,0,0,2,2,2,2,2,2,0,2,1,2,2,1],
    [1,0,2,0,0,0,1,2,0,0,2,2,2,2,2,2,2,0,1,2,2,0,0,2,1],
    [1,0,0,1,0,2,1,1,1,1,1,1,0,1,1,1,1,1,1,2,2,1,0,0,1],
    [1,0,2,0,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,0,0,2,2,0,1],
    [1,0,0,0,2,0,0,2,0,0,0,0,2,2,2,0,2,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


COLOR_FONDO = (45, 25, 70)
COLOR_LIBRE = (245, 225, 245)
COLOR_INDESTRUCTIBLE = (125, 85, 175)
COLOR_X = (70, 40, 110)
COLOR_DESTRUCTIBLE = (250, 205, 55)
COLOR_BORDE = (170, 120, 20)
COLOR_LINEA = (215, 190, 220)

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
                pygame.draw.line(pantalla, COLOR_X, (x + 5, y + 5), (x + TAM - 5, y + TAM - 5), 3)
                pygame.draw.line(pantalla, COLOR_X, (x + TAM - 5, y + 5), (x + 5, y + TAM - 5), 3)
            elif celda == 2:
                rombo = [(x + TAM // 2, y + 3), (x + TAM - 3, y + TAM // 2),
                         (x + TAM // 2, y + TAM - 3), (x + 3, y + TAM // 2)]
                pygame.draw.polygon(pantalla, COLOR_DESTRUCTIBLE, rombo)
                pygame.draw.polygon(pantalla, COLOR_BORDE, rombo, 2)

            
            pygame.draw.rect(pantalla, COLOR_LINEA, (x, y, TAM, TAM), 1)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
