import math

def analisador_complexidade(a, b, k, p):
    """
    Analisador de complexidade para o Teorema Mestre.

    A função printa a entrada, a expressão de f(n) e o resultado da análise de complexidade.

    A análise de complexidade é baseada no Teorema Mestre, que define a complexidade de um algoritmo como sendo T(n) = aT(n/b) + f(n),
    onde a > 0 e b > 1 são constantes, f(n) é um polinômio de grau k e n^(log_b a) é o termo dominante.

    Parameters:
        a (float): o valor de a no Teorema Mestre
        b (float): o valor de b no Teorema Mestre
        k (float): o grau do polinômio f(n)
        p (float): o expoente de log(n) no polinômio f(n)

    Returns:
        None
    """
    log_b_a = math.log(a, b)
    eps = 1e-9

    print(f"\nEntrada: a={a}, b={b}, k={k}, p={p}")
    print(f"f(n) = n^{k}" + (f" * log^{p}(n)" if p != 0 else ""))
    print(f"n^(log_{b} {a}) = n^{log_b_a:.4f}")
    print("-" * 45)

    if abs(k - log_b_a) < eps:
        if p >= 0:
            print("Caso 2 do Teorema Mestre: f(n) = n^(log_b a)")
            if p == 0:
                print(f"Resultado: T(n) = Θ(n^{log_b_a:.4f} * log(n))")
            else:
                print(f"Resultado: T(n) = Θ(n^{log_b_a:.4f} * log^{p+1}(n))")
        else:
            print("Caso 2 estendido (p < 0)")
            print(f"Resultado: T(n) = Θ(n^{log_b_a:.4f})")

    elif k < log_b_a:
        print("Caso 1 do Teorema Mestre: f(n) < n^(log_b a)")
        print(f"Resultado: T(n) = Θ(n^{log_b_a:.4f})")

    else:
        print("Caso 3 do Teorema Mestre: f(n) > n^(log_b a)")
        print(f"Resultado: T(n) = Θ(n^{k}" + (f" * log^{p}(n))" if p != 0 else ")"))

print("=== Analisador de Complexidade — Teorema Mestre ===")

# Caso Merge Sort: a = 2, b = 2, k = 1, p = 0
# Caso Multiplicação de matrizes: a = 8, b = 2, k = 2, p = 0
# Caso 2T(n/4) + √n : a = 2, b = 4, k = 0.5, p = 0
# Caso 2T(n/4) + n : a = 2, b = 4, k = 1, p = 0
# Caso 16T(n/4) + n^2 : a = 16, b = 4, k = 2, p = 0

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
k = float(input("Digite o valor de k: "))
p = float(input("Digite o valor de p (expoente de log(n), digite 0 se não houver): "))

analisador_complexidade(a, b, k, p)