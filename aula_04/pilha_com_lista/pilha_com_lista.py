class Pilha:
    def __init__(self):
        self.esta_vazia = True
        self.pilha = []

    def topo(self):
        try:
            return self.pilha[-1]
        except:
            raise PilhaVaziaExcecao('Pilha vazia')

    def empilhar(self, obj):
        self.esta_vazia = False
        self.pilha.append(obj)

    def desempilhar(self):
        if len(self.pilha) == 1:
            self.esta_vazia = True
        try:
            return self.pilha.pop()
        except:
            raise PilhaVaziaExcecao('Pilha vazia')





class PilhaVaziaExcecao(Exception):
    pass