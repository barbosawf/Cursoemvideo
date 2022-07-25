# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar decobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
np = randint(0, 5)
nd = int(input('Digite um número inteiro entre 0 e 5: '))
if nd == np:
    print('Você acertou o número pensado pelo computador!')
else:
    print('Você errou o número pensado pelo computador!')
