from typing import Dict, List, Tuple, Optional, Set

# Criação de um "Type Alias" para facilitar a leitura da tipagem do grafo
GrafoType = Dict[str, List[Tuple[str, int]]]


def calcular_rota_fibra(grafo: GrafoType, vertice_inicial: str) -> Tuple[List[Tuple[str, str, int]], int]:
    """
    Calcula a Árvore Geradora Mínima (MST) de um grafo ponderado e não
    direcionado utilizando o Algoritmo de Prim.

    Args:
        grafo: Dicionário representando o grafo em formato de Lista de Adjacência.
        vertice_inicial: O nó de partida para a construção da árvore.

    Returns:
        Uma tupla contendo:
        - A lista das arestas que compõem a MST no formato (origem, destino, peso).
        - O custo total (inteiro) da rota.
    """
    menor_peso: Dict[str, float] = {}
    predecessor: Dict[str, Optional[str]] = {}

    # Inicialização dos vértices
    for v in grafo:
        menor_peso[v] = float('inf')
        predecessor[v] = None

    menor_peso[vertice_inicial] = 0
    nao_visitados: Set[str] = set(grafo.keys())

    mst: List[Tuple[str, str, int]] = []
    custo_total = 0

    while nao_visitados:
        u: Optional[str] = None
        menor_valor = float('inf')

        # Busca manual do vértice com o menor peso disponível
        for vertice in nao_visitados:
            if menor_peso[vertice] < menor_valor:
                menor_valor = menor_peso[vertice]
                u = vertice

        # Se u continuar None, o grafo é desconexo; podemos abortar
        if u is None:
            break

        nao_visitados.remove(u)

        # Adiciona a aresta à Árvore Geradora Mínima
        if predecessor[u] is not None:
            # O type ignore/cast indireto aqui garante que o predecessor é string, não None
            mst.append((predecessor[u], u, int(menor_peso[u])))  # type: ignore
            custo_total += int(menor_peso[u])

        # Atualiza os pesos dos vértices adjacentes
        for v, peso in grafo[u]:
            if v in nao_visitados and peso < menor_peso[v]:
                predecessor[v] = u
                menor_peso[v] = peso

    return mst, custo_total


def main() -> None:
    """Função principal para instanciar dados e executar o algoritmo."""
    # Representação do grafo (Lista de Adjacência)
    polos_tecnologicos: GrafoType = {
        'A': [('B', 4), ('C', 4)],
        'B': [('A', 4), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 5), ('E', 6)],
        'D': [('B', 5), ('C', 5), ('E', 3), ('F', 4)],
        'E': [('C', 6), ('D', 3), ('F', 2)],
        'F': [('D', 4), ('E', 2)]
    }

    rota_instalacao, km_totais = calcular_rota_fibra(polos_tecnologicos, 'A')

    # Saída de dados formatada
    print("ROTA DOS CABOS A SEREM INSTALADOS (em ordem):")
    print("-" * 55)

    for origem, destino, km in rota_instalacao:
        print(f"Conectar Polo {origem} ao Polo {destino} -> "
              f"Utilizando {km} Km de fibra")

    print("-" * 55)
    print(f"Quantidade total mínima de quilômetros "
          f"de cabos utilizados: {km_totais} Km")


if __name__ == "__main__":
    main()