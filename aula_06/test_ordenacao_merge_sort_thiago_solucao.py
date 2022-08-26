import unittest


def ordenar(seq):
    if len(seq) > 1:
        m = len(seq) // 2
        left_list = ordenar(seq[:m])
        right_list = ordenar(seq[m:])

        right_index = left_index = 0
        seq = []

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] <= right_list[right_index]:
                seq.append(left_list[left_index])
                left_index += 1
            else:
                seq.append(right_list[right_index])
                right_index += 1
        seq.extend(right_list[right_index:])
        seq.extend(left_list[left_index:])
    return seq


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
    ordenar(list(range(1000)))
