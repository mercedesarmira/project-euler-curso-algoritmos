"""
Problema 48

Enunciado: https://projecteuler.net/problem=48
Categoría: #1 
Tiempo observado: 0.01467 s
"""

def solve():
    suma = 0
    for n in range(1, 1001):
        numero = n ** n
        suma += numero

    resultado = str(suma)
    digitos = resultado[-10:]
    print(digitos)
    

if __name__ == "__main__":
    solve()