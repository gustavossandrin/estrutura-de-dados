import unittest
from random import randint


def quick_sort(seq):
    def _quick_sort(i, j):
        if j - i < 1:
            return
        fim = j
        p = randint(i, j)
        seq[p], seq[j] = seq[j], seq[p]

        while i < j:
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
                while j > i:
                    if seq[j] < seq[i]:
                        seq[i], seq[j] = seq[j], seq[i]
                        break
                    j -= 1
            i += 1
        _quick_sort(0, j - 1)
        _quick_sort(j + 1, fim)

    _quick_sort(0, len(seq) - 1)

    return seq




class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
