"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]

print('='*50)
for a in range(0, 3):
    for b in range(0, 3):
        n = int(input(f'Digite um valor para {[a, b]}: '))
        if a == 0:
            linha0[b].append(n)
        if a == 1:
            linha1[b].append(n)
        if a == 2:
            linha2[b].append(n)

print('='*50)
print(linha0)
print(linha1)
print(linha2)
print('='*50)

print(' ')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print('='*50)

s =