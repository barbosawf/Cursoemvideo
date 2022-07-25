"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
"""

"""
from time import sleep

cont = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            sleep(0.25)
            print(f'{c}', end=' ')
            cont = cont + 1
print('A soma dos {} valores ímpares e múltiplos de 3 entre 1 e 500 é {}.'.format(cont, t))
"""

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print('A soma dos {} valores ímpares e múltiplos de 3 entre 1 e 500 é {}.'.format(cont, soma))
