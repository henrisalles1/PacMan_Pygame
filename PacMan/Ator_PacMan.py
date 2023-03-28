import pygame
from constantes import *


class PacMan:
    def __init__(self, tamanho):
        self.coluna: int = 1
        self.linha: int = 1
        self.centro_x: int = WIDTH_TELA//2
        self.centro_y: int = HEIGHT_TELA//2
        self.tamanho: int = tamanho
        self.raio: int = self.tamanho // 2
        self.vx: int = 0
        self.vy: int = 0

    def calcular_regras(self):
        self.coluna += self.vx
        self.linha += self.vy
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def pintar(self, tela):
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


    def processar_eventos(self, eventos):
        self.movimentos_por_tecla(eventos)
    def movimentos_por_tecla(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vx = 1
                if e.key == pygame.K_LEFT:
                    self.vx = -1
                if e.key == pygame.K_UP:
                    self.vy = -1
                if e.key == pygame.K_DOWN:
                    self.vy = 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or pygame.K_LEFT:
                    self.vx = 0
                if e.key == pygame.K_DOWN or pygame.K_UP:
                    self.vy = 0