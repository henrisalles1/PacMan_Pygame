import pygame
from constantes import *

pygame.init()
tela_teste = pygame.display.set_mode((WIDTH_TELA, HEIGHT_TELA), 0)
class PacMan:
    def __init__(self):
        self.centro_x: int = WIDTH_TELA//2
        self.centro_y: int = HEIGHT_TELA//2
        self.tamanho: int = TAMANHO
        self.raio: int = self.tamanho//2

    def pintar_virado_direita(self, tela):
        # Desenho de Corpo
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio)

        # Desenho de Boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Desenho de olho
        olho_x: int = int(self.centro_x + self.raio / 4)
        olho_y: int = int(self.centro_y - self.raio / 2)
        olho_raio = int(self.raio / 8)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)


if __name__=='__main__':
    pacman = PacMan()

    while True:
        # Pintar a tela
        pacman.pintar_virado_direita(tela_teste)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


