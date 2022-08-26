import unittest


def ordenar_bubble(lista):
    # [9, 7, 1, 8, 5, 3, 6, 4, 2, 0]
    for i in range(len(lista)):
        sentinela = True

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
                sentinela = False
        if sentinela: return lista

    return lista





class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar_bubble([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar_bubble([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar_bubble([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar_bubble([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada_melhorada(self):
        self.assertListEqual([0, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9],
                             ordenar_bubble([9, 7, 1, 8, 5, 3, 6, 4, 2, 0, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
    ordenar(list(range(1000)))
