class MelhorPontuacao:
    def __init__(self):
        self.score = [[0, 'UNK'], [0, 'UNK'], [0, 'UNK'], [0, 'UNK'], [0, 'UNK']]

    def checapontuacao(self, novapontuacao: int):
        self.score.sort()
        self.score = self.score[::-1]
        if self.score[4][0] < novapontuacao:
            return True
        return False

    def novapontuacao(self, novapontuacao, nome):
        self.score.pop(4)
        self.score.append([novapontuacao, nome])
        self.score.sort()
        self.score = self.score[::-1]

