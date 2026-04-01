import math
import sys

sys.setrecursionlimit(10000)


def f(n):
    """
    Calcula o valor de f(n) de acordo com a fórmula:
    f(n) = 2f(n-1)+n^2

    Args:
        n (int): o número a ser calculado

    Returns:
        float: o valor calculado de f(n)
    """
    if n == 1:
        return 2
    else:
        return f(n-1) * 2 + n**2


def formula_fechada(n):
    """
    Calcula o valor de f(n) de acordo com a fórmula fechada:
    f(n) = 13 * 2^(n-1) - n^2 - 4n - 6

    Args:
        n (int): o número a ser calculado

    Returns:
        float: o valor calculado de f(n)
    """
    if n == 1:
        return 2
    else:
        return 13 * math.pow(2, n-1) - math.pow(n, 2) - 4*n - 6


n = int(input("Digite um valor para n: "))
if n < 1:
    print("n deve ser maior ou igual a 1")
else:
    print(f"O valor de f({n}) é: {f(n)}")
    print(f"O valor de formula_fechada({n}) é: {formula_fechada(n)}")
