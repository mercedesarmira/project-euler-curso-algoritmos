"""
Problema 16

Enunciado: https://projecteuler.net/problem=16
Categoría: #1
Tiempo observado: 0.00066 s
"""

def solve():
    numero = 2 ** 1000
    digitos = []
    for i in str(numero):
        digitos.append(int(i))
    print(sum(digitos))

if __name__ == "__main__":
    solve()