"""
Problema 5

Enunciado: https://projecteuler.net/problem=5
Categoría: #1 
Tiempo observado: 0.00133 s
"""

# Algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    return a

# Fórmula del mcm
def mcm(a, b):
    return a * b // mcd(a, b)

def solve():
    multiplo = 6
    for i in range(6, 21):
        multiplo = mcm(multiplo, i)
    print(multiplo)

if __name__ == "__main__":
    solve()