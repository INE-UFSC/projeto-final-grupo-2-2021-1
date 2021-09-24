from animacao import Animacao
import pygame

class SpriteBotaoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/jogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

class SpriteBotaoComoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/comojogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

class SpriteBotaoVoltar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/voltar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

class SpriteBotaoPontuacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/pontuacao/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True
        self.dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
class SpriteCaixaTexto(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/caixatexto/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True    
        self.dimensoes = (192, 48)

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
class SpriteBotaoSalvar(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/salvar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True   
        self.dimensoes = (192, 48) 

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

class SpriteQuadroPontuacao(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/quadropontuacao/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True  
        self.dimensoes = (192, 288)  

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
class SpriteTeclaUp(Animacao):

    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/cima/'])
        self.__rect = self.image.get_rect(center=(0, 0))
        self.inicio_posicao = True  
        self.dimensoes = (52, 56)  

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
