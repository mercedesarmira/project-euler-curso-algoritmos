"""
Problema 10

Enunciado: https://projecteuler.net/problem=10
Categoría: #1 
Tiempo observado: 12.10970 s
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    primos = []
    for i in range(2, 2000000):
        if es_primo(i):
            primos.append(i)
    print(sum(primos))

if __name__ == "__main__":
    solve()