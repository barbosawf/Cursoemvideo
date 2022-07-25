print('Desafio 037')
"""
Escreva um programa que leia um número inteiro qualquer e peça 
para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

n = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases de conversão: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")

pgnt = int(input('DIGITE A OPÇÃO QUE DESEJA CONVERTER: '))
if pgnt == 1:
    print('{} convertido para Binário é {}.'.format(n, bin(n)[2:]))
elif pgnt == 2:
    print('{} convertido para Octal é {}.'.format(n, oct(n)[2:]))
elif pgnt == 3:
    print('{} convertido para Hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')

"""
numero_converter = int(input('Digite o número que deseja converter: '))
numero_antigo = numero_converter
base = int(input('Escolha qual a base de conversão você quer usar, 1 para binário, 2 para octal e 3 para hexadecimal: '))

if base == 1:
    numero_convertido = str(numero_converter % 2)
    numero_converter = int(numero_converter / 2)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 2) + numero_convertido
        numero_converter = int(numero_converter / 2)
    print(f'O número {numero_antigo} em binário é {numero_convertido}')
elif base == 2:
    numero_convertido = str(numero_converter % 8)
    numero_converter = int(numero_converter / 8)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 8) + numero_convertido
        numero_converter = int(numero_converter / 8)
    print(f'O número {numero_antigo} em octal é {numero_convertido}')


elif base == 3:
    numero_convertido = int(numero_converter % 16)
    if numero_convertido > 9:
        a = 1
        if numero_convertido == 10:
            numero_convertido = 'A'
        if numero_convertido == 11:
            numero_convertido = 'B'
        if numero_convertido == 12:
            numero_convertido = 'C'
        if numero_convertido == 13:
            numero_convertido = 'D'
        if numero_convertido == 14:
            numero_convertido = 'E'
        if numero_convertido == 15:
            numero_convertido = 'F'
    else:
        numero_convertido = str(numero_converter % 16)
    numero_converter = int(numero_converter / 16)
    while numero_converter > 0:
        numero_a_ser_adicionado = int(numero_converter % 16)
        if numero_a_ser_adicionado > 9:
            a = 1
            if numero_a_ser_adicionado == 10:
                numero_a_ser_adicionado = 'A'
            if numero_a_ser_adicionado == 11:
                numero_a_ser_adicionado = 'B'
            if numero_a_ser_adicionado == 12:
                numero_a_ser_adicionado = 'C'
            if numero_a_ser_adicionado == 13:
                numero_a_ser_adicionado = 'D'
            if numero_a_ser_adicionado == 14:
                numero_a_ser_adicionado = 'E'
            if numero_a_ser_adicionado == 15:
                numero_a_ser_adicionado = 'F'
        else:
            numero_a_ser_adicionado = str(numero_converter % 16)
        print(numero_a_ser_adicionado)
        numero_convertido = numero_a_ser_adicionado + numero_convertido
        numero_converter = int(numero_converter / 16)
    print(f'O número {numero_antigo} em hexadecimal é {numero_convertido}')
else:
print('Opção inválida')

"""