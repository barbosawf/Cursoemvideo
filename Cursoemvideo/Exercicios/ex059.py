"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
c = 'Continua'
op = 6

while c != 'Pare':
    print('')
    op = int(input("""Digite uma das opções a seguir:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    """))
    if 0 < op <= 5:
        c = 'Continua'
        if op == 1:
            print('A soma é: {:.2f}'.format(n1 + n2))
        elif op == 2:
            print('A multiplicação é {:.2f}.'.format(n1 * n2))
        elif op == 3:
            if n1 > n2:
                print(f'{n1} é maior.')
            elif n2 > n1:
                print(f'{n2} é maior:')
            else:
                print('Os números são iguais:')
        elif op == 4:
            n1 = float(input('Digite novamente um 1º número: '))
            n2 = float(input('Digite novamente um 2º número: '))
        elif op == 5:
            c = 'Pare'
    else:
        c = 'Continua'
        print(f'{op} não é uma das opções.')

print('ACABOU!')
print('')

# Outro Aluno
# Outro Aluno



from termcolor import colored
from time import sleep
print(colored('=', 'blue') * 55)
print(colored('Seja muito bem-vindo ao Py Math 1.0!', 'green'))
print(colored('=', 'blue') * 55)
sleep(0.5)
print(colored('Iniciando o programa...', 'magenta'))
sleep(1)
print(colored('=', 'blue') * 55)
print(colored("""Digite 1 - Para somar os números!
Digite 2 - Para multiplicar os números!
Digite 3 - Para ver qual é o maior número!
Digite 4 - Para digitar novos números!
Digite 5 - Para poder sair do programa!""", 'green'))
print(colored('=', 'blue') * 55)
primeiro_número = int(input(colored('Digite o primeiro valor: ', 'yellow')))
segundo_número = int(input(colored('Digite o segundo valor: ', 'yellow')))
print(colored('=', 'blue') * 55)
sleep(0.5)
escolha_da_opção = 0
while escolha_da_opção != 5:
    escolha_da_opção = int(input(colored('Informe a opção desejada: ', 'yellow')))
    if escolha_da_opção == 1:
        print(colored('Calculando...', 'magenta'))
        sleep(1)
        print(colored('=', 'blue') * 55)
        print(colored("""{} + {} = {}!""".format(primeiro_número, segundo_número,
                                                 primeiro_número + segundo_número), 'green'))
        print(colored('=', 'blue') * 55)
    elif escolha_da_opção == 2:
        print(colored('Calculando...' , 'magenta'))
        sleep(1)
        print(colored('=', 'blue') * 55)
        print(colored("""{} x {} = {}!""".format(primeiro_número, segundo_número,
                                                 primeiro_número * segundo_número), 'green'))
        print(colored('=', 'blue') * 55)
    elif escolha_da_opção == 3:
        if primeiro_número > segundo_número:
            print(colored('Verificando...', 'magenta'))
            sleep(1)
            print(colored('=', 'blue') * 55)
            print(colored("""O maior valor é {}!""".format(primeiro_número), 'green'))
            print(colored('=', 'blue') * 55)
        elif segundo_número > primeiro_número:
            print(colored('Verificando...', 'magenta'))
            sleep(1)
            print(colored('=', 'blue') * 55)
            print(colored("""O maior valor {}!""".format(segundo_número), 'green'))
            print(colored('=', 'blue') * 55)
        elif primeiro_número == segundo_número:
            print(colored('Verificando...', 'magenta'))
            sleep(1)
            print(colored('=', 'blue') * 55)
            print(colored("""Ambos os valores são iguais!""", 'green'))
            print(colored('=', 'blue') * 55)
    elif escolha_da_opção == 4:
        print(colored('=', 'blue') * 55)
        primeiro_número = int(input(colored('Digite o primeiro valor: ', 'yellow')))
        segundo_número = int(input(colored('Digite o segundo valor: ', 'yellow')))
        print(colored('=', 'blue') * 55)
    elif escolha_da_opção == 5:
        print(colored('=', 'blue') * 55)
        print(colored('Saindo do programa...', 'magenta'))
        sleep(1)
        print(colored('Você saiu do programa!', 'red'))
        print(colored('=', 'blue') * 55)
    elif escolha_da_opção > 5:
        print(colored('=', 'blue') * 55)
        print(colored('Opção inválida! Tente novamente!', 'red'))
        print(colored('=', 'blue') * 55)
        sleep(0.5)

