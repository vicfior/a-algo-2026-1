"""
Dever de Casa — Missão de Engenharia de Grafos (§30).

Algoritmo de Dijkstra: Menor Caminho em Grafo Ponderado Aleatório.

Disciplina: Análise de Algoritmos — Centro Universitário IESB
Descrição:
    1. Gera um grafo ponderado aleatório com 50 nós e 150 arestas.
    2. Implementa Dijkstra com fila de prioridade (min-heap).
    3. Encontra e imprime o menor caminho do Nó 1 ao Nó 50.
"""

import random
import heapq
import time

# Constantes do problema (parametrizadas conforme o enunciado)
NUM_NOS = 50
NUM_ARESTAS = 150
NO_ORIGEM = 1
NO_DESTINO = 50
PESO_MIN = 1
PESO_MAX = 20
SEMENTE = 42


def gerar_grafo(num_nos, num_arestas, peso_min, peso_max, semente=None):
    """Gera um grafo não-direcionado, ponderado e conexo.

    Estratégia em duas fases:
        - Fase 1: constrói uma árvore geradora aleatória (n-1
          arestas) para garantir que o grafo é conexo.
        - Fase 2: adiciona arestas extras aleatórias até atingir
          o total desejado, evitando duplicatas e self-loops.

    Parâmetros:
        num_nos     (int): Quantidade de vértices (1 a num_nos).
        num_arestas (int): Quantidade total de arestas desejadas.
        peso_min    (int): Peso mínimo de uma aresta.
        peso_max    (int): Peso máximo de uma aresta.
        semente     (int): Semente do gerador aleatório.

    Retorna:
        dict: Lista de adjacências {nó: [(vizinho, peso), ...]}.
    """
    if semente is not None:
        random.seed(semente)

    adjacencias = {i: [] for i in range(1, num_nos + 1)}
    arestas_existentes = set()

    def _adicionar_aresta(u, v, peso):
        """Registra aresta bidirecional no grafo."""
        adjacencias[u].append((v, peso))
        adjacencias[v].append((u, peso))
        arestas_existentes.add((min(u, v), max(u, v)))

    # Fase 1 — árvore geradora aleatória (garante conectividade)
    nos = list(range(1, num_nos + 1))
    random.shuffle(nos)
    for i in range(len(nos) - 1):
        peso = random.randint(peso_min, peso_max)
        _adicionar_aresta(nos[i], nos[i + 1], peso)

    # Fase 2 — arestas extras até atingir num_arestas
    while len(arestas_existentes) < num_arestas:
        u = random.randint(1, num_nos)
        v = random.randint(1, num_nos)
        if u == v:
            continue
        chave = (min(u, v), max(u, v))
        if chave in arestas_existentes:
            continue
        peso = random.randint(peso_min, peso_max)
        _adicionar_aresta(u, v, peso)

    return adjacencias


def dijkstra(adjacencias, origem, destino):
    """Encontra o menor caminho entre origem e destino.

    Utiliza uma fila de prioridade (min-heap) via heapq,
    conforme discutido na aula 01 sobre Heaps e Filas de
    Prioridade: o heap permite extrair o nó de menor
    distância em O(log n).

    Parâmetros:
        adjacencias (dict): Grafo como lista de adjacências.
        origem       (int): Nó de partida.
        destino      (int): Nó de chegada.

    Retorna:
        tuple: (distancia_minima, lista_do_caminho)
               ou (inf, []) se não houver caminho.

    Complexidade:
        Tempo:  O((V + E) * log V) com heap binário.
        Espaço: O(V) para distâncias e predecessores.
    """
    distancias = {no: float("inf") for no in adjacencias}
    distancias[origem] = 0

    predecessores = {no: None for no in adjacencias}

    visitados = set()

    # Fila de prioridade: (distância acumulada, nó)
    fila = [(0, origem)]

    while fila:
        # Extrai o nó com menor distância — O(log V)
        dist_atual, no_atual = heapq.heappop(fila)

        # Entrada obsoleta no heap — pula
        if no_atual in visitados:
            continue

        # Distância finalizada para este nó
        visitados.add(no_atual)

        # Parada antecipada ao atingir o destino
        if no_atual == destino:
            break

        # Relaxamento das arestas vizinhas
        for vizinho, peso in adjacencias[no_atual]:
            if vizinho in visitados:
                continue
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return _reconstruir_caminho(
        predecessores, distancias, origem, destino
    )


def _reconstruir_caminho(predecessores, distancias, origem, destino):
    """Reconstrói a sequência de nós do caminho mínimo.

    Parte do destino e segue os predecessores até a origem,
    invertendo a lista ao final.

    Parâmetros:
        predecessores (dict): Mapa {nó: predecessor}.
        distancias    (dict): Mapa {nó: distância mínima}.
        origem         (int): Nó de partida.
        destino        (int): Nó de chegada.

    Retorna:
        tuple: (distancia_minima, lista_do_caminho)
               ou (inf, []) se o caminho não existir.
    """
    caminho = []
    no = destino
    while no is not None:
        caminho.append(no)
        no = predecessores[no]
    caminho.reverse()

    if not caminho or caminho[0] != origem:
        return float("inf"), []

    return distancias[destino], caminho


def main():
    """Ponto de entrada: gera grafo, executa Dijkstra, imprime."""
    print("=" * 60)
    print(" MISSÃO DE ENGENHARIA DE GRAFOS — DIJKSTRA")
    print("=" * 60)

    # Passo 1 — gerar o grafo
    print(
        f"\n[1] Gerando grafo com {NUM_NOS} nós "
        f"e {NUM_ARESTAS} arestas..."
    )
    grafo = gerar_grafo(
        NUM_NOS, NUM_ARESTAS, PESO_MIN, PESO_MAX, SEMENTE
    )

    total_arestas = sum(len(v) for v in grafo.values()) // 2
    print(
        f"    Grafo gerado: {NUM_NOS} nós, "
        f"{total_arestas} arestas."
    )
    print(f"    Pesos das arestas: [{PESO_MIN}, {PESO_MAX}]")

    # Passo 2 e 3 — Dijkstra + menor caminho
    print(
        f"\n[2] Executando Dijkstra do Nó {NO_ORIGEM} "
        f"ao Nó {NO_DESTINO}..."
    )

    inicio = time.perf_counter()
    custo, caminho = dijkstra(grafo, NO_ORIGEM, NO_DESTINO)
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000

    # Resultado
    print("\n[3] RESULTADO — Menor Caminho:")
    print("-" * 60)

    if caminho:
        rota = " → ".join(str(no) for no in caminho)
        print(f"    Rota: {rota}")
        print(f"    Custo total: {custo}")
        print(f"    Nós no caminho: {len(caminho)}")
        print(f"    Saltos (arestas): {len(caminho) - 1}")
    else:
        print("    Não foi possível encontrar um caminho.")

    print(f"\n    Tempo de execução: {tempo_ms:.4f} ms")
    print("=" * 60)


if __name__ == "__main__":
    main()