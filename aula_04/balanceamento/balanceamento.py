from aula_04.pilha_com_lista.pilha_com_lista import Pilha


def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    pilha = Pilha()
    pares = {')': '(', ']': '[', '}': '{'}
    for i in expressao:
        if i in '([{':
            pilha.empilhar(i)
        elif i in ')]}':
            try:
                pilha.topo()
            except:
                return False
            else:
                if pilha.topo() != pares[i]:
                    return False
                else:
                    pilha.desempilhar()
    if pilha.esta_vazia == True:
        return True
    else:
        return False

if __name__ == '__main__':
    print(esta_balanceada('{{}}()()([])'))
