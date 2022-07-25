# Desafio 035
# Desenvolva um programa que leia o comprimento de três retas
# e diga se elas podem ou não formar um triângulo.
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

if abs(b - c) < a < (b + c):
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')

