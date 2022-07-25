"""
Soma dos números digitados que forem pares.
"""

print('Desafio 050')
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n

print('A soma de todos os números pares digitados é {}.'.format(soma))
