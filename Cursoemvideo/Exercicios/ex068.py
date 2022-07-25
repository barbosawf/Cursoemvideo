"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

'''
c = 0
from random import randint
print("Jogo do Par ou Ímpar! Let's play!")
while True:
    print('=' * 40)
    escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    player = int(input('Digite um número inteiro entre 0 e 10: '))
    comp = randint(0, 10)
    s = player + comp
    if escolha == 'P':
        print(f'\nEscolha do COMPUTADOR: {comp}.')
        if s % 2 == 0:
            print(f'A soma entre {player} e {comp} é {s}, portanto, PAR!')
            print('VOCÊ GANHOU!')
            c += 1
        else:
            print(f'A soma entre {player} e {comp} é {s}, portanto, ÍMPAR!')
            print('VOCÊ PERDEU!')
            break
    elif escolha in 'ÍI':
        print(f'Escolha do COMPUTADOR: {comp}.')
        if s % 2 > 0:
            print(f'A soma entre {player} e {comp} é {s}, portanto, ÍMPAR!')
            print('VOCÊ GANHOU!')
            c += 1
        else:
            print(f'A soma entre {player} e {comp} é {s}, portanto, PAR!')
            print('VOCÊ PERDEU!')
            break
print('=' * 30)
print(f'Você ganhou {c} vezes até perder.')
'''

"""
c = 0
from random import randint
print("Jogo do Par ou Ímpar! Let's play!")
while True:
    print('=' * 40)
    escolha = ' '
    while escolha not in 'PIÍ':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if escolha not in 'PIÍ':
            print('Digite corretamente, por favor!')
    player = -3.2
    while player % 1 != 0 or 10 < player < 0:
        player = float(input('Digite um número inteiro entre 0 e 10: '))
        if player % 1 != 0 or 0 <= player <= 10:
            player = -3.2
            print('Você digitou um número fora do intervalo ou não inteiro.')
            print('Digite corretamente, por favor!')
    player = int(player)
    comp = randint(0, 10)
    s = player + comp
    if escolha == 'P':
        print(f'\nEscolha do COMPUTADOR: {comp}.')
        if s % 2 == 0:
            print(f'A soma entre {player} e {comp} é {s}, portanto, PAR!')
            print('VOCÊ GANHOU!')
            c += 1
        else:
            print(f'A soma entre {player} e {comp} é {s}, portanto, ÍMPAR!')
            print('VOCÊ PERDEU!')
            break
    elif escolha in 'ÍI':
        print(f'Escolha do COMPUTADOR: {comp}.')
        if s % 2 > 0:
            print(f'A soma entre {player} e {comp} é {s}, portanto, ÍMPAR!')
            print('VOCÊ GANHOU!')
            c += 1
        else:
            print(f'A soma entre {player} e {comp} é {s}, portanto, PAR!')
            print('VOCÊ PERDEU!')
            break
print('=' * 30)
print(f'Você ganhou {c} vezes até perder.')
"""
v = 0
from random import randint
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIpi':
        tipo = str(input('Par ou Ímpar? [P|I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total foi {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-'*25)
print(f'GAME OVER! Você venceu {v} vezes.')


