"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para {[l, c]}: '))
        matriz[l][c] = n
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print('='*50)

s1 = 0
s2 = 0

for a, l in enumerate(matriz):
    for b, c in enumerate(l):
        if c % 2 == 0:
            s1 += c
        if b == 2:
            s2 += c
        if a == 1:
            max_l = max(l)

print(f'A soma de todos os valores pares digitados é {s1}.')
print(f'A soma dos valores da terceira coluna é {s2}.')
print(f'O maior valor da segunda linha é: {max_l}.')
print('='*50)

# outro aluno

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Informe o valor [{c, l}]: ')))
        matriz[l][c] = num
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    soma = soma + matriz[l][2]
    print()
maior = max(matriz[1][0], matriz[1][1], matriz[1][2])
print('=' * 30)
print(f'A soma dos valores pares vale {pares}')
print(f'A soma dos valores da 3ª coluna vale {soma}')
print(f'O maior valor da 2ª coluna vale {maior}')


# Outro aluno

matriz = [[], [], []]
somaPares = 0
somaColuna2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor do elemento [{i},{j}]: '))
        matriz[i].append(n)
        if n % 2 == 0:
            somaPares += n
        if j == 2:
            somaColuna2 += n
        if i == 1:
            if j == 0:
                maior2 = n
            else:
                if n > maior2:
                    maior2 = n
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^6}]',end='')
    print()
print(f'A soma dos pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaColuna2}')
print(f'O maior valor da segunda linha é: {maior2}')


# Outro aluno

L = [int(input(f'Digite o número {x}: ')) for x in range(1, 10)]

print('='*52)
print(f'{L[0]:^15} | {L[1]:^15} | {L[2]:^15}')
print('-'*52)
print(f'{L[3]:^15} | {L[4]:^15} | {L[5]:^15}')
print('-'*52)
print(f'{L[6]:^15} | {L[7]:^15} | {L[8]:^15}')
print('='*52)

print(f'SOMA TERCEIRA COLUNA: {L[2]+L[5]+L[8]:.>22}')
print(f'\nSOMA TOTAL: {sum(L)}'
      f'\nSOMA PARES: {sum([x for x in L if x % 2 ==0])}'
      f'\nMAIOR VALOR LINHA 2: {max([L[3], L[4], L[5]])}'