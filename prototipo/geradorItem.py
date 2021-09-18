from abc import ABC, abstractmethod
from itemInvencibilidade import ItemInvencibilidade
from itemTamanho import ItemTamanho


# Factory GeradorItem
class GeradorItem(ABC):
    def __init__(self) -> None:
        pass

    # Factory method criador_item será especializado para cada tipo de item
    @abstractmethod
    def criador_item(self):
        raise NotImplementedError("Você deve implementar isso!")

# classe derivada 1 - especializa criador_item criando um item de tamanho
class GeradorItemTamanho(GeradorItem):
    def criador_item(self):
        return ItemTamanho()

# classe derivada 2 - especializa criador_item criando um item de invencibilidade
class GeradorItemInvencibilidade(GeradorItem):
    def criador_item(self):
        return ItemInvencibilidade()
