import pygame


pygame.init()

# Cores
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL_ESCURO = (0, 0, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CIANO = (0, 255, 255)
AZUL = (30, 30, 255)
LARANJA = (255, 140, 0)
ROSA = (255, 140, 140)

# limites de tela
WIDTH_TELA: int = 750
HEIGHT_TELA: int = 600

# Ator PacMan
VELOCIDADE: int = 1
VIDAS = 5

# Proporcoes
CELULAS = 30
TAMANHO = 600 // 30

FONTE = pygame.font.SysFont("arial", 20, True, False)
FONTE_P = pygame.font.SysFont("arial", 25, True, False)

# Direcoes Fantasma
STAY = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# Posicoes iniciais
LIN_PAC = 1
COL_PAC = 1
LIN_FAN = 15
COL_FAN = 13
