"""
Problema 19

Enunciado: https://projecteuler.net/problem=19
Categoría: #3
Tiempo observado: 0.00487 s
"""

def bisiesto(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def dias_mes(mes, anio):
    if mes in (4, 6, 9, 11):
        dias = 30
    elif mes == 2:
        if bisiesto(anio):
            dias = 29
        else:
            dias = 28
    else:
        dias = 31
    return list(range(1, dias + 1))

# Ayuda de LLM para completar y verificar esta función
def agrupar_en_semanas(dias_del_mes, semana_incompleta):
    semanas = []

    if len(semana_incompleta) > 0:
        while len(semana_incompleta) < 7:
            primer_dia = dias_del_mes.pop(0)
            semana_incompleta.append(primer_dia)
        semanas.append(semana_incompleta)

    while len(dias_del_mes) > 0:
        semana = dias_del_mes[:7]
        dias_del_mes = dias_del_mes[7:]
        semanas.append(semana)

    if len(semanas[-1]) < 7:
        semana_incompleta = semanas.pop()
    else:
        semana_incompleta = []

    return semanas, semana_incompleta


def solve():
    semana_incompleta = []
    domingos = 0

    for anio in range(1900, 2001):
        for mes in range(1, 13):
            dias_del_mes = dias_mes(mes, anio)
            semanas, semana_incompleta = agrupar_en_semanas(dias_del_mes, semana_incompleta)

            if anio >= 1901:
                for semana in semanas:
                    if semana[6] == 1:
                        domingos += 1
    print(domingos)

if __name__ == "__main__":
    solve()