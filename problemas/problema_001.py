"""

Problema 1

Enunciado: https://projecteuler.net/problem=1
Categoría: #1
Complejidad: 
Tiempo observado:

"""
def solve():
    multiplos = []
    for i in range(1000):
        if i % 5 == 0 or i % 3 == 0 :
            multiplos.append(i)
    print(sum(multiplos))

if __name__ == "__main__":
    solve()