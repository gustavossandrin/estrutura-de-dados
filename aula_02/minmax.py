from math import inf


def min_max_usando_for(lista):
    """
    calculando tempo:
    O(n)
    calculando memoria:
    O(1)
    :param lista:
    :return:
    """
    valor_maximo = -inf
    valor_minimo = inf
    for i in lista:
        if i > valor_maximo:
            valor_maximo = i
        if i < valor_minimo:
            valor_minimo = i
    return valor_minimo, valor_maximo


contagem = 0
valor_minimo = inf
valor_maximo = -inf


def min_max_recursivo(lista):
    global valor_maximo, valor_minimo, contagem
    if contagem == len(lista) - 1:
        print(valor_minimo, valor_maximo)
        return
    elif contagem <= len(lista):
        if lista[contagem] > valor_maximo:
            valor_maximo = lista[contagem]
        if lista[contagem] < valor_minimo:
            valor_minimo = lista[contagem]
    contagem += 1
    min_max_recursivo(lista)


if __name__ == '__main__':
    print(min_max_usando_for([1, 2, 3, 4, 5, 1, 2, 3, 4, 21312, 3213, -21312, 32132, 32141]))

    for i in range(15):
        lista = list(range(i))
        min_max_recursivo(lista)
