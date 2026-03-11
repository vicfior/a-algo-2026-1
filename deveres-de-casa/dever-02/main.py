import time
import sys

# Mecanismo para definir o chamado de funções recursivas com o limite de 2000
sys.setrecursionlimit(2000)


def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão

    Args:
        n (int): o número a ser calculado

    Returns:
        int: o fatorial do número
    """
    if n <= 1:  # Condicional para n menor ou igual a 1
        return 1
    else:  # Chamada recursiva
        # Retorna n! = n * (n-1) * (n-2) * ... * 1 fazendo a chamada recursiva
        return n * fatorial(n - 1)


# Lista com os números a serem calculados para os fatoriais
lista = [10, 100, 500, 1000]

# Loop para calcular os fatoriais
for x in lista:
    # Inicia o cronômetro de segundos fracionários
    start = time.perf_counter()
    # Guarda o resultado do fatorial de x na variável fatorial_n
    fatorial_n = fatorial(x)
    # Para o cronômetro
    end = time.perf_counter()
    # Imprime o tempo de execução
    print(f"Fatorial de {x}: {fatorial_n}")
    print("Tempo de execução: ", end - start)

# -- Análise de complexidade: --
# A função de fatorial possui complexidade linear O(n), pois realiza
# n multiplicações para calcular o fatorial de um número n.
#
# Esse algoritmo possui relação de recorrência de:
# T(n) = T(n-1) + O(1) ou T(n) = T(n-1) + 1
# Considerando que T(n-1) = T(n-2) + 1 então T(n) = T(n-2) + 2
# e assim por diante, logo T(n) = T(n-k) + k.
#
# Para atingir o caso base em que n <= 1, é necessário chegar a T(0),
# para n-k=0 tem-se n=k, portanto T(n) = T(n-n) + n,
# resultando em T(n) = T(0) + n ou T(n) = n.
# Logo, o algoritmo possui complexidade linear O(n).
