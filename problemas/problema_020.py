"""
Problema 20

Enunciado: https://projecteuler.net/problem=20
Categoría: #1 
Tiempo observado: 0.00157 s
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def solve():
    numero = factorial(100)
    digitos = []
    for i in str(numero):
        digitos.append(int(i))
    print(sum(digitos))

if __name__ == "__main__":
    solve()