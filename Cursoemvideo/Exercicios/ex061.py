"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r + r
for c in range(p, d, r):
    print('{} '.format(c), end='➡ ')
print('ACABOU!')
print('')

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = 10
c = 0

while c < d:
    print('{} '.format(p), end='➡ ')
    p += r
    c += 1
print('ACABOU!')