### Outro Aluno
valor1 = float(input('Digite o 1 valor: '))
valor2 = float(input('Digite o 2 valor: '))
finalizar = False
while not finalizar:
    menu = int(input('''Agora, insira o número que corresponde ao que você quer fazer com seus valores
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA:    '''))
    soma = valor1 + valor2
    mult = valor1 * valor2
    maiorvalor = ''
    if menu == 1:
        print('A soma dos valores é de {}.'.format(soma))
    if menu == 2:
        print('A multiplicação entre os valores é de {}.'.format(mult))
    if menu == 3:
        if valor1 > valor2:
            maiorvalor = valor1
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if valor2 > valor1:
            maiorvalor = valor2
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if valor2 == valor1:
            print('Os dois valores são iguais!')
    if menu == 4:
        print('Seu desejo é uma ordem!')
        valor1 = int(input('Insira o novo 1 valor: '))
        valor2 = int(input('Insira o novo 2 valor: '))
    if menu == 5:
        print('Entendido, estamos finalizando o programa! Tchauzinho! :)')
        finalizar = True
    print('-='*10)

print('')



### Outro Aluno

import os

from time import sleep
maior = 0
continuar = False
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while not continuar:
    print('''
[0] Limpar Tela
[1] SOMA 
[2] Multiplicar 
[3] MAIOR NÚMERO 
[4] NOVOS NÚMEROS 
[5] Sair do programa''')
    print(7 * '=-=')
    menu = input('Qual dessas opções? ')
    if menu == '0':
        os.system("cls")
    if menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5':
        print('Opção inválida, Tente novamente')
    if menu == '5':
        print('Saindo...')
        sleep(1)
        continuar = True
    else:
        if menu == '1':
            r = n1 + n2
            print(7 * '=-=')
            print(f'SOMA : {n1} + {n2} = {r}')
            print(7 * '=-=')
        elif menu == '2':
            r = n1 * n2
            print(7 * '=-=')
            print(f'MULTIPLICAÇÃO: {n1} x {n2} = {r}')
            print(7 * '=-=')
        elif menu == '3' and n1 > n2:
            maior = n1
            print(7 * '=-=')
            print(f'O Maior número é {maior}')
            print(7 * '=-=')
        elif menu == '3' and n2 > n1:
            maior = n2
            print(7 * '=-=')
            print(f'O MAIOR número é {maior}')
            print(7 * '=-=')
        elif menu == '4':
            print(7 * '=-=')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
            print(7 * '=-=')

print(7 * '=-=')
print('  Fim do programa!')
print(7 * '=-=')

print('')

# Outro aluno

n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
menu = 0
while menu != 5:
    print('escolha uma opção no menu')
    menu = int(input(('''
    1: para soma
    2: para multiplicar
    3: para ver qual e o maior
    4: para escolher novos numeros
    5: para sair do programa
    digite aqui: ''')))
    if menu == 1:
        soma = n1 + n2
        print('a soma entre {} e {} e de {}'.format(n1, n2, soma))
    if menu == 2:
        multi = n1 * n2
        print('o numero {} multiplicado por {} e {}'.format(n1, n2, multi))
    if menu == 3:
        if n1 > n2:
            print('o numero {} e o maior'.format(n1))
        if n2 > n1:
            print('o numero {} e maior'.format(n2))
    if menu == 4:
        n1 = int(input('digite um novo numero'))
        n2 = int(input('digite mais um novo numero'))
    elif menu == 5:
        print('programa filalizado')
    else:
        print('opção invalida')
print('fim do programa')

print('')

# Outro Aluno

n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))
opcao = 0
parar = False
while not parar:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior valor\n[4]Novos numeros\n[5]Sair')
    opcao = int(input('>>>>>>Qual sua opçao ? '))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
        print('=-='*10)
    if opcao == 2:
        mult = n1*n2
        print('A multiplicaçao de {} e {} é igual a {}'.format(n1, n2, mult))
        print('=-=' * 10)
    if opcao == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor é {maior}')
        print('=-=' * 10)
    if opcao == 4:
        n1 = int(input('Primeiro valor : '))
        n2 = int(input('Segundo valor : '))
        print('=-=' * 10)
    if opcao == 5:
        parar = True
        print('=-=' * 10)
        print('EXIT')

print('')

# Outro Aluno
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('Escolha uma opção:'
          '\n[ 1 ] Somar'
          '\n[ 2 ] Multiplicar'
          '\n[ 3 ] Maior'
          '\n[ 4 ] Novos números'
          '\n[ 5 ] Sair do programa')
    opção = int(input('=========> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 - int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando',end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
print('')

