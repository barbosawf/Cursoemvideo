"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print(50*'=')
print('{:^50}'.format("Banco CEV"))
print(50*'=')

valor = int(input('Qual o valor você quer sacar? R$ '))
total = valor
cedula = 50
totcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas > 0:
            print('Total de {} cédulas de R$ {:.2f}.'.format(totcedulas, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedulas = 0
        if total == 0:
            break
print(50*'=')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')