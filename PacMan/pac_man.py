import pygame


pygame.init()
# Cores
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

# limites de tela
WIDTH_TELA = 680
HEIGHT_TELA = 420
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

