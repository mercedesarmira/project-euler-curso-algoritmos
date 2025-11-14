"""
Problema 41

Enunciado: https://projecteuler.net/problem=41
Categoría: #2
Complejidad: 
Tiempo observado: 225.64821 s
"""

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:   
            return False
    return True

def generar_permutaciones(numero : str):
    permutaciones_totales = []

    if len(numero) == 1:
        permutaciones_totales.append(numero)

    for i in range(len(numero)):
        letra_fija = numero[i]
        letras_sobrantes = numero[:i] + numero[i+1:]
        sub_permutaciones = generar_permutaciones(letras_sobrantes)

        for j in sub_permutaciones:
            permutaciones_totales.append(letra_fija + j)
    return permutaciones_totales

def generar_cadena(n):
    cadena = ""
    k = 1
    while k <= n:
        cadena += str(k)
        k += 1
    return cadena

def solve():
    n = 9  
    while n >= 1:
        cadena = generar_cadena(n)
        permutaciones = sorted(generar_permutaciones(cadena), reverse=True)

        mayor_primo = 0
        for i in permutaciones:
            numero = int(i)
            if es_primo(numero):
                if numero > mayor_primo:
                    mayor_primo = numero
                    return mayor_primo
        n -= 1
    return None

if __name__ == "__main__":
    solve()