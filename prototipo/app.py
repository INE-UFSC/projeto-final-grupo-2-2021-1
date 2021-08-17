# Vamos tentar reunir nesse aqreuivo as funcionalidades do programa
# De inicio é importante a gente apenas fazer o jogo funcionar e depois ir separando as coisas

import pygame, sys
from personagem import Personagem
from cano import Cano
from cenario import Cenario
from pygame.locals import *


pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

passaro = Personagem(x=150, y=300)

canos = Cano(pygame.image.load('projeto-final-grupo-2-2021-1-main/prototipo/teste.png'))
spawncano = pygame.USEREVENT
pygame.time.set_timer(spawncano, 2000)

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
        if evento.type == spawncano:
            canos.lista_canos.append(canos.criar_cano())
            print(canos.lista_canos)
    pygame.display.update()

pygame.quit()
