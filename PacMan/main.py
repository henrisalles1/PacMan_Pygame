from constantes import *
from cenario import Cenario
from Ator_PacMan import PacMan
from fantasma import Fantasma

tela = pygame.display.set_mode((WIDTH_TELA, HEIGHT_TELA), 0)

if __name__ == '__main__':
    tamanho = TAMANHO
    pacman = PacMan(tamanho)
    blinky = Fantasma(VERMELHO, tamanho)
    inky = Fantasma(CIANO, tamanho)
    clyde = Fantasma(LARANJA, tamanho)
    pinky = Fantasma(ROSA, tamanho)
    cenario = Cenario(tamanho, pacman)
    cenario.add_movivel(blinky)
    cenario.add_movivel(inky)
    cenario.add_movivel(clyde)
    cenario.add_movivel(pinky)
    cenario.add_movivel(pacman)

    while True:
        # Calcular Regras
        pacman.calcula_regra()
        blinky.calcula_regra()
        inky.calcula_regra()
        clyde.calcula_regra()
        pinky.calcula_regra()
        cenario.calcula_regra()

        # Pintar tela
        tela.fill(PRETO)
        cenario.pintar(tela)
        pacman.pintar(tela)
        blinky.pintar(tela)
        inky.pintar(tela)
        clyde.pintar(tela)
        pinky.pintar(tela)

        # Ajuste de tela, apos pintura
        pygame.display.update()
        pygame.time.delay(100)

        # Captura Eventos
        eventos = pygame.event.get()
        pacman.processa_evento(eventos)
        cenario.processa_evento(eventos)


