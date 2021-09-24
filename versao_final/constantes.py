from singleton import Singleton

class Constante(Singleton):
    def __init__(self) -> None:
        self.tela_jogo_largura = 780
        self.tela_jogo_altura = 640
        self.botao_maior_x = 300
        self.botao_maior_y = 75
        self.posicao_gera_cano = 320
        self.largura_cano = 40
        self.largura_item = 20
        self.distancia_item_cano = 70
        self.posicao_destruir = -40
        self.posicao_pontuar = 120
        self.posicao_personagem_x = 160
        self.posicao_personagem_y = 300
        self.tamanho_personagem = 35
        self.dimensoes_personagem = (65, 57)
        self.dimensoes_personagem_item_tamanho = (47, 42)
        self.fps = 60
        self.tempo_invencibilidade = 5
        self.tempo_pequeno = 7