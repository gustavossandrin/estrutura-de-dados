import unittest


def ordenar(seq):
    for indice_atual, _ in enumerate(seq):
        indice_do_valor_minimo = min(
            (valor, indice) for indice, valor in
            enumerate(gerar_slice_sem_gastar_memoria(indice_atual, seq), start=indice_atual)
        )[1]
        seq[indice_atual], seq[indice_do_valor_minimo] = seq[indice_do_valor_minimo], seq[indice_atual]
    return seq


def gerar_slice_sem_gastar_memoria(indice_atual, seq):
    for indice in range(indice_atual, len(seq)):
        yield seq[indice]



if __name__ == '__main__':
    print(ordenar(list(range(100000))))
