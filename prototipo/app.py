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
from pontuacao import Pontuacao
from itemTamanho import ItemTamanho
from itemInvencibilidade import ItemInvencibilidade

pygame.init() 

cenario = Cenario()
clock = pygame.time.Clock()
fps = 60

contador = Contador()

# para testar o funcionamento dos itens, substituir "Itens" abaixo por "ItemTamanho" ou "ItemInvencibilidade"
item_tamanho = ItemTamanho(780, 640, cenario.tela, 320)
item_invencibilidade = ItemInvencibilidade(780, 640, cenario.tela, 320)
lista_itens = [item_tamanho, item_invencibilidade]
item = random.choice(lista_itens)
# ainda precisamos pensar em uma forma de gerar aleatoriamente itens de ambos os tipos

ignorar_item = False

cano1 = Cano(780, 640, cenario.tela)
cano2 = Cano(780, 640, cenario.tela)
cano3 = Cano(780, 640, cenario.tela)

passaro = Personagem(x=160, y=300)

pontos_jogador = Pontuacao()

listaObjetos = [cano1]

rodando = True
while rodando:
    contador.contador_tempo()
    pontos_jogador.mostra_ponto(passaro.game_over)

    clock.tick(fps)
    cenario.tela.fill((0, 0, 150))
    
    for parte in listaObjetos:
        parte.desenha_objeto()
        if isinstance(parte, Cano):
            if parte.x == 120:
                pontos_jogador.marca_ponto(1)

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
        item = random.choice(lista_itens)
        if item.criado == False:
            if random.randint(1, 1) == 1:
               item.posicao_tela()
               listaObjetos.append(item)        
        cano3.tamanho_cano()
        listaObjetos.append(cano3)
    if cano2.x < -40:
        cano2.destruir()
        listaObjetos.remove(cano2)

    if cano3.x == 320:
        if item.criado == False:
            if random.randint(1, 1) == 1:
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
        item = random.choice(lista_itens)

    passaro.desenha_personagem(cenario.tela)
    passaro.mover()

    passaro.colisao(canos=cano1.gera_retangulo())
    passaro.colisao(canos=cano2.gera_retangulo())
    passaro.colisao(canos=cano3.gera_retangulo())

    # para conferir se o personagem coleta o item
    for objeto in listaObjetos:
        if isinstance(objeto, Itens) and not ignorar_item: 
            # adicionei a variável "ignorar_item" para que o item tenha efeito sobre o personagem apenas uma vez (quando é coletado)
            # e não por todo o período em que o personagem tem contato com ele
            # provavelmente isso será desnecessário quando conseguirmos fazer o item desaparecer assim que for coletado 
            passaro.pegou_item(item=objeto, personagem=passaro)
            if objeto.coletado:
                contador.setar_tempo(5)
                objeto.coletado = False
                ignorar_item = True
    
    # controla o tempo de duração do efeito do item
    # ainda precisa ser melhorado, para que o personagem possa receber dois efeitos diferentes ao mesmo tempo 
    if ignorar_item == True:  # verifica se o item já está ativo
        if contador.fim_contagem() == True:  # verifica o tempo de duração do item
            for efeitos in lista_itens:
                efeitos.reverter(passaro)# reverte o estado do personagem ao que estava antes de coletar o item 
            item.timer = None
            ignorar_item = False


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not passaro.voando and not passaro.game_over:
            if evento.key == pygame.K_UP:
                passaro.voando = True

    pygame.display.update()

pygame.quit()