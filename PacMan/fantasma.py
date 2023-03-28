from base import *
from constantes import *
import random


class Fantasma(Element, Movivel):
    def __init__(self, cor, tamanho):
        self.coluna = COL_FAN
        self.linha = LIN_FAN
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = 0
        self.cor = cor
        self.tamanho = tamanho

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px: int = int(self.coluna * self.tamanho)
        py: int = int(self.linha * self.tamanho)
        # Corpo
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        # Olho
        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x: int = int(px + fatia * 2.5)
        olho_e_y: int = int(py + fatia * 2.5)

        olho_d_x: int = int(px + fatia * 5.5)
        olho_d_y: int = int(py + fatia * 2.5)

        pygame.draw.circle(tela, BRANCO, (olho_e_x, olho_e_y), olho_raio_ext, 8)
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y), olho_raio_int, 8)
        pygame.draw.circle(tela, BRANCO, (olho_d_x, olho_d_y), olho_raio_ext, 8)
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y), olho_raio_int, 8)

    def calcula_regra(self):
        if self.direcao == UP:
            self.linha_intencao -= self.velocidade
        elif self.direcao == DOWN:
            self.linha_intencao += self.velocidade
        elif self.direcao == LEFT:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == RIGHT:
            self.coluna_intencao += self.velocidade

    def muda_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)
    def esquina(self, direcoes):
        self.muda_direcao(direcoes)

    def aceita_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusa_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.muda_direcao(direcoes)

    def processa_evento(self, evento):
        pass
