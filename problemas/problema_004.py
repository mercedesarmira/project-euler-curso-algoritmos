"""
Problema 4

Enunciado: https://projecteuler.net/problem=4
Categoría: #1
Tiempo observado: 0.36475 s
"""

def solve():
    palindromos = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            producto = i * j
            if str(producto) == str(producto)[::-1]:
                palindromos.append(producto)
    print(max(palindromos))

if __name__ == "__main__":
    solve()