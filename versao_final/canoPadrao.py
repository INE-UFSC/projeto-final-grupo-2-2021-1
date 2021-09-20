from cano import Cano


class CanoPadrao(Cano):
    def __init__(self):
        super().__init__()

    def efeito_colisao(self, personagem):
        if not personagem.invencivel:
            personagem.game_over = True
            self.colidiu = True

    def move(self):
        self.x += -5
