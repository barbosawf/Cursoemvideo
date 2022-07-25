"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
"""

soma = 0
maior = 0
hvelho = str('')
contf = 0
cont = 0
for c in range(1, 5):
    print(f'====== {c}ª PESSOA ======')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    print('')
    soma += idade
    if sexo in 'mM':
        cont += 1
    if cont == 1 and sexo in 'mM':
        maior = idade
        hvelho = nome
    if idade > maior and sexo in 'mM':
        maior = idade
        hvelho = nome
    if idade < 20 and sexo in 'fF':
        contf += 1

print('A média de idade do grupo é {:.2f}.'.format(soma/c))
print('O homem mais velho se chama {} e tem {} anos de idade.'.format(hvelho, maior))
print('{} mulhere(s) têm menos de 20 anos.'.format(contf))
print('')

# Outro Aluno:
mediaIdade = 0
nomeMaisVelho = str('')
maiorIdade = 0
Count_Mulher_Menor_20 = 0
Count_Mulher = 0
Count_Homem = 0


for p in range(1, 5):
    print(f'=== {p}° PESSOA ===')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M or F): ')).upper().strip()
    mediaIdade = ((mediaIdade + idade)/p)
    if p == 1 and sexo == "M":
        maiorIdade = idade
        nomeMaisVelho = nome
        Count_Homem += 1
    if sexo == "M" and maiorIdade < idade:
        maiorIdade = idade
        nomeMaisVelho = nome
        Count_Homem += 1
    else:
        if sexo == "F":
            Count_Mulher += 1
            if idade < 20:
                Count_Mulher_Menor_20 += 1

print('A média da idade do grupo é: {:.2f}'.format(mediaIdade))

if Count_Homem > 0:
    print(f'O homem de maior idade é o {nomeMaisVelho} e sua idade é {maiorIdade}')
else:
    print('Não há homens no grupo!')

if Count_Mulher > 0:
    print(f'Ao todo são {Count_Mulher_Menor_20} mulheres com menos de 20 anos.')
else:
    print('Não há mulheres no grupo!')


"""
###### Outro Aluno #####

import datetime
ano = datetime.date.today().year
#m == média

m = 0
#maiorh == maior homem (idade do maior homem)

maiorh = 0
#nmh == nome do homem (mais velho)

nmh = None
#mcm20a == mulheres com menos de 20 anos (abreviação como os anteriores)

mcm20a = 0
for a in range(1, 5):
    n = str(input('Qual o nome da {}ª pessoa? : '.format(a)))
    i = int(input('Qual a idade da {}ª pessoa? : '.format(a)))
    s = int(input('1 -> feminino\n2 -> masculino\nQual o sexo da {}ª pessoa? : '.format(a)))
    m = m + i
    if s == 2:
        if a == 1:
            maiorh = i
            nmh = n
        if i > maiorh:
            maiorh = i
            nmh = n
    if s == 1:
        if i < 20:
            mcm20a = mcm20a + 1
print(('A média de idade dessas pessoas é de {} anos').format(m / 4))
print('O nome do homem mais velho é {}'.format(nmh))
#para ficar mais bonito elaborei melhor essa parte
if mcm20a > 1 or mcm20a == 0:
    print('{} mulheres tem menos de 20 anos'.format(mcm20a))
elif mcm20a == 1:
    print('{} mulher tem menos de 20 anos'.format(mcm20a))

print('')

homemmaisvelho = ''
idadehomemmaisvelho = 0
mulheressub20 = []

for pessoa in range(1, 5):
    print('-'*5, f'{pessoa}ª PESSOA', '-'*5)
    nome = str(input(f'Nome: ')).strip()
    idade = int(input('Idade? '))
    sexo = str(input('Sexo [M/F]:')).strip()
    if sexo == 'm' or 'M':
        if pessoa == 1 and sexo in 'Mm':  ########Aqui tive que inserir o "and sexo in 'mM'
            homemmaisvelho = nome
            idadehomemmaisvelho = idade
        else:
            if idade > idadehomemmaisvelho and sexo in 'Mm':
                idadehomemmaisvelho = idade
                homemmaisvelho = nome
    elif sexo == "f" or 'F':
        if idade < 20:
            mulheressub20 = [idade]

    media += [idade]

print(f'\nO homem mais velho do grupo é o {homemmaisvelho} e tem {idadehomemmaisvelho} anos.')
print(f'A média de idade do grupo é {sum(media)/4} anos.')
print(f'{len(mulheressub20)} mulher(es) possuem menos de 20 anos.')

"""