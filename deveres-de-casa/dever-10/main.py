"""Algoritmo de Kruskal modificado para Árvore Geradora Máxima.

Este módulo implementa o algoritmo de Kruskal com a modificação
necessária para encontrar a Árvore Geradora Máxima (MaxST) de um
grafo ponderado conexo, em vez da Árvore Geradora Mínima (MST).

A única alteração estrutural em relação ao Kruskal padrão está na
ordenação inicial das arestas: do maior para o menor peso. As
otimizações do Union-Find (Path Compression e Union by Rank)
permanecem inalteradas.
"""

import time


class Grafo:
    """Grafo não direcionado ponderado com algoritmo de Kruskal.

    Atributos:
        num_vertices: Número total de vértices do grafo.
        arestas: Lista de arestas no formato [origem, destino, peso].
    """

    def __init__(self, num_vertices):
        """Inicializa o grafo com a quantidade de vértices informada.

        Parâmetros:
            num_vertices: Quantidade de vértices do grafo.
        """
        self.num_vertices = num_vertices
        self.arestas = []

    def adicionar_aresta(self, origem, destino, peso):
        """Adiciona uma aresta não direcionada ao grafo.

        Parâmetros:
            origem: Vértice de partida da aresta.
            destino: Vértice de chegada da aresta.
            peso: Custo associado à aresta.
        """
        self.arestas.append([origem, destino, peso])

    def buscar_raiz(self, pai, indice):
        """Encontra a raiz da rede com Compressão de Caminho.

        Aplica a otimização Path Compression: durante a busca,
        todos os nós no caminho passam a apontar diretamente
        para a raiz, achatando a árvore progressivamente.

        Parâmetros:
            pai: Lista que mapeia cada nó ao seu pai.
            indice: Índice do nó cuja raiz se quer encontrar.

        Retorna:
            O índice da raiz da rede que contém o nó.

        Complexidade:
            Praticamente O(1) amortizado pela função inversa de
            Ackermann α(V), efetivamente constante.
        """
        if pai[indice] == indice:
            return indice
        pai[indice] = self.buscar_raiz(pai, pai[indice])
        return pai[indice]

    def unir_redes(self, pai, rank, vertice_a, vertice_b):
        """Une duas redes usando União por Rank.

        Aplica a otimização Union by Rank: a árvore com menor
        rank é anexada à de maior rank, evitando árvores
        profundas e mantendo o custo de busca logarítmico no
        pior caso.

        Parâmetros:
            pai: Lista que mapeia cada nó ao seu pai.
            rank: Lista com o rank (altura) de cada raiz.
            vertice_a: Primeiro vértice a ser unido.
            vertice_b: Segundo vértice a ser unido.

        Complexidade:
            O(α(V)) amortizado em conjunto com Path Compression,
            praticamente constante.
        """
        raiz_a = self.buscar_raiz(pai, vertice_a)
        raiz_b = self.buscar_raiz(pai, vertice_b)

        if rank[raiz_a] < rank[raiz_b]:
            pai[raiz_a] = raiz_b
        elif rank[raiz_a] > rank[raiz_b]:
            pai[raiz_b] = raiz_a
        else:
            pai[raiz_b] = raiz_a
            rank[raiz_a] += 1

    def executar_kruskal_maxima(self):
        """Executa o Kruskal para encontrar a Árvore Geradora Máxima.

        Modificação em relação ao Kruskal padrão: as arestas são
        ordenadas do MAIOR para o MENOR peso (reverse=True). Toda
        a lógica de validação por Union-Find permanece inalterada.

        Retorna:
            Uma tupla (arestas_selecionadas, custo_total) com as
            arestas da Árvore Geradora Máxima e a soma dos pesos.

        Complexidade:
            O(E log E) dominada pela ordenação das arestas.
            O Union-Find com otimizações contribui com O(E α(V)),
            praticamente linear.
        """
        resultado = []
        indice_aresta = 0
        arestas_adicionadas = 0
        custo_total = 0

        # Única mudança em relação ao Kruskal padrão:
        # ordenação decrescente das arestas (reverse=True).
        self.arestas = sorted(
            self.arestas, key=lambda item: item[2], reverse=True
        )

        # Cada vértice começa como sua própria rede independente.
        pai = list(range(self.num_vertices))
        rank = [0] * self.num_vertices

        # Itera até formar uma árvore geradora (V - 1 arestas).
        while arestas_adicionadas < self.num_vertices - 1:
            origem, destino, peso = self.arestas[indice_aresta]
            indice_aresta += 1

            raiz_origem = self.buscar_raiz(pai, origem)
            raiz_destino = self.buscar_raiz(pai, destino)

            # Raízes distintas -> a aresta não forma ciclo.
            if raiz_origem != raiz_destino:
                arestas_adicionadas += 1
                resultado.append([origem, destino, peso])
                custo_total += peso
                self.unir_redes(pai, rank, raiz_origem, raiz_destino)

        return resultado, custo_total


def main():
    """Executa o caso de teste do mapa da dinâmica."""
    grafo = Grafo(8)

    grafo.adicionar_aresta(4, 7, 1)
    grafo.adicionar_aresta(5, 6, 2)
    grafo.adicionar_aresta(4, 5, 3)
    grafo.adicionar_aresta(6, 7, 4)
    grafo.adicionar_aresta(0, 1, 5)
    grafo.adicionar_aresta(3, 7, 6)
    grafo.adicionar_aresta(2, 5, 7)
    grafo.adicionar_aresta(2, 6, 8)
    grafo.adicionar_aresta(1, 2, 9)
    grafo.adicionar_aresta(1, 6, 10)
    grafo.adicionar_aresta(1, 5, 11)
    grafo.adicionar_aresta(1, 7, 13)
    grafo.adicionar_aresta(1, 4, 14)
    grafo.adicionar_aresta(0, 4, 15)
    grafo.adicionar_aresta(0, 3, 16)
    grafo.adicionar_aresta(3, 6, 17)
    grafo.adicionar_aresta(0, 7, 18)

    inicio = time.perf_counter()
    caminho_final, custo_final = grafo.executar_kruskal_maxima()
    fim = time.perf_counter()
    tempo_execucao_ms = (fim - inicio) * 1000

    print("--- RESULTADO: ÁRVORE GERADORA MÁXIMA ---")
    print("Rotas escolhidas (maior peso primeiro):")
    for origem, destino, peso in caminho_final:
        print(
            f"  Rota da cidade {origem} para a cidade {destino} "
            f"| Custo: {peso}"
        )
    print(f"\nCusto Total da Obra (MÁXIMO sem ciclos): {custo_final}")
    print(f"Tempo de execução: {tempo_execucao_ms:.4f} milissegundos")


if __name__ == "__main__":
    main()