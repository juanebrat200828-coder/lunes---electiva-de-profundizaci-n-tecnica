
import pygame
import sys


pygame.init()


ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Introducción a Pygame - Juan Esteban Ebrat López")


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


fuente = pygame.font.SysFont("Arial Black", 40)


texto_superficie = fuente.render("Juan Esteban Ebrat López", True, BLANCO)
texto_rect = texto_superficie.get_rect()


texto_rect.center = (ANCHO // 2, ALTO // 2)


while True:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    ventana.fill(NEGRO)


    ventana.blit(texto_superficie, texto_rect)


    pygame.display.flip()

