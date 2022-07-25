"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
"""
i = 1
n = int(input('Digite um número: '))
fat = 1
while i <= n:
    fat = fat*i
    i = i + 1

print(fat)

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')