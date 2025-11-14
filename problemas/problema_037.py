"""
Problema 37

Enunciado: https://projecteuler.net/problem=37
Categoría: #1
Tiempo observado: 8.27963 s
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def eliminar_izquierda(n):
    n_texto = str(n)
    resultado = []
    for i in range(len(n_texto)):
        numero_generado = int(n_texto[i:])
        resultado.append(numero_generado)
    return resultado

def eliminar_derecha(n):
    n_texto = str(n)
    resultado = []
    for i in range(len(n_texto)):
        numero_generado = int(n_texto[:len(n_texto)-i])
        resultado.append(numero_generado)
    return resultado

def solve():
    primos_truncables = []
    for n in range(11, 1000000):
        if es_primo(n):
            numeros_primos_izquierda = True
            for i in eliminar_izquierda(n):
                if not es_primo(i):
                    numeros_primos_izquierda = False
                    break
            if numeros_primos_izquierda:
                numeros_primos_derecha = True
                for j in eliminar_derecha(n):
                    if not es_primo(j):
                        numeros_primos_derecha = False
                        break
                if numeros_primos_derecha:
                    primos_truncables.append(n)
    print(sum(primos_truncables))

if __name__ == "__main__":
    solve()