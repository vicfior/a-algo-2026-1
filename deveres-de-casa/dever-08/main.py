"""Implementação simples do algoritmo de Floyd-Warshall.

Objetivo: encontrar o menor caminho entre TODOS os pares de vértices.

Paradigma: Programação Dinâmica.
Complexidade de tempo: Theta(|V|^3) — três laços aninhados sobre
todos os vértices, sem saída antecipada.
Complexidade de espaço: Theta(|V|^2) — uma matriz N x N.
"""

import math

def floyd_warshall(n, dist):
    """Calcula o caminho mínimo entre todos os pares de vértices.

    Aplica a recorrência:
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    para cada vértice intermediário k, liberando um vértice por fase.

    Args:
        n (int): número de vértices do grafo.
        dist (list[list[float]]): matriz de adjacência N x N com os
            pesos das arestas; use math.inf onde não há aresta direta
            e 0 na diagonal principal.

    Returns:
        list[list[float]] | None: matriz de distâncias mínimas entre
            todos os pares, ou None se houver ciclo negativo.
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        if dist[i][i] < 0:
            print("Ciclo negativo detectado — resultado inválido.")
            return None

    return dist


def print_matrix(dist, labels):
    """Exibe a matriz de distâncias formatada com rótulos de vértices.

    Args:
        dist (list[list[float]]): matriz de distâncias mínimas.
        labels (list[str]): rótulos dos vértices (ex.: ['A','B','C','D']).
    """
    header = f"{'':>6}" + "".join(f"{label:>8}" for label in labels)
    print(header)
    print("-" * (6 + 8 * len(labels)))
    for i, row in enumerate(dist):
        values = ""
        for val in row:
            values += f"{'INF':>8}" if val == math.inf else f"{val:>8.0f}"
        print(f"{labels[i]:>6} {values}")


def main():
    """Executa o Floyd-Warshall no grafo de exemplo do slide."""
    INF = math.inf

    # Grafo do slide: vértices A, B, C, D
    # Arestas: A->B=2, A->D=3, B->A=3, B->C=2, C->D=4, D->A=-2, D->B=6
    labels = ["A", "B", "C", "D"]
    n = len(labels)

    dist_matrix = [
        [0, 2, INF, 3],
        [3, 0, 2, INF],
        [INF, INF, 0, 4],
        [-2, 6, INF, 0],
    ]

    print("=== Floyd-Warshall — Implementação Simples ===\n")
    print("Matriz inicial (arestas diretas):")
    print_matrix(dist_matrix, labels)

    result = floyd_warshall(n, dist_matrix)

    if result is not None:
        print("\nMatriz final (menores distâncias entre todos os pares):")
        print_matrix(result, labels)


if __name__ == "__main__":
    main()