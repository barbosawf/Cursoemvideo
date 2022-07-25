"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
# cores: https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
print('Desafio 047')

for c in range(0, 51, 2):
    if c > 0:
        print(c, end=' ')
print('ACABOU!\n')

for c in range(2, 51, 2):
    print(c, end=' ')
print('ACABOU!\n')

for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('ACABOU!\n')