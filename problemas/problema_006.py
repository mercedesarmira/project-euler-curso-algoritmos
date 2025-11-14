"""
Problema 6

Enunciado: https://projecteuler.net/problem=6
Categoría: #1
Tiempo observado: 0.00182 s
"""

def suma_cuadrados(n):
    cuadrados = []
    for i in range(n + 1):
        j = i ** 2
        cuadrados.append(j)
    return sum(cuadrados)

def cuadrado_dela_suma(n):
    numeros = []
    for i in range(n + 1):
        numeros.append(i)
    cuadrado = sum(numeros) ** 2
    return cuadrado

def solve():
    a = cuadrado_dela_suma(100)
    b = suma_cuadrados(100)
    diferencia = a - b
    print(diferencia)

if __name__ == "__main__":
    solve()