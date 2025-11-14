"""
Problema 31

Enunciado: https://projecteuler.net/problem=31
Categoría: #1
Tiempo observado: 0.02056 s
"""

def solve():
    formas = 0
    for a in range(0, 201, 200):
        for b in range(0, 201 - a, 100):
            for c in range(0, 201 - a - b, 50):
                for d in range(0, 201 - a - b - c, 20):
                    for e in range(0, 201 - a - b - c - d, 10):
                        for f in range(0, 201 - a - b - c - d - e, 5):
                            for g in range(0, 201 - a - b - c - d - e - f, 2):
                                suma = a + b + c + d + e + f + g
                                if suma <= 200:
                                    formas += 1
    print(formas)

if __name__ == "__main__":
    solve()