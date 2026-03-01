import random
import time


def insertion_sort(array):
    """
    Ordenação de uma lista usando o insertion sort

    Args:
        array (list): a lista a ser ordenada

    Returns:
        lista: a lista ordenada
    """
    for i in range(1, len(array)):
        aux = array[i]
        j = i-1
        while (j >= 0 and aux < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = aux
    return array


n = [1000, 5000, 10000, 20000, 50000]
for i in n:
    lista = []
    for j in range(i):
        lista.append(random.randint(0, 1000))
    print('insertion sort')
    start = time.time()
    insertion_sort(lista.copy())
    end = time.time()
    print(f"Tempo de execução para {i} elementos: {end - start}")
    print('sorted')
    start = time.time()
    sorted(lista.copy())
    end = time.time()
    print(f"Tempo de execução para {i} elementos: {end - start}")