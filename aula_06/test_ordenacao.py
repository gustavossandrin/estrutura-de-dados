import unittest
from math import inf


def ordenar(seq):
    lista_ordenada = []
    for indice, valor in enumerate(list(seq)):
        valor_minimo = inf
        for i in seq[indice:]:
            if i < valor_minimo:
                valor_minimo = i
        seq.remove(valor_minimo)
        seq.insert(0, 0)
        lista_ordenada.append(valor_minimo)
    return lista_ordenada


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada_melhorada(self):
        self.assertListEqual([0, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
