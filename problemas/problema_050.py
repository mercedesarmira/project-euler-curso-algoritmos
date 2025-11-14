"""
Problema 50

Enunciado: https://projecteuler.net/problem=50
Categoría: #1
Tiempo observado: 9.92047 s
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generador_primos(n):
    primos = []
    for i in range(n):
        if es_primo(i):
            primos.append(i)
    
    return primos


def solve():
    primo_mas_largo = 0
    longitud_max = 0
    
    primos = generador_primos(1000000)
    for i in range(len(primos)):
        suma  = 0
        for j in range(i, len(primos)):
            suma += primos[j]
            if suma > 1000000:
                break
            if es_primo(suma):
                longitud = j - i + 1
                if longitud > longitud_max:
                    longitud_max = longitud
                    primo_mas_largo = suma
    print(primo_mas_largo)

if __name__ == "__main__":
    solve()