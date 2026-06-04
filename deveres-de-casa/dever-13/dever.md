# Redução Polinomial do Problema do Ciclo Hamiltoniano para o Problema do Caixeiro Viajante

## Introdução

A empresa de logística já possui um software capaz de resolver perfeitamente o Problema do Caixeiro Viajante (TSP). Entretanto, um novo contrato exige a resolução do Problema do Ciclo Hamiltoniano.

O objetivo deste trabalho é demonstrar que o software existente pode ser utilizado para resolver o novo problema por meio de uma redução polinomial.

## Definição dos Problemas

### Problema do Ciclo Hamiltoniano

Dado um grafo \(G=(V,E)\), deseja-se determinar se existe um ciclo que:

- visite todos os vértices exatamente uma vez;
- retorne ao vértice inicial.

### Problema do Caixeiro Viajante (TSP)

Dado um conjunto de cidades e as distâncias entre elas, deseja-se encontrar a rota de menor custo que:

- visite todas as cidades exatamente uma vez;
- retorne ao ponto de partida.

## Construção da Redução

Considere uma instância qualquer do Problema do Ciclo Hamiltoniano representada por um grafo \(G=(V,E)\) com \(n\) vértices.

A transformação para uma instância do TSP é feita da seguinte maneira:

1. Mantêm-se os mesmos vértices do grafo original.
2. Constrói-se um grafo completo entre todos os vértices.
3. Para cada par de vértices:

   - Se a aresta existir no grafo original, atribui-se peso **1**.
   - Se a aresta não existir no grafo original, atribui-se peso **2**.

Após essa transformação, o grafo está pronto para ser processado pelo software que resolve o TSP.

## Utilização do Software Existente

O software de TSP é executado sobre a instância construída.

Como existem \(n\) vértices, qualquer ciclo que visite todos eles utilizará exatamente \(n\) arestas.

Observe que:

- Se existir um ciclo hamiltoniano no grafo original, será possível percorrer todos os vértices utilizando apenas arestas de peso 1.
- Nesse caso, o custo total da rota será exatamente \(n\).

Por outro lado:

- Se não existir ciclo hamiltoniano, qualquer rota que visite todos os vértices precisará utilizar pelo menos uma aresta artificial de peso 2.
- Assim, o custo total será maior que \(n\).

Portanto:

- Se o custo ótimo encontrado pelo TSP for igual a \(n\), existe um ciclo hamiltoniano.
- Se o custo ótimo for maior que \(n\), não existe ciclo hamiltoniano.

## Prova de Correção

### Caso 1: Existe um ciclo hamiltoniano

Se o grafo possuir um ciclo hamiltoniano, todas as arestas desse ciclo pertencem ao grafo original e possuem peso 1. Como o ciclo utiliza exatamente \(n\) arestas, o custo total será:

\[
n
\]

Logo, o solucionador de TSP encontrará uma solução de custo \(n\).

### Caso 2: O solucionador retorna custo \(n\)

Se o custo encontrado for exatamente \(n\), então todas as arestas utilizadas possuem peso 1.

Consequentemente, todas essas arestas pertencem ao grafo original.

Como a rota visita todos os vértices exatamente uma vez e retorna ao início, ela constitui um ciclo hamiltoniano.

Assim, existe um ciclo hamiltoniano no grafo original.

## Complexidade da Transformação

A construção do grafo completo exige apenas verificar a existência de arestas entre pares de vértices e atribuir pesos 1 ou 2.

Esse procedimento pode ser realizado em:

O(n²)

que é tempo polinomial.

Portanto, a transformação é uma redução polinomial.

## Conclusão

Foi demonstrado que qualquer instância do Problema do Ciclo Hamiltoniano pode ser transformada, em tempo polinomial, em uma instância do Problema do Caixeiro Viajante.

Dessa forma, caso exista um software capaz de resolver perfeitamente o TSP, ele pode ser utilizado para resolver o Problema do Ciclo Hamiltoniano através da transformação apresentada.

Conclui-se, portanto, que:

Ciclo Hamiltoniano ≤ₚ Caixeiro Viajante

Logo, o software já existente na empresa é suficiente para atender ao novo contrato.