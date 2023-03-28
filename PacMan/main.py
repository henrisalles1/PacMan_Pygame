import pygame
from constantes import *
from cenario import Cenario
from Ator_PacMan import PacMan


pygame.init()
tela = pygame.display.set_mode((WIDTH_TELA, HEIGHT_TELA), 0)


if __name__ == '__main__':
    tamanho = TAMANHO
    pacman = PacMan(tamanho)
    cenario = Cenario(tamanho)

    while True:
        # Calcular Regras
        pacman.calcular_regras()

        # Pintar tela
        tela.fill(PRETO)
        cenario.pintar(tela)
        pacman.pintar(tela)
        pygame.display.update()
        pygame.time.delay(100)

        # Captura Eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)


