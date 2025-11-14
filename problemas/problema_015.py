"""
Problema 15

Enunciado: https://projecteuler.net/problem=15
Categoría: #3
Complejidad: 
Tiempo observado: 0.00081 s
"""

from functools import lru_cache

@lru_cache(maxsize=None)

# Ayuda de LLM para pasar de pseudocódigo a Python
def contar_caminos(x, y, n):
    if x == n or y == n:
        return 1
    derecha = contar_caminos(x + 1, y, n)
    abajo = contar_caminos(x, y + 1, n)
    return derecha + abajo

def solve():
    print(contar_caminos(0, 0, 20))

if __name__ == "__main__":
    solve()