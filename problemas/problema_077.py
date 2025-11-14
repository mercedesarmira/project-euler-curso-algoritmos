"""
Problema 77

Enunciado: https://projecteuler.net/problem=77
Categoría: #4
Complejidad: 
Tiempo observado: 0.00601 s
Enlace chat LLM:
"""

from typing import List, Tuple


def primes_upto(n: int) -> List[int]:
    """Devuelve la lista de primos <= n usando la criba de Eratóstenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    limit = int(n**0.5) + 1
    for p in range(2, limit):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n + 1:step] = [False] * (((n - start) // step) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def first_with_more_than(limit_ways: int) -> Tuple[int, int]:
    """
    Busca el menor entero n tal que el número de formas de escribir n
    como suma de primos (combinaciones, orden no importa) sea > limit_ways.
    Retorna (n, cantidad_de_formas).
    """
    n = 2
    while True:
        primes = primes_upto(n)
        # ways[x] = número de formas de formar x usando primos (combinaciones)
        ways = [0] * (n + 1)
        ways[0] = 1  # hay una forma de formar 0: usar ninguna moneda
        # Técnica tipo "coin change": iterar primos y actualizar combinaciones
        for p in primes:
            for value in range(p, n + 1):
                ways[value] += ways[value - p]
        if ways[n] > limit_ways:
            return n, ways[n]
        n += 1

def solve():
    n_answer, count_answer = first_with_more_than(5000)
    print(n_answer)


if __name__ == "__main__":
    solve()