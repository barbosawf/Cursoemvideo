# Desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
num = int(input('Digite um número inteiro: '))
rest = num % 2
if rest == 0:
    print('O número é par!')
else:
    print('O número é impar!')
