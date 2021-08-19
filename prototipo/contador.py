import pygame

class Contador:
    def __init__(self) -> None:
        self.__terminou = False
        self.__auxiliar = 1
        self.__tempo_contado = 0
        self.__tempo_fim = -1

    def contador_tempo(self):
        tempo = pygame.time.get_ticks()/1000
        if tempo >= self.__auxiliar:
            self.__tempo_contado = self.__auxiliar
            self.__auxiliar += 1
  
    def setar_tempo(self, tempo_para_contar):
        self.__terminou = False
        self.__tempo_fim = self.__tempo_contado + tempo_para_contar

    def fim_contagem(self):
        if self.__tempo_fim == self.__tempo_contado:
            self.__terminou = True 
        return self.__terminou