import pygame
from constantes import *
from Ator_PacMan import PacMan


pygame.init()
tela = pygame.display.set_mode((WIDTH_TELA, HEIGHT_TELA), 0)

# variaveis de movimento
x: float = 10
y: float = 240
v: float = 0.5
vx: float = v
vy: float = v

while True:
    # Calcula regras
    x += vx
    if x > WIDTH_TELA or x < 0:
        vx *= -1
    y += vy
    if y > HEIGHT_TELA or y < 0:
        vy *= -1

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (x, y), 30, 0)
    pygame.display.update()

    # Eventos

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()


