"""
Problema 25

Enunciado: https://projecteuler.net/problem=25
Categoría: #1 
Tiempo observado: 0.04776 s
"""

def solve():
    Fib1 = 1
    Fib2 = 1
    indice = 2

    while len(str(Fib2)) < 1000:
        Fib3 = Fib1 + Fib2
        Fib1 = Fib2
        Fib2 = Fib3
        indice = indice + 1

    print(indice)

if __name__ == "__main__":
    solve()