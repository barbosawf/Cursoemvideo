"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

aluno = []
lista_alunos = []

print('='*51)
while True:
    resp1 = False
    while not resp1:
        nome = input('Nome do aluno: ').strip()
        resp1 = ''.join(nome.split()).isalpha()
    aluno.append(str(nome))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nota1)
    aluno.append(nota2)
    lista_alunos.append(aluno[:])
    aluno.clear()
    resp2 = ' '
    while resp2 not in 'SN':
        resp2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('='*51)
    if resp2 == 'N':
        break

print('No.   NOME                          MÉDIA')
print('-'*51)
for a, b in enumerate(lista_alunos):
    print(a, end='     ')
    print(f'{b[0]:<30}', end='')
    print(f'{((b[1] + b[2])/2):>5.2f}')
print('-'*51)

n_alunos = range(0, len(lista_alunos) + 1)

n = -1
while n not in [range(0, len(lista_alunos)), 999]:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n not in range(0, len(lista_alunos)) and n != 999:
        print(f'ATENÇÃO! Intervalo de cadastro de aluno: {[0,len(lista_alunos) - 1]}')
        print('-'*51)
    elif n in range(0, len(lista_alunos)):
        print(f'As notas de {lista_alunos[n][0]} são: {[lista_alunos[n][1], lista_alunos[n][2]]}')
        print('-'*51)
    if n == 999:
        break
print('-'*51)
# Melhoria
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        print('-'*51)
        break
    elif n in range(0, len(lista_alunos)):
        print(f'As notas de {lista_alunos[n][0]} são: {[lista_alunos[n][1], lista_alunos[n][2]]}')
        print('-'*51)
    elif len(lista_alunos) - 1 < n < 0:
        print(f'ATENÇÃO! Intervalo de cadastro de aluno: {[0,len(lista_alunos) - 1]}')
        print('-'*51)


print(' ')
print(' Outro Aluno:')
print(' ')

boletim = []
while True:
    n = str(input('Qual o nome do aluno? ')).strip().title()
    note = float(input('Qual a nota do aluno? '))
    note2 = float(input('Qual a segunda nota do aluno? '))
    média = (note + note2) / 2
    boletim.append([n, [note, note2], média])
    perg = str(input('Deseja resgistrar outro aluno? [S/N] ')).strip().upper()[0]
    if perg not in 'SN':
        print('\033[33mNão entendi...', end=' ')
        perg = str(input('\033[mResponda com [S/N]: ')).strip().upper()[0]
        if perg == 'N':
            break
    if perg == 'N':
        break
print('-=' * 5, 'BOLETIM', '=-' * 5)
print(f'{"Nº":<4}{"NOME ":<10}{"NOTA":>8}')
print('-' * 25)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8}')

while True:
    continuar = int(input('Digite o número do aluno para ver a nota (999 para parar): '))
    if continuar == 999:
        break
    if continuar <= len(boletim):
        print(f'As notas do aluno {boletim[continuar][0]} são {boletim[continuar][1]}')

print(' ')
print(' Outro Aluno:')
print(' ')

lista = []
cont = 0
while True:
    lista.append([])
    lista[cont].append(str(input('Digite o nome do aluno: ')))
    lista[cont].append(float(input('Digite a primeira nota: ')))
    lista[cont].append(float(input('Digite a segunda nota: ')))
    # Vou colocar a media na 4 posição (3)
    media = (lista[cont][1] + lista[cont][2]) / 2
    lista[cont].append(media)
    parar = str(input('Deseja continuar? [S/N] '))
    if parar in 'Nn':
        break
    cont += 1

print('x+'*30)
print('Nº Nome          Média')
print('-'*25)
for pos, alun in enumerate(lista):
    print(pos, f'{alun[0]:<15}', alun[3])

while True:
    print('-'*25)
    aluno = int(input('Deseja ver a nota de qual aluno? (999 para parar) '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1:3]}')
print('Programa Finalizado\nVolte sempre! :D')

print(' ')
print(' Outro Aluno:')
print(' ')


f=list()
g=list()
while True:
    n=str(input('digite um numero: '))
    n1=float(input('nota 1:  '))
    n2=float(input('nota 2:  '))
    media=(n1+n2)/2
    g.append([n,n1,n2])
    f.append([n,media])
    n3=str(input('quer continuar?  ')).strip()[0]
    while n3 not in 'SsNn':
        print('tente novamente')
        n3=str(input('quer continuar?  ')).strip()[0]
    if n3 in 'Nn' :
        break
print('numero   nome   media')
for i,j in enumerate(f):
    print('{}        {}      {}'.format(i,f[i][0],f[i][1]))
while True:
    n4=int(input('digite o numero do aluno(digite 999 para interromper): '))
    for c, k in enumerate(g):
        if c ==n4:
            print('{} com as notas [{},{}]'.format(g[c][0],g[c][1],g[c][2]))
    if n4==999:
        print('****finalizado****')
        break

print(' ')
print(' Outro Aluno:')
print(' ')

alunos = []
notas = -1
while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    alunos.append([nome, nota1, nota2])
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print('Nº.  NOME       MÉDIA')
print('-'*25)
for numero in range(0, len(alunos)):
    print(f'{numero}    {alunos[numero][0]:<13}{((alunos[numero][1] + alunos[numero][2])/2):.1f}')
print('-'*40)
while True:
    while notas not in range(0, len(alunos)) and notas != 999:
        notas = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if notas == 999:
        break
    else:
        print(f'Notas de {alunos[notas][0]} é {alunos[notas][1:]:}')
        print('-'*40)
        notas = -1
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')


print(' ')
print(' Outro Aluno:')
print(' ')

alunos = list()
dados = list()
while True:
    dados.append(str(input('Nome: ').capitalize().strip()))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    ask = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if ask in 'nN':
        break
a = 'NOME'
b = 'MÉDIA'
print('='*30)
print(f'N°{a:^20}{b:<20}')
print('-'*30)
for c,v in enumerate(alunos):
    print(f'{c}  {v[0]:^20}  {(v[1]+v[2])/2:<20}')
print('='*30)
while True:
    ask = int(input('Mostrar nota de qual aluno?[999 Encerra]: '))
    if ask == 999:
        break
    else:
        if ask >= len(alunos):
            print('Aluno não existe, digite um válido.')
        else:
            print(f'As notas de {alunos[ask][0]} são {alunos[ask][1]} e {alunos[ask][2]}')
print('<<= OBRIGADO VOLTE SEMPRE! =>>')

print(' ')
print(' Outro Aluno:')
print(' ')

main = []
name = []
grades = []
while True:
    name.append(input('Nome: '))
    grades.append(float(input('Nota 1: ')))
    grades.append(float(input('Nota 2: ')))
    name.append(grades[:])
    main.append(name[:])
    name.clear()
    grades.clear()
    ask = str(input('Quer continuar? [S/N] '))
    if ask in 'Nn':
        break
print('-'*42)
print(f'No. NOME      MÉDIA')
print('*'*20)
for i, v in enumerate(main):
    print(f'{i} {v[0]:>7} {(v[1][0] + v[1][1]) / 2:>8.1f}')
print('-'*42)
while True:
    ask_1 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ask_1 == 999:
        print('<< VOLTE SEMPRE :) >>')
        break
    for i in range(len(main)):
        print(f'Notas da {main[ask_1][0]} são {main[ask_1][1]}')
        break
    print('-'*42)