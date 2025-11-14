"""
Problema 39

Enunciado: https://projecteuler.net/problem=39
Categoría: #1
Tiempo observado: 8.33111 s
"""

def solve():
    p_max = 0
    soluciones = 0

    for p in range(1, 1001):
        contador = 0
        for a in range(1, p):
            for b in range(a, p-a):
                c = p - a - b
                if c > b and a * a + b * b == c * c:
                    contador += 1
        
        if contador > soluciones:
            soluciones = contador
            p_max = p
    
    print(p_max)

if __name__ == "__main__":
    solve()