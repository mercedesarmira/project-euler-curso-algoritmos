"""
Problema 7

Enunciado: https://projecteuler.net/problem=7
Categoría: #2
Complejidad:  
Tiempo observado: 33.49342 s
"""

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:   
            return False
    return True

def solve():
    contador = 0
    numero = 1

    while contador < 10001:
        numero += 1
        if es_primo(numero):
            contador += 1

    print(numero)

if __name__ == "__main__":
    solve()