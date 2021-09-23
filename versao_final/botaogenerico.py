from abc import ABC, abstractmethod
from spritebotoes import SpriteBotaoJogar, SpriteBotaoComoJogar, SpriteBotaoPontuacao, SpriteBotaoVoltar
import pygame

class BotaoGenerico(ABC):
    def __init__(self, sprite) -> None:
        self.__sprite = pygame.sprite.Group(sprite)
    
    def atualizar(self, x, y):
        self.__sprite.update(x, y)
    
    def desenhar(self, tela):
        self.__sprite.draw(tela)
    
    def gera_retangulo(self):
        rect_superior = self.__sprite.sprites()[0].rect

        return rect_superior
    
    @abstractmethod
    def efeito_colisao(self):
        pass

class BotaoJogar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoJogar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "Jogo"

class BotaoComoJogar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoComoJogar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "ComoJogar"

class BotaoPontuacao(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoPontuacao())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "Pontuacao"

class BotaoVoltar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoVoltar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "MenuPrincipal"