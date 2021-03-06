import pygame

class Contador:
    def __init__(self) -> None:
        self.__terminou = False
        self.__auxiliar = 1
        self.__tempo_contado = 0
        self.__tempo_fim = -1

    @property
    def tempo_contado(self):
        return self.__tempo_contado

    def contador_tempo(self):
        tempo = pygame.time.get_ticks()/1000
        if tempo >= self.__auxiliar:
            self.__tempo_contado = self.__auxiliar
            self.__auxiliar += 1