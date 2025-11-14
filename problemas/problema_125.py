"""
Problema 125

Enunciado: https://projecteuler.net/problem=125
Categoría: #4
Tiempo observado: 0.00051 s
Rating: 25
Puntuación: 1
"""

LIMIT = 10**8  
end_max = 1
while True:
    b = end_max + 1
    if (b-1)**2 + b**2 >= LIMIT:
        break
    end_max = b

prefix = [0] 
for i in range(1, end_max + 1):
    prefix.append(prefix[-1] + i*i)

n = len(prefix) - 1  
palindromic_sums = set()
for start in range(1, n+1):
    for end in range(start + 1, n+1): 
        s = prefix[end] - prefix[start - 1] 
        if s >= LIMIT:
            break 
        if str(s) == str(s)[::-1]:
            palindromic_sums.add(s)


def solve():
    answer = sum(palindromic_sums)
    print(answer)

if __name__ == "__main__":
    solve()