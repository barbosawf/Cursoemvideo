"""
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

condition = False
s = maior = menor = cont = 0


while not condition:
    n = int(input('Digite um número: '))
    cont += 1
    s += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    p = str(input('Deseja comtinuar? [SIM ou NÃO] ')).strip().upper()
    if p[0] == 'S':
        condition = False
    elif p[0] == 'N':
        condition = True


print('\n{} é o maior número.\n{} é o menor número'.format(maior, menor))
print('Você digitou {} números e a média de todos eles é {:.2f}.'.format(cont, s/cont))


print('')

from termcolor import colored
from time import sleep
print(colored('=', 'blue') * 57)
print(colored('Seja muito bem-vindo ao Py Number 0.4!', 'green'))
print(colored('=', 'blue') * 57)
sleep(0.5)
print(colored('Iniciando o programa...', 'magenta'))
sleep(1)
lista = []
contador = 0
total_de_números = 0
soma_dos_números = 0
while contador == 0:
    números = float(input(colored('Digite um número: ', 'yellow')))
    contador += 1
    total_de_números += 1
    soma_dos_números += números
    lista += [números]
    print(colored('=', 'blue') * 57)
    escolha = str(input(colored('Deseja continuar? [S/N]: ', 'yellow')).upper())
    print(colored('=', 'blue') * 57)
    if escolha != 'S' and escolha != 'N' :
        print(colored('Resposta inválida!', 'red'))
        contador = 0
        print(colored('=', 'blue') * 57)
        escolha = str(input(colored('Deseja continuar? [S/N]: ', 'yellow')).upper())
    elif escolha == 'S':
        contador = 0
    elif escolha == 'N':
        contador = -1
print(colored('Foram digitados cerca de {} números!'.format(total_de_números), 'green'))
print(colored('A soma entre estes valores é igual a {}! E a média é {:.2f}'.format(soma_dos_números,
                                                                                   soma_dos_números / total_de_números), 'green'))
print(colored('O maior valor foi {} e o menor valor foi {}'.format(max(lista), min(lista)), 'green'))
print(colored('=', 'blue') * 57)

print('')

_author_ = 'Fernando Cruz'
from time import sleep
d = '-=-' * 10
s = 0
c = 1
m = 0
menor = 0
maior = 0
media = 0
totFim = 0
fim = False
n = int(input('Digite um número [999 Para sair]: '))
while not fim:
    if n == 999:
        if c > 1:
            print('{}'.format(d))
            print('Foram digitados \033[1;32m{}\033[m valores'.format(c - 1))
            print('Soma: \033[1;32m{}\033[m'.format(totFim))
            print('Média: \033[1;32m{:.2f}\033[m'.format(media))
            print('Menor valor: \033[1;32m{}\033[m'.format(menor))
            print('Maior valor: \033[1;32m{}\033[m'.format(maior))
            print('{}'.format(d))
            n = int(input('Deseja realmente sair? [999 Para sair] Se não, digite outro número: '))
            if n == 999:
                fim = True
            else:
                totFim = totFim + n
        else:
            fim = True
    else:
        if c == 1:
            menor = n
            maior = n
        else:
            if menor > n:
                menor = n
            elif maior < n:
                maior = n
        s = s + n
        n = s
        m = n
        media = m / c
        c += 1
        totFim = n
        n = int(input('Deseja adicionar outro número? [999 Para sair]: '))
print('Finalizando programa', end='')
sleep(0.5)
print('\033[1;33m.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('')
print('\n*** Fim de execução ***\033[m')

print('')
parada = 'S'
while parada in 'Ss':
    n = int(input('Entre um número: '))
    somatoria += n
    acumulador += 1
    if acumulador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        else:
            maior = menor = n
    parada = str.strip(input('Continua, [s/n]? ')).upper()[0]
    if (parada not in 'SsNn'):
        while (parada not in 'SsNn'):
            parada = str.strip(input('Continua, [s/n]? ')).upper()[0]

media = somatoria/acumulador
print('A média dos {} números entrados é {}'.format(acumulador, media))
if maior != menor:
    print('O maior número é o {}, e o menor número é o {}.'.format(maior, menor))
else:
    print('Todos os números entrados são iguais!')
print('Fim!')

print('')

# Leia vários números. Perguntar se quer continuar digitando os números. A média. O maior e o menor.
n = soma = count = media = maior = menor = 0
r = ''
while n >= 0:
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    count += 1
    soma = soma + 1
    media = soma / count
    if r == 'N':
        print('Você digitou {} números. A média entre eles foi de {}.'.format(
            count, media))
    if n == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
            print('O maior número é o {}; e o menor número é o {}.'.format(maior, menor))

print('')
"""
from time import sleep

hora = int(input('HORA (Formato 12h): '))
min = int(input('MIN: '))
seg = int(input('SEG: '))
n = 0
horad = int(input('Digite um horário para o despertador: \n HORA (Formato 12h): '))
mind = int(input('MIN: '))
if hora < 12 and min < 60 and seg < 60:
    while n == 0:
        print('{:2}h : {:2}min : {:2}s'.format(hora, min, seg))
        sleep(1)
        seg+= 1
        if seg > 59:
            seg = 0
            min+= 1
        if min > 59:
            min = 0
            seg = 0
            hora+= 1
        if hora > 11:
            hora = 0
            seg  = 0
            min  = 0
        if hora == horad and min == mind:
            print('ALARME!!!!')
            horad=0
            mind=0
else:
    print('Valores digitados inválidos!')
    

"""