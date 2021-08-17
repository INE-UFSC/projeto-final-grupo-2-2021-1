# Vamos tentar reunir nesse aqreuivo as funcionalidades do programa
# De inicio é importante a gente apenas fazer o jogo funcionar e depois ir separando as coisas

import pygame
from personagem import Personagem
from cenario import Cenario
from pygame.locals import *


pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

passaro = Personagem(x=350, y=300)

rodando = True
while rodando:

    clock.tick(fps)
    cenario.tela.fill((0, 0, 150))
    passaro.desenha_personagem(cenario.tela)
    passaro.mover()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not passaro.voando and not passaro.game_over:
            if evento.key == pygame.K_UP:
                passaro.voando = True

    pygame.display.update()

pygame.quit()
