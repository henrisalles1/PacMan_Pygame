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
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao += self.vx
        self.linha_intencao += self.vy
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

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    def processar_eventos(self, eventos):
        self.movimentos_por_tecla(eventos)
    def movimentos_por_tecla(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vx = VELOCIDADE
                if e.key == pygame.K_LEFT:
                    self.vx = -VELOCIDADE
                if e.key == pygame.K_UP:
                    self.vy = -VELOCIDADE
                if e.key == pygame.K_DOWN:
                    self.vy = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or pygame.K_LEFT:
                    self.vx = 0
                if e.key == pygame.K_DOWN or pygame.K_UP:
                    self.vy = 0