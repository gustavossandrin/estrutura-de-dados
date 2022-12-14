import unittest
from numbers import Number
from typing import Dict, List


class Arco():
    def __init__(self, origem: str, destino: str, valor: Number):
        self.valor_original = self.valor = valor
        self.vertices = (origem, destino)

    def __hash__(self):
        return hash(self.vertices + (self.valor,))

    def __eq__(self, arco):
        return (self.valor,) + self.vertices == (arco.valor,) + arco.vertices

    def __lt__(self, other):
        return self.valor < other.valor

    def __repr__(self):
        return 'Arco({!r}, {!r}, {!r})'.format(self.vertices[0], self.vertices[1], self.valor)

    def oposto(self, vertice: str):
        if vertice == self.vertices[0]:
            return self.vertices[1]
        elif vertice == self.vertices[1]:
            return self.vertices[0]


class ArcoTestes(unittest.TestCase):
    def teste_init(self):
        arco = Arco('origem', 'destino', 1)
        self.assertTupleEqual(('origem', 'destino'), arco.vertices)
        self.assertEqual(1, arco.valor)

    def teste_oposto(self):
        arco = Arco('origem', 'destino', 1)
        self.assertEqual('origem', arco.oposto('destino'))
        self.assertEqual('destino', arco.oposto('origem'))


# Dados a serem usados nos testes

# Dados de vérticos
bertioga = 'Bertioga'
caragua = 'Caragua'
jacarei = 'Jacareí'
mogi = 'Mogi da Cruzes'
santos = 'Santos'
sjc = 'São José dos Campos'
sao_paulo = 'São Paulo'
taubate = 'Taubaté'

vertices_cidades = (
    bertioga,
    caragua,
    jacarei,
    mogi,
    santos,
    sjc,
    sao_paulo,
    taubate
)
# Dados de arcos
arco_tauba_sjc = Arco(taubate, sjc, 43900)
arco_sjc_jaca = Arco(sjc, jacarei, 13200)
arco_scj_caragua = Arco(sjc, caragua, 86900)
arco_caragua_bertioga = Arco(caragua, bertioga, 114000)
arco_bertioga_mogi = Arco(bertioga, mogi, 48700)
arco_mogi_jaca = Arco(mogi, jacarei, 54300)
arco_mogi_sp = Arco(mogi, sao_paulo, 61900)
arco_jaca_sp = Arco(jacarei, sao_paulo, 81800)
arco_santos_sp = Arco(santos, sao_paulo, 72800)
arco_santos_bertioga = Arco(santos, bertioga, 74400)

arcos_distancias = (
    arco_tauba_sjc,
    arco_sjc_jaca,
    arco_scj_caragua,
    arco_caragua_bertioga,
    arco_bertioga_mogi,
    arco_mogi_jaca,
    arco_mogi_sp,
    arco_jaca_sp,
    arco_santos_sp,
    arco_santos_bertioga
)


class Grafo:

    def __init__(self):
        self._vertices: Dict[str, Dict[str, List[Arco]]] = dict()

    def vertices(self):
        return tuple(self._vertices)

    def adicionar_vertice(self, vertice: str):
        self._vertices[vertice] = self._vertices.get(vertice, dict())

    def arcos(self, vertice: str):
        lista_de_arcos = []
        for lista_de_arcos_vertice_oposto in self._vertices[vertice].values():
            lista_de_arcos.extend(lista_de_arcos_vertice_oposto)

        return tuple(lista_de_arcos)

    def adjacencias(self, vertice: str):
        return tuple(self._vertices[vertice].keys())

    def adicionar_arco(self, arco: Arco):
        for vertice in arco.vertices:
            self.adicionar_vertice(vertice)
            dict_adjacencias: Dict[str, List[Arco]] = self._vertices[vertice]
            vertice_oposto: str = arco.oposto(vertice)
            lista_de_arcos: List[Arco] = dict_adjacencias.get(vertice_oposto, list())
            lista_de_arcos.append(arco)
            dict_adjacencias[vertice_oposto] = lista_de_arcos

    def caminho(self, vertice_origem: str, vertice_destino: str) -> List[str]:
        if vertice_destino == vertice_origem:
            return [vertice_origem]
        vertices_visitados = {vertice_origem}
        arcos = []
        arcos.extend(self.arcos(vertice_origem))
        caminho = [vertice_origem]
        while arcos:
            arco = arcos.pop()
            vertice_oposto = arco.oposto(vertice_origem)
            if vertice_oposto == vertice_destino:
                caminho.append(vertice_destino)
                return caminho

            if vertice_oposto not in vertices_visitados:
                vertice_origem = vertice_oposto
                vertices_visitados.add(vertice_origem)
                caminho.append(vertice_origem)
                arcos.extend(self.arcos(vertice_origem))
        return []

    def calcular_melhores_caminhos_partindo_de(self, cidade) -> dict:
        cidades_visitadas = {cidade}
        caminho = [cidade]
        lista_de_arcos = list(self.arcos(cidade))
        dct_caminhos_minimos = {cidade: (0, caminho)}
        while len(lista_de_arcos) > 0:
            arco_distancia_minima = min(lista_de_arcos)
            if set(arco_distancia_minima.vertices).issubset(cidades_visitadas):
                lista_de_arcos.remove(arco_distancia_minima)
                continue

            uma_cidade_do_arco_distancia_minima = arco_distancia_minima.vertices[0]
            if uma_cidade_do_arco_distancia_minima in cidades_visitadas:
                origem = arco_distancia_minima.oposto(uma_cidade_do_arco_distancia_minima)
                caminho = list(dct_caminhos_minimos[uma_cidade_do_arco_distancia_minima][1])
            else:
                origem = uma_cidade_do_arco_distancia_minima
                caminho = list(
                    dct_caminhos_minimos[arco_distancia_minima.oposto(uma_cidade_do_arco_distancia_minima)][1])
            lista_de_arcos.remove(arco_distancia_minima)
            distancia_minima = arco_distancia_minima.valor
            caminho.append(arco_distancia_minima.valor_original)
            caminho.append(origem)
            dct_caminhos_minimos[origem] = (distancia_minima, caminho)

            arcos_da_origem = self.arcos(origem)
            for arco in arcos_da_origem:
                if arco.oposto(origem) not in cidades_visitadas:
                    arco.valor += distancia_minima
                    lista_de_arcos.append(arco)
            cidades_visitadas.add(origem)

        return dct_caminhos_minimos


