"""
Ler o primeiro termo e a razão de uma PA e mostrar a soma.
"""

n = int(input('Qual é o primeiro termo da PA: '))
p = n
r = int(input('Qual é a razão da PA: '))
z = 0

for c in range(1, 11):
    print(n, end=' ➡ ')
    n += r
    z = n - r
print('ACABOU!')
print('O resultado da PA de primeiro termo {} e razão {} é {}.\n'. format(p, r, z))


p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r + r
for c in range(p, d, r):
    print('{} '.format(c), end='➡ ')
print('ACABOU!')
