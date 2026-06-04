"""Implementação do Algoritmo de Bellman-Ford.

Dever de Casa - Análise de Algoritmos

Objetivos:
    - Calcular menores caminhos a partir de uma origem
    - Realizar o relaxamento das arestas
    - Detectar ciclos negativos
    - Exibir tabelas de atualização das distâncias por iteração

Complexidade:
    Tempo  : O(|V| * |E|)
    Espaço : O(|V|)
"""


# =============================================================================
# REPRESENTAÇÃO DO GRAFO
# =============================================================================

ARESTAS = [
    ("A", "B", 1),
    ("A", "C", 4),
    ("B", "C", 2),
    ("B", "D", 5),
    ("C", "D", 1),
    ("C", "E", 3),
    ("D", "C", -3),
    ("D", "E", 2),
    ("E", "D", 1),
]

VERTICE_ORIGEM = "A"


# =============================================================================
# FUNÇÕES AUXILIARES DE EXIBIÇÃO
# =============================================================================

def obter_vertices(arestas):
    """
    Extrai todos os vértices únicos a partir da lista de arestas.

    Parâmetros:
        arestas (list): Lista de tuplas (origem, destino, peso).

    Retorna:
        list: Lista ordenada de vértices únicos.

    Complexidade: O(|E|)
    """
    vertices = set()
    for origem, destino, _ in arestas:
        vertices.add(origem)
        vertices.add(destino)
    return sorted(vertices)


def exibir_tabela(iteracao, distancias, predecessores, vertices):
    """
    Exibe a tabela de distâncias e predecessores no formato pedido.

    O enunciado pede: "Tabela por iteração: A | B | C | D"
    Cada célula mostra dist[v] e predecessor[v].

    Parâmetros:
        iteracao   (int) : Número da iteração atual (0 = estado inicial).
        distancias (dict): Mapa vértice → distância mínima atual.
        predecessores (dict): Mapa vértice → vértice anterior no caminho.
        vertices   (list): Lista de vértices na ordem de exibição.

    Retorna:
        None
    """
    rotulo = "Inicial" if iteracao == 0 else f"Iteração {iteracao}"
    print(f"\n{'─' * 60}")
    print(f"  {rotulo}")
    print(f"{'─' * 60}")

    # Cabeçalho
    cabecalho = f"  {'Vértice':<10}" + "".join(f"{v:^12}" for v in vertices)
    print(cabecalho)
    print(f"  {'─' * (10 + 12 * len(vertices))}")

    # Linha de distâncias
    linha_dist = f"  {'dist':<10}"
    for v in vertices:
        d = distancias[v]
        valor = "∞" if d == float("inf") else str(d)
        linha_dist += f"{valor:^12}"
    print(linha_dist)

    # Linha de predecessores
    linha_pred = f"  {'pred':<10}"
    for v in vertices:
        p = predecessores[v] if predecessores[v] is not None else "-"
        linha_pred += f"{p:^12}"
    print(linha_pred)


def exibir_relaxamento(u, v, peso, dist_u, dist_v, nova_dist):
    """Exibe a mensagem de relaxamento de uma aresta.

    Formato conforme o enunciado:
    "Relaxando A→B: 0 + 4 < ∞ → Atualizar B = 4"

    Parâmetros:
        u        (str)  : Vértice de origem da aresta.
        v        (str)  : Vértice de destino da aresta.
        peso     (int)  : Peso da aresta u→v.
        dist_u   (float): Distância atual até u.
        dist_v   (float): Distância atual até v (antes do relaxamento).
        nova_dist(float): Nova distância calculada (dist_u + peso).

    Retorna:
        None
    """
    du_str = str(int(dist_u)) if dist_u != float("inf") else "∞"
    dv_str = str(int(dist_v)) if dist_v != float("inf") else "∞"
    nd_str = str(int(nova_dist)) if nova_dist != float("inf") else "∞"
    print(
        f"    Relaxando {u}→{v}: {du_str} + {peso} = {nd_str} < {dv_str}"
        f"  →  Atualizar {v} = {nd_str}"
    )


# =============================================================================
# ALGORITMO DE BELLMAN-FORD
# =============================================================================

def bellman_ford(arestas, origem):
    """
    Executa o algoritmo de Bellman-Ford para caminhos mínimos.

    Ideia central (programação dinâmica):
        dist[v] após k iterações = menor caminho de 'origem' a 'v'
        usando no máximo k arestas.

        Como qualquer caminho simples tem no máximo |V|-1 arestas,
        após |V|-1 iterações dist[v] já contém a resposta ótima —
        a menos que exista um ciclo negativo.

    Passo de relaxamento:
        Para cada aresta (u, v, w):
            se dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

    Detecção de ciclo negativo:
        Se após |V|-1 iterações ainda for possível relaxar alguma aresta,
        existe um ciclo negativo alcançável a partir da origem.

    Parâmetros:
        arestas (list): Lista de tuplas (origem, destino, peso).
        origem  (str) : Vértice fonte.

    Retorna:
        tuple: (distancias, predecessores, ciclo_negativo)
            distancias     (dict): Distâncias mínimas finais.
            predecessores  (dict): Predecessores no caminho mínimo.
            ciclo_negativo (bool): True se houver ciclo negativo.

    Complexidade: O(|V| * |E|)
    """
    vertices = obter_vertices(arestas)
    num_vertices = len(vertices)

    distancias = {v: float("inf") for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[origem] = 0

    print("=" * 60)
    print("  ALGORITMO DE BELLMAN-FORD")
    print(
        f"  Origem: {origem}  |  Vértices: {num_vertices}"
        f"  |  Arestas: {len(arestas)}"
    )
    print("=" * 60)

    exibir_tabela(0, distancias, predecessores, vertices)
    for i in range(1, num_vertices):
        print(f"\n{'━' * 60}")
        print(f"  ITERAÇÃO {i}  (garante caminhos com até {i} aresta(s))")
        print(f"{'━' * 60}")

        houve_atualizacao = False

        for u, v, peso in arestas:
            # Só relaxa se u já foi alcançado (dist[u] != ∞)
            if distancias[u] == float("inf"):
                continue

            nova_dist = distancias[u] + peso

            if nova_dist < distancias[v]:
                exibir_relaxamento(
                    u, v, peso,
                    distancias[u], distancias[v],
                    nova_dist
                )
                distancias[v] = nova_dist
                predecessores[v] = u
                houve_atualizacao = True

        exibir_tabela(i, distancias, predecessores, vertices)

        if not houve_atualizacao:
            print(f"\n  ✓ Convergência antecipada na iteração {i}.")
            break

    print(f"\n{'=' * 60}")
    print("  VERIFICAÇÃO DE CICLO NEGATIVO (iteração extra)")
    print(f"{'=' * 60}")

    ciclo_negativo = False
    for u, v, peso in arestas:
        if distancias[u] == float("inf"):
            continue
        if distancias[u] + peso < distancias[v]:
            ciclo_negativo = True
            print(f"\n  CICLO NEGATIVO DETECTADO!")
            print(
                f"     Aresta {u}→{v} (peso {peso})"
                f" ainda pode ser relaxada."
            )
            dist_nova = distancias[u] + peso
            print(
                f"     dist[{u}] + {peso} = {dist_nova}"
                f" < dist[{v}] = {distancias[v]}"
            )
            break

    if not ciclo_negativo:
        print("  ✓ Nenhum ciclo negativo detectado.")

    return distancias, predecessores, ciclo_negativo


# =============================================================================
# RECONSTRUÇÃO E EXIBIÇÃO DO CAMINHO MÍNIMO
# =============================================================================

def reconstruir_caminho(predecessores, origem, destino):
    """Reconstrói o caminho mínimo da origem até o destino.

    Segue a cadeia de predecessores de trás para frente.

    Parâmetros:
        predecessores (dict): Mapa vértice → predecessor.
        origem        (str) : Vértice de partida.
        destino       (str) : Vértice de chegada.

    Retorna:
        list | None: Lista de vértices do caminho, ou None se inalcançável.

    Complexidade: O(|V|)
    """
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        if atual == origem:
            break
        atual = predecessores[atual]
    else:
        return None  # origem não foi atingida

    if caminho[-1] != origem:
        return None

    caminho.reverse()
    return caminho


def exibir_resultados(distancias, predecessores, origem, vertices):
    """
    Exibe a tabela final de caminhos mínimos e os caminhos reconstruídos.

    Parâmetros:
        distancias    (dict): Distâncias mínimas finais.
        predecessores (dict): Predecessores no caminho mínimo.
        origem        (str) : Vértice de partida.
        vertices      (list): Lista de todos os vértices.

    Retorna:
        None
    """
    print(f"\n{'=' * 60}")
    print("  RESULTADO FINAL — CAMINHOS MÍNIMOS")
    print(f"  Origem: {origem}")
    print(f"{'=' * 60}")
    print(f"  {'Destino':<10} {'Distância':<12} {'Caminho'}")
    print(f"  {'─' * 50}")

    for v in vertices:
        dist = distancias[v]
        dist_str = str(dist) if dist != float("inf") else "∞ (inalcançável)"

        caminho = reconstruir_caminho(predecessores, origem, v)
        caminho_str = " → ".join(caminho) if caminho else "—"

        print(f"  {v:<10} {dist_str:<12} {caminho_str}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Ponto de entrada: executa Bellman-Ford com o grafo do enunciado."""
    vertices = obter_vertices(ARESTAS)

    distancias, predecessores, ciclo_negativo = bellman_ford(
        ARESTAS, VERTICE_ORIGEM
    )

    if not ciclo_negativo:
        exibir_resultados(distancias, predecessores, VERTICE_ORIGEM, vertices)
    else:
        print(
            "\n  ⚠️  Resultados podem ser inválidos devido ao ciclo negativo."
        )


if __name__ == "__main__":
    main()