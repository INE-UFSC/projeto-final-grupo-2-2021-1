from animacao import Animacao
import pygame

class SpriteBotaoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/jogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.__dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

class SpriteBotaoComoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/comojogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.__dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

class SpriteBotaoVoltar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/voltar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.__dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

class SpriteBotaoPontuacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/pontuacao/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.__dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes
    
class SpriteCaixaTexto(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/caixatexto/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True    
        self.__dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes
    
class SpriteBotaoSalvar(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/salvar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True   
        self.__dimensoes = (192, 48) 

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

class SpriteQuadroPontuacao(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/quadropontuacao/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True  
        self.__dimensoes = (192, 288)  

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes