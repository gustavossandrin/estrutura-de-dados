def pegar_simbolos(lista):
    simbolos = []
    for i in lista:
        if i == '(':
            simbolos.append(i)
        elif i == ')':
            simbolos.append(i)
        if i == ']':
            simbolos.append(i)
        if i == '[':
            simbolos.append(i)
        if i == '{':
            simbolos.append(i)
        if i == '}':
            simbolos.append(i)
    return simbolos


def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    if expressao == '':
        return True
    expressao_com_simbolos = pegar_simbolos(expressao)
    pilha = []
    if expressao_com_simbolos[0] == '}':
        return False
    if expressao_com_simbolos[0] == ')':
        return False
    if expressao_com_simbolos[0] == ']':
        return False

    for i in expressao_com_simbolos:
        if i:
            if i == ')' and pilha[-1] == '(':
                pilha.pop()
            elif i == ']' and pilha[-1] == '[':
                pilha.pop()
            elif i == '}' and pilha[-1] == '{':
                pilha.pop()
            elif i == ')' and pilha[-1] != '(':
                return False
            elif i == ']' and pilha[-1] != '[':
                return False
            elif i == '}' and pilha[-1] != '{':
                return False
            else:
                pilha.append(i)

    if len(pilha) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(esta_balanceada('[[[]]{{}}()'))
    print(pegar_simbolos('4 5 123 321 [ [ } ] 21 ('.split()))
