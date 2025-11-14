"""
Problema 77

Enunciado: https://projecteuler.net/problem=77
Categoría: #4
Tiempo observado: 0.00601 s
Rating: 25
Puntuación: 1
Enlace chat LLM: https://chatgpt.com/share/6916ce5e-4d3c-800f-b225-34f700accb3c   
""" 

from typing import List, Tuple


def primes_upto(n: int) -> List[int]:
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
    n = 2
    while True:
        primes = primes_upto(n)
        ways = [0] * (n + 1)
        ways[0] = 1
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