from random import sample
from time import sleep
sorteios = []
print('='*50)
print(f'{"JOGO DA MEGA SENA":^50}')
print('='*50)
n = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    jogo = sorted(sample(range(1, 61), 6))
    if jogo not in sorteios:
         sorteios.append(jogo)
print('='*50)
print(sorteios)
print(f'Os sorteios dos {n} jogos são os seguintes:')
for a, b in enumerate(sorteios):
    sleep(1)
    print(f'JOGO {a + 1}: {b}')
sleep(1)
print('='*50)

# Outro aluno

print(' ')
from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=-= SORTEANDO {quantidade_jogos} JOGOS =-=-=-=')
sleep(1)
for c in range(0, quantidade_jogos):
    jogo = []
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    sleep(1)
print('=-=-=-=-= < BOA SORTE! > =-=-=-=-=')
print(' ')
# outro aluno

from random import sample

q = int(input('Quantas apostas gerar? '))
nums = [sample(range(1,61), k=6) for x in range(0,q)]

for i in range(0,q):
    print(f'Aposta {i+1}: {sorted(nums)[i]}')

# outro aluno
print(' ')

from random import sample
from time import sleep
jogos=list()
n=int(input('Quantos jogos?: '))
for c in range(n):
    a=sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f'Jogo {c+1}: {a}')
    sleep(0.5)