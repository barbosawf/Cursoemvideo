"""
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\33[0;31mERRO! Por favor, digite um número inteiro.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[0;33mEntrada de dados interrompida pelo usuário.\33[m')
            return 'NENHUM'
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\33[0;31mERRO! Por favor, digite um número inteiro.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[0;33mEntrada de dados interrompida pelo usuário.\33[m')
            return 'NENHUM'
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'\nO número inteiro digitado foi {n1}.')
print(f'O número real digitado foi {n2}.')
