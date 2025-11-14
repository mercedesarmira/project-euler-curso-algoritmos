"""
Problema 3

Enunciado: https://projecteuler.net/problem=3
Categoría: #1 
Tiempo observado: 0.07914 s
"""

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solve():
    n = 600851475143
    primos = []
    limite = int(n ** 0.5) + 1

    for i in range(2, limite):
        if n % i == 0:
            if es_primo(i):
                primos.append(i)

    print(max(primos))

if __name__ == "__main__":
    solve()