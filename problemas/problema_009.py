"""
Problema 9

Enunciado: https://projecteuler.net/problem=9
Categoría: #1
Tiempo observado: 0.04050 s
"""

def solve():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c > b and a * a + b * b == c * c:
                producto = a * b * c
                print(producto)
                return

if __name__ == "__main__":
    solve()


