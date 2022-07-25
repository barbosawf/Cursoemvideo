"""
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""
print('Desafio 052')

n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        t += 1
if t == 2:
    print('O número é primo!\n')
else:
    print('O número não é primo!\n')


num = int(input('Digite um número: '))
tot = 0
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
    cont += 1
    if cont % 25 == 0:
        print('')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot), end=' ')
if tot == 2:
    print('e por isso ele é PRIMO!\n')
else:
    print('e por isso ele NÃO É PRIMO!\n')


numero = int(input("Número: "))
divisores = []
for x in range(1, numero + 1):
    if numero % x == 0:
        divisores.append(x)
if len(divisores) == 2:
    print("É um número primo!")
else:
    print("Não é primo!")
print(divisores)
