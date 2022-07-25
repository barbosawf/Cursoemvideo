"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

print('=' * 50)
print(f'{"JOGO DE DADOS":^50}')
print('=' * 50)

dicionario = {}
for c in range(1, 5):
    dicionario[f'Jogador {c}'] = randint(1, 6)

for k, v in dicionario.items():
    print(f'O {k} obteve o valor {v}.')
    sleep(1)

print('=' * 50)
print()
print('=' * 50)
print(f'{"RANKING DOS JOGADORES:":^50}')
print('=' * 50)

ranking = list()
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print('=' * 50)


from random import randint
from time import sleep
resutados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = randint(1, 6)
    resutados['Jogador'+str(c+1)] = n
    jogadores.append(n)
    sleep(0.5)
    print(f'O {"Jogador"+str(c+1)} tirou {n}')
jogadores.sort(reverse= True)
jogar = 't'
print('Ranking dos jogadores:')
for p in range(0,4):
    print(f'{p+1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.1)
            print(k,'com',v)
            jogar = k
            break

# outro aluno
import time,random
data = {}
for c in range (0,4):
    player_id = "player "+str(c+1)
    data[player_id] = random.randint(1,6)
    time.sleep(.5)
    print(f'The {player_id} has {data[player_id]}')
n = 1
for c in range(0,7):
    for p,v in data.items():
        if v == (6 - c):
            time.sleep(.5)
            print(f"The {n}º position is the {p} with {v}")
            n += 1


#Outro aluno
# import operator
jogador = 1
Dict = {}
quantidade_de_jogadores = 4
for c in range(quantidade_de_jogadores):
    Dict['Jogador' + str(jogador)] = randint(1, 7)
    jogador += 1
lista = list(Dict.copy().items())
# print(sorted(lista, key=operator.itemgetter(1)))
ordem = sorted(lista, key=lambda a: a[1], reverse=True)
print('Valores sorteados: ')
for c in lista:
    print(f'    O {c[0]} tirou {c[1]}')
    sleep(1)
print('Ranking dos Jogadores: ')
for v, c in enumerate(ordem):
    print(f'    Em {v+1}° lugar: {c[0]} com {c[1]}')
    sleep(1)

#

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for j in range(0, 4):
    jogadores[f'Jogador {j+1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('='*30)
print('          ==RANKING==')
contador = 1
for x in range(0, len(ranking)):
    if x == 0:
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')
    elif ranking[x][1] == ranking[x - 1][1]:
        print(f'       {ranking[x][0]} com {ranking[x][1]} pontos.')
    else:
        contador += 1
        print(f'  {contador}º - {ranking[x][0]} com {ranking[x][1]} pontos.')

# Outro aluno

# código que faz os jogadores "jogar o dado"
jogadores = dict()
for c in range(1, int(input('quantos jogadores participarão? ')) + 1):
    jogadores[c] = randint(1, 6)
    print(f'o jogador {c} tirou {jogadores[c]} no dado')
    sleep(0.75)

# código que pega a variável Jogadores e coloca na variável Ranking ordenado em ordem decrescente
ranking = {}
while len(jogadores) > 0:
    maior = [0, 0]
    for chave, valor in jogadores.items():
        if valor > maior[1]:
            maior = [chave, valor]
    ranking[maior[0]] = maior[1]
    del jogadores[maior[0]]

# código que coloca os jogadores que tiraram a mesma coisa no dado na mesma posição do Ranking
aparecido = list()
for chave, item in ranking.items():
    novo = True
    for item2 in range(0, len(aparecido)):
        if item == aparecido[item2][0]:
            novo = False
            aparecido[item2][1].replace(' e',',')
            aparecido[item2][1] += f' e {chave}'
            break
    if novo:
        aparecido.append([item, str(chave)])

# código que transcreve oque temna variável Aparecido para a variável Ranking
ranking = dict()
for item3 in aparecido:
    ranking[item3[1]] = item3[0]

#código que mostra o Ranking
print('Ranking: ')
posicao = 1
for chave, valor in ranking.items():
    sleep(0.75)
    print(f'{posicao}º lugar: {chave}: {valor} pontos')

#sort_orders = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

jogadores = {input(f'\nNome do jogador {i}: ').capitalize(): randint(1, 6) for i in range(1, 5)}

for k, v in jogadores.items():
    sleep(1), print(f'\n{k} tirou {v}.'), sleep(1)

ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

print(), print('-' * 32)
print(f'| {"Ranking dos jogadores":^28} |')
print('-' * 32)
print(f'| Posição |  Jogador  | Pontos |')
print('-' * 32)
posicao = 1
for num in range(len(ranking)):
    if num == 0 or ranking[num][1] == ranking[num - 1][1]:
        print(f'| {str(posicao) + "º":^7} | {ranking[num][0]:^9} | {ranking[num][1]:^6} |')
    else:
        posicao += 1
        print(f'| {str(posicao) + "º":^7} | {ranking[num][0]:^9} | {ranking[num][1]:^6} |')
print('-' * 32)
""" 
ordem = {}
max_v = min_v = 0
#ERRADO por quando sai o valor menor e o maior não dá.
for c in range(1, len(dicionario) + 1):
    if c == 1:
        ordem[f'Jogador {c}'] = dicionario[f'Jogador {c}']
        max_v = dicionario[f'Jogador {c}']
        min_v = dicionario[f'Jogador {c}']
    if dicionario[f'Jogador {c}'] >= max_v:
        max_v = dicionario[f'Jogador {c}']
        ordem[f'Jogador {c}'] = dicionario[f'Jogador {c}']
    if dicionario[f'Jogador {c}'] <= min_v:
        min_v = dicionario[f'Jogador {c}']
        provisorio = ordem
        ordem = dict()
        ordem[f'Jogador {c}'] = dicionario[f'Jogador {c}']
        for k, v in provisorio.items():
            ordem[k] = v

print(ordem)
"""

