from abc import ABC, abstractmethod
from itemInvencibilidade import ItemInvencibilidade
from itemTamanho import ItemTamanho


# Factory MazeGame que criar jogos do tipo labirinto com salas (produtos) distintas
class GeradorItem(ABC):
    def __init__(self, cenario) -> None:
        self.cenario = cenario

    # Factory method make_room será especializado para cada tipo de sala
    @abstractmethod
    def criador_item(self):
        raise NotImplementedError("Você deve implementar isso!")

# classe derivada 1 - escializa make_room criando uma sala mágica
class GeradorItemTamanho(GeradorItem):
    
    def criador_item(self):
        return ItemTamanho(self.cenario.tela)

# classe derivada 2
class GeradorItemInvencibilidade(GeradorItem):

    def criador_item(self):
        return ItemInvencibilidade(self.cenario.tela)
