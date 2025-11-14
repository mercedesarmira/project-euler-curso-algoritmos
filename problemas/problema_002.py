"""
Problema 2

Enunciado: https://projecteuler.net/problem=2
Categoría: #1 
Tiempo observado: 0.00149 s
"""

def solve():

    Fib1 = 1
    Fib2 = 2
    pares = []

    while Fib2 < 4000000:
        if Fib2 % 2 == 0:
            pares.append(Fib2)
        Fib3 = Fib1 + Fib2
        Fib1 = Fib2
        Fib2 = Fib3

    print(sum(pares))

if __name__ == "__main__":
    solve()