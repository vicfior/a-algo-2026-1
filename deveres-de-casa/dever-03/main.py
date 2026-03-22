def palindromo(s):
    """
    Verifica se uma palavra é um palíndromo.

    Args:
        s (str): A palavra a ser verificada.

    Returns:
        "É Palíndromo" ou "Não é Palíndromo".
    """
    if len(s) <= 1:
        return "É Palíndromo"
    else:
        if s[0] == s[-1]:
            return palindromo(s[1:-1])
        else:
            return "Não é Palíndromo"


print(palindromo([0, 1, 2, 3, 2, 1, 0]))
print(palindromo(["a", "b", "b", "a"]))
print(palindromo(["a", "b", "c", "b", "a"]))
print(palindromo(["a", "b", "c", "f", "b", "a"]))
