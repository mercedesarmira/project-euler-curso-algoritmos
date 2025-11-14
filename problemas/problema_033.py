"""
Problema 33

Enunciado: https://projecteuler.net/problem=33
Categoría: #1
Tiempo observado: 0.00414 s
"""

def eliminar_comun(a, b):
    a_texto = str(a)
    b_texto = str(b)

    for i in a_texto:
        if i in b_texto:
            a_texto = a_texto.replace(i, "", 1)
            b_texto = b_texto.replace(i, "", 1)
            return a_texto, b_texto
    return None
    

def mcd(a, b):
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    return a

def simplificar_fraccion(a, b):
    divisor = mcd(a, b)
    numerador = a // divisor
    denominador = b // divisor
    return numerador, denominador

def solve():
    numeradores = []
    denominadores = []

    for a in range(10, 100):
        for b in range(10, 100):
            if a >= b:   
                continue
            if a % 10 == 0 and b % 10 == 0:
                continue

            resultado = eliminar_comun(a, b)
            if resultado is not None:
                a_texto, b_texto = resultado
                nuevo_a = int(a_texto)
                nuevo_b = int(b_texto)
                if a * nuevo_b == b * nuevo_a:
                    numeradores.append(nuevo_a)
                    denominadores.append(nuevo_b)

    producto_numeradores = 1
    for j in numeradores:
        producto_numeradores *= j
                    
    producto_denominadores = 1
    for j in denominadores:
        producto_denominadores *= j

    n, denominador = simplificar_fraccion(producto_numeradores,
                                                  producto_denominadores)
                    
    print(denominador)

if __name__ == "__main__":
    solve()