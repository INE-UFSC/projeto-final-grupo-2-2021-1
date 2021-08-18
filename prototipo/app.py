# Vamos tentar reunir nesse aqreuivo as funcionalidades do programa
# De inicio é importante a gente apenas fazer o jogo funcionar e depois ir separando as coisas

import pygame
from personagem import Personagem
from cenario import Cenario
from pygame.locals import *
from cano import Cano

pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

cano1 = Cano(780, 640, cenario.tela)
cano2 = Cano(780, 640, cenario.tela)
cano3 = Cano(780, 640, cenario.tela)

passaro = Personagem(x=160, y=300)

listaCano = [cano1]

rodando = True
while rodando:

    clock.tick(fps)
    cenario.tela.fill((0, 0, 150))
    passaro.desenha_personagem(cenario.tela)
    passaro.mover()
    
    for parte in listaCano:
        parte.geraCano()
        parte.move()

    if cano1.x == 320:
        cano2.tamanhoCano()
        listaCano.append(cano2)
    if cano1.x < -40:
        cano1.destruir()
        listaCano.remove(cano1)
    
    if cano2.x == 320:
        cano3.tamanhoCano()
        listaCano.append(cano3)
    if cano2.x < -40:
        cano2.destruir()
        listaCano.remove(cano2)

    if cano3.x == 320:
        cano1.tamanhoCano()
        listaCano.append(cano1)
    if cano3.x < -40:
        cano3.destruir()
        listaCano.remove(cano3)


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not passaro.voando and not passaro.game_over:
            if evento.key == pygame.K_UP:
                passaro.voando = True

    pygame.display.update()

pygame.quit()
