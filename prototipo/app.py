# Vamos tentar reunir nesse aqreuivo as funcionalidades do programa
# De inicio é importante a gente apenas fazer o jogo funcionar e depois ir separando as coisas

import random
import pygame
from personagem import Personagem
from cenario import Cenario
from pygame.locals import *
from cano import Cano
from itens import Itens
from contador import Contador


pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

contador = Contador()

item = Itens(780, 640, cenario.tela, 320)

cano1 = Cano(780, 640, cenario.tela)
cano2 = Cano(780, 640, cenario.tela)
cano3 = Cano(780, 640, cenario.tela)

passaro = Personagem(x=160, y=300)

listaObjetos = [cano1]

rodando = True
while rodando:
    contador.contador_tempo()
 
    contador.fim_contagem()

    clock.tick(fps)
    cenario.tela.fill((0, 0, 150))
    
    for parte in listaObjetos:
        parte.desenha_objeto()
        if not passaro.game_over and passaro.voando:  # caso ocorra um "game over" os canos param de mover
            parte.move()

    if cano1.x == 320:
        if item.criado == False:
            if random.randint(1, 8) == 1:
               item.posicao_tela()
               listaObjetos.append(item)
        cano2.tamanho_cano()
        listaObjetos.append(cano2)
    if cano1.x < -40:
        cano1.destruir()
        listaObjetos.remove(cano1)
    
    if cano2.x == 320:
        if item.criado == False:
            if random.randint(1, 20) == 1:
               item.posicao_tela()
               listaObjetos.append(item)        
        cano3.tamanho_cano()
        listaObjetos.append(cano3)
    if cano2.x < -40:
        cano2.destruir()
        listaObjetos.remove(cano2)

    if cano3.x == 320:
        if item.criado == False:
            if random.randint(1, 20) == 1:
               item.posicao_tela()
               listaObjetos.append(item)
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

    # para conferir se o personagem coleta o item
    for objeto in listaObjetos:
        if isinstance(objeto, Itens):
            passaro.pegou_item(item=objeto, personagem=passaro)
    
    # controla o tempo de duração do efeito do item
    # ainda precisa ser melhorado, para que o personagem possa receber dois efeitos diferentes ao mesmo tempo 
    if item.timer is not None:  # verifica se o item já está ativo
        item.timer.contador_tempo()
        if item.timer.fim_contagem():  # verifica o tempo de duração do item
            # local para reverter mudanças dos itens, provavelmente vamos ter que implementar um método específico pra isso
            # caso queiram testar o funcionamento, descomentem a linha abaixo e a linha 65 do arquivo "itens"
            # passaro.tamanho = 35
            item.timer = None


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not passaro.voando and not passaro.game_over:
            if evento.key == pygame.K_UP:
                passaro.voando = True

    pygame.display.update()

pygame.quit()
