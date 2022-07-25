"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

num = list()
n = 0
c = 0
print('='*55)
while True:
    c += 1
    if n == 0 and c == 1:
        n = int(input('Digite um número: '))
    else:
        while num.count(n) > 0:
            n = int(input('Digite um número: '))
    num.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('='*55)
print(f'Os diferentes números em ordem crescente ficam assim: \n{sorted(num)}')
print('='*55)
print('FIM!')

print('')
print('Outro Aluno')

valores = []
while True:
    r = 0
    nvalor = int(input('Digite um valor: '))
    for c in range(0, len(valores)):
        if valores[c] == nvalor:
            print('Valor Duplicado! Não vou adicionar...')
            r = 1
            break
    if r == 0:
        valores.append(nvalor)
    cont = str(input('Quer continuar? [S/N] '))
    while cont not in 'SsNn':
        cont = str(input('Resposta não válida! Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores {valores}')

print(' ')
print('Outro Aluno')

list = []
while True:
    l = int(input('Digite um valor: '))
    if l not in list:
        list.append(l)
        print('Valor adicionado')
    else:
        print('Valor duplicado não é adicionado')
    answer = str(input('Deseja continuar a adiconar nº? [S/N]  ')) .strip() .upper()[0]
    while answer not in 'NS':
        answer = str(input('Digite [S/N]: ')) .strip() .upper()[0]
    if answer in 'N':
        break
list.sort()
print(f'Sua lista é {list}')

print(' ')
print('Outro Aluno')

nun = []
from time import sleep

while True:
    c = 0
    v = int(input(f'Digite um número: '))
    sleep(0.3)
    for posic, valor in enumerate(nun):
        if v in nun:
            c += 1
    if c == 0:
        valor = nun.append(v)
        print('Número adicionado com sucesso!')
        sleep(0.2)
    else:
        print('Número repetido... Não irei adicionar')
        sleep(0.2)
    r = str(input(f'Quer continuar? [S/N]: ')).capitalize()
    sleep(0.3)
    if r == 'S' or 'N':
        if r == 'N':
            break
    if r != 'S' or 'N':
        print('Opção invalida. Tente novamente...')
        sleep(0.3)
print('=-' * 20)
nun.sort()
print(f'A lista em ordem foi: {nun}')


print(' ')
print('Outro Aluno')

valores = list()
while True:
    num = input('Digite um número, ([S] p/ sair): ')
    if num.upper().split()[0] == 'S' and len(valores) == 0:
        break
    elif num.upper().split()[0] == 'S':
        valores.sort()
        print(f'A lista de valores digitados foi {valores}')
        break
    elif num.isalpha():
        print('Apenas números são permitidos ou a letra (S) para sair')
    elif int(num) not in valores:
        valores.append(int(num))
        print('Número adicionado a lista com sucesso')
    else:
        print('Impossível adicionar números repetidos')


print(' ')
print('Outro Aluno')
lista=[]
resposta=" "
while resposta in "S":
    num=int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Esse numero ja existe")
    resposta=str(input("Deseja continuar? [S/N]")).upper()
    if resposta == "N":
        break
print(sorted(lista))

print(' ')
print('Outro Aluno')

valor = list()
while True:
    valor.append(int(input('Adicione um valor: ')))
    if len(valor) > 1:
        if valor[-1] in valor[0:-1]:
            print('valor duplicado não inserido')
            valor.pop()
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if quest == 'N':
        break
print('=' * 30)
print(f'Você digitou os valores {sorted(valor)}')