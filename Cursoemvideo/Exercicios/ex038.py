print('Desafio 038')
"""Escreva um programa que leia doi números inteiros e compareos,
mostrando na tela a mensagem:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais."""

n1 = 4.2
n2 = 5.4

while n1 != int(n1):
    print('')
    n1 = float(input('Digite um número inteiro: '))
    if n1 != int(n1):
        print('Digite apenas números inteiros, por favor!')

while n2 != int(n2):
    print('')
    n1 = float(input('Digite outro número inteiro: '))
    if n2 != int(n2):
        print('Digite apenas números inteiros, por favor!')

print('')
if n1 > n2:
    print('O primeiro valor é o maior: {} > {}'.format(int(n1), int(n2)))
elif n2 > n1:
    print('O segundo valor é o maior: {} < {}'.format(int(n1), int(n2)))
else:
    print('Os valores são iguais: {} = {}'. format(int(n1), int(n2)))
