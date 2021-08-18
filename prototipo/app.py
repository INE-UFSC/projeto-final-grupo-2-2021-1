# Vamos tentar reunir nesse aqreuivo as funcionalidades do programa
# De inicio é importante a gente apenas fazer o jogo funcionar e depois ir separando as coisas

import pygame
from personagem import Personagem
from cenario import Cenario
from pygame.locals import *
from cano import Cano
from itens import Itens

pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

item = Itens(780, 640, cenario.tela, 320)

cano1 = Cano(780, 640, cenario.tela)
cano2 = Cano(780, 640, cenario.tela)
cano3 = Cano(780, 640, cenario.tela)

passaro = Personagem(x=160, y=300)

listaObjetos = [cano1]

rodando = True
while rodando:

    clock.tick(fps)
    cenario.tela.fill((0, 0, 150))
    
    for parte in listaObjetos:
        parte.desenha_objeto()
        if not passaro.game_over:  # caso ocorra um "game over" os canos param de mover
            parte.move()

    if cano1.x == 320:
        item.posicao_tela()
        cano2.tamanho_cano()
        listaObjetos.append(item)
        listaObjetos.append(cano2)
    if cano1.x < -40:
        cano1.destruir()
        listaObjetos.remove(cano1)
    
    if cano2.x == 320:
        cano3.tamanho_cano()
        listaObjetos.append(cano3)
    if cano2.x < -40:
        cano2.destruir()
        listaObjetos.remove(cano2)

    if cano3.x == 320:
        cano1.tamanho_cano()
        listaObjetos.append(cano1)
    if cano3.x < -40:
        cano3.destruir()
        listaObjetos.remove(cano3)

    if item.x < -40:
        item.destruir()
        listaObjetos.remove(item)
    
    passaro.desenha_personagem(cenario.tela)
    passaro.mover()

    passaro.colisao(canos=cano1.gera_retangulo())
    passaro.colisao(canos=cano2.gera_retangulo())
    passaro.colisao(canos=cano3.gera_retangulo())

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not passaro.voando and not passaro.game_over:
            if evento.key == pygame.K_UP:
                passaro.voando = True

    pygame.display.update()

pygame.quit()