class GrafoTestes(unittest.TestCase):
    def teste_adicionar_vertice(self):
        grafo = Grafo()
        self.assert_mesmo_elementos(tuple(), grafo.vertices())
        grafo.adicionar_vertice(santos)
        self.assert_mesmo_elementos((santos,), grafo.vertices())
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos((santos, jacarei), grafo.vertices())
        grafo.adicionar_vertice(mogi)
        self.assert_mesmo_elementos((santos, jacarei, mogi), grafo.vertices())
        grafo.adicionar_vertice(caragua)
        self.assert_mesmo_elementos((santos, jacarei, mogi, caragua), grafo.vertices())

    def teste_adicionar_arco(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(jacarei))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(jacarei))
        grafo.adicionar_arco(arco_sjc_jaca)
        self.assert_mesmo_elementos((arco_sjc_jaca,), grafo.arcos(jacarei))
        self.assert_mesmo_elementos((arco_sjc_jaca,), grafo.arcos(sjc))
        self.assert_mesmo_elementos((jacarei,), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_tauba_sjc)
        self.assert_mesmo_elementos((arco_sjc_jaca, arco_tauba_sjc), grafo.arcos(sjc))
        self.assert_mesmo_elementos((arco_tauba_sjc,), grafo.arcos(taubate))

        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(taubate))
        self.assert_mesmo_elementos((taubate, jacarei), grafo.adjacencias(sjc))

    def teste_caminho_para_proprio_vertice(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assertListEqual([sjc], grafo.caminho(sjc, sjc))

    def teste_caminho_vertices_desconexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        self.assertListEqual([], grafo.caminho(sjc, jacarei))

    def teste_caminho_dois_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_arco(arco_sjc_jaca)
        self.assertListEqual([sjc, jacarei], grafo.caminho(sjc, jacarei))

    def teste_caminho_tres_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_sjc_jaca)
        grafo.adicionar_arco(arco_tauba_sjc)

        self.assertListEqual([taubate, sjc, jacarei], grafo.caminho(taubate, jacarei))
        self.assertListEqual([taubate, sjc], grafo.caminho(taubate, sjc))

    def teste_caminho_4_vertices_conexos_nao_lineares(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(mogi)
        grafo.adicionar_vertice(sao_paulo)
        grafo.adicionar_arco(arco_sjc_jaca)
        grafo.adicionar_arco(arco_jaca_sp)
        grafo.adicionar_arco(arco_mogi_jaca)
        grafo.adicionar_arco(arco_mogi_sp)

        caminho = grafo.caminho(sjc, sao_paulo)
        self.assertTrue([sjc, jacarei, sao_paulo] == caminho or [sjc, jacarei, mogi, sao_paulo] == caminho)

    def teste_melhor_caminho_partindo_de_taubate_considerando_distancias(self):
        grafo = Grafo()
        for v in vertices_cidades:
            grafo.adicionar_vertice(v)

        for a in arcos_distancias:
            grafo.adicionar_arco(a)

        dct = grafo.calcular_melhores_caminhos_partindo_de(taubate)
        self.assert_mesmo_elementos(vertices_cidades, dct.keys())

        distancia, caminho = dct[taubate]
        self.assertEqual(0, distancia)
        self.assertListEqual([taubate], caminho)

        distancia, caminho = dct[sjc]
        self.assertEqual(43900, distancia)
        self.assertListEqual([taubate, 43900, sjc], caminho)

        distancia, caminho = dct[jacarei]
        self.assertEqual(57100, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei], caminho)

        distancia, caminho = dct[mogi]
        self.assertEqual(111400, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 54300, mogi], caminho)

        distancia, caminho = dct[caragua]
        self.assertEqual(130800, distancia)
        self.assertListEqual([taubate, 43900, sjc, 86900, caragua], caminho)

        distancia, caminho = dct[sao_paulo]
        self.assertEqual(138900, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 81800, sao_paulo], caminho)

        distancia, caminho = dct[bertioga]
        self.assertEqual(160100, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 54300, mogi, 48700, bertioga], caminho)

        distancia, caminho = dct[santos]
        self.assertEqual(211700, distancia)
        self.assertListEqual([taubate, 43900, sjc, 13200, jacarei, 81800, sao_paulo, 72800, santos], caminho)

    def teste_melhor_caminho_partindo_de_taubate_considerando_custo(self):
        grafo = Grafo()
        for v in vertices_cidades:
            grafo.adicionar_vertice(v)

        preco_gasolina = 3.65  # R$/litro
        rendimento_carro_popular = 15000  # metros/litro
        preco_por_distancia = preco_gasolina / rendimento_carro_popular  # R$/metro
        arcos_custo = [Arco(a.vertices[0], a.vertices[1], a.valor * preco_por_distancia)
                       for a in arcos_distancias]

        pedagios = {(jacarei, sao_paulo): 11.8, (jacarei, mogi): 6.1, (sao_paulo, santos): 23, (sao_paulo, mogi): 3.2,
                    (bertioga, santos): 10.8}

        for a in arcos_custo:
            vertices_contrarios = (a.vertices[1], a.vertices[0])
            pedagio = pedagios.get(a.vertices, pedagios.get(vertices_contrarios, 0))
            a.valor_original = a.valor = round(pedagio + a.valor)

            grafo.adicionar_arco(a)

        dct = grafo.calcular_melhores_caminhos_partindo_de(taubate)
        self.assert_mesmo_elementos(vertices_cidades, dct.keys())

        distancia, caminho = dct[taubate]
        self.assertEqual(0, distancia)
        self.assertListEqual([taubate], caminho)

        distancia, caminho = dct[sjc]
        self.assertEqual(11, distancia)
        self.assertListEqual([taubate, 11, sjc], caminho)

        distancia, caminho = dct[jacarei]
        self.assertEqual(14, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei], caminho)

        distancia, caminho = dct[mogi]
        self.assertEqual(33, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi], caminho)

        distancia, caminho = dct[caragua]
        self.assertEqual(32, distancia)
        self.assertListEqual([taubate, 11, sjc, 21, caragua], caminho)

        distancia, caminho = dct[sao_paulo]
        self.assertEqual(46, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 32, sao_paulo], caminho)

        distancia, caminho = dct[bertioga]
        self.assertEqual(45, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi, 12, bertioga], caminho)

        distancia, caminho = dct[santos]
        self.assertEqual(74, distancia)
        self.assertListEqual([taubate, 11, sjc, 3, jacarei, 19, mogi, 12, bertioga, 29, santos], caminho)

    def assert_mesmo_elementos(self, iteravel, outro_iteravel):
        "Método auxiliar para asserção de elementos"
        self.assertSetEqual(set(iteravel), set(outro_iteravel))