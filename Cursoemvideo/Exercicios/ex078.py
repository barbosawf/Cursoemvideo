"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

print('='*70)
num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite o {c + 1}º número: ')))

print('='*70)
pos_max = list()
pos_min = list()
for c, v in enumerate(num):
    if v == max(num):
        pos_max.append(c + 1)
    if v == min(num):
        pos_min.append(c + 1)

print(f'Você digitou os seguintes números: {num}')

print(f'O maior valor digitado foi o {max(num)} e ele está na ', end='')
for i, j in enumerate(pos_max):
    print(f'{j}ª', end='')
    if i < len(pos_max) - 2:
        print(', ', end='')
    elif i == len(pos_max) - 2:
        print(' e ', end='')
if len(pos_max) == 1:
    print(' posição.')
else:
    print(' posições.')

print(f'O menor valor digitado foi o {min(num)} e ele está na ', end='')
for i, j in enumerate(pos_min):
    print(f'{j}ª', end='')
    if i < len(pos_min) - 2:
        print(', ', end='')
    elif i == len(pos_min) - 2:
        print(' e ', end='')
if len(pos_min) == 1:
    print(' posição.')
else:
    print(' posições.')
print('='*70)

