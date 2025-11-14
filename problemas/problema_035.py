"""
Problema 35

Enunciado: https://projecteuler.net/problem=35
Categoría: #1
Tiempo observado: 8.34900 s
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def circulares(n):
    n_texto = str(n)
    circulares = []

    for i in range(len(n_texto)):
        rotacion = n_texto[i:] + n_texto[:i]
        circulares.append(int(rotacion))
    return circulares

def solve():
    contador = 0
    for n in range(2, 1000001):
        if es_primo(n):
            primo_circular = True
            for i in circulares(n):
                if not es_primo(i):
                    primo_circular = False
                    break
            if primo_circular:
                contador += 1
    print(contador)

if __name__ == "__main__":
    solve()