"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
rand = randint(0, 10)
n = rand + 1
tentativas = 1

while rand != n:
    n = int(input('Digite um número inteiro: '))
    if n != rand:
        tentativas += 1
    else:
        print('\nVocê acertou o número que pensei. PARABÉNS!')
print(f'Você tentou {tentativas}x até acertar que pensei no número {rand}!')


####### Outro Aluno #######
from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites))

print('')

###### Outro Aluno ########
from time import sleep
from random import randint
print("Olá, eu sou seu computador")
sleep(1.25)
print("Por acaso eu tenho um nome?")
sleep(1.5)
print("Poderia dizer meu nome?")
sleep(1.25)
pc = str(input("Digite o nome do seu computador: ")).strip()
print(f"Ah então meu nome é {pc}?")
sleep(1.5)
print("Okay então... Você quer brincar comigo?")
sleep(1.4)
op = str(input("[S/N]")).strip().upper()
while op != "S/N":
    if op == "S":
        sleep(0.75)
        print("Okay, então vamos brincar! (^-^) ")
        sleep(0.5)
        print("Então vamos pro jogo:")
        sleep(0.25)
        print("ele é simples. \n")
        sleep(0.25)
        print("Vou pensar em um número de 0 à 10. \n")
        sleep(0.25)
        print("E você vai tentar advinhar!")
        sleep(0.25)
        print("Então vamos nessa!")
        sleep(0.25)
        comp = randint(0, 10)
        acertou = False
        palpites = 0
        while not acertou:
            jogador = int(input("Qual é o seu palpite? "))
            palpites += 1
            if jogador == comp:
                acertou = True
            else:
                if jogador < comp:
                    print("Você errou... mas você ainda pode continuar tentando \n"
                          "Vou te dar uma dica é um pouco maior que o número que você escolheu \n")
                elif jogador > comp:
                    print("Você errou... mas você ainda pode continuar tentando \n"
                          "Vou te dar uma dica é um pouco menor que o número que você escolheu \n")
        print("Aeeee você ganhou meus parabéns!\n"
              f"Depois de {palpites} tentativas, você me venceu kkkkkk")
        break
    elif op == "N":
        print("Que pena! (T-T) ")
        break
    else:
        print("Eu não entendi, poderia digitar novamente?")
        op = str(input("[S/N]")).strip().upper()
print('')

#####
from random import randint, choice
nome = ''
tentativa = 0
computador = randint(1, 10)
nJogador = str(input('Digite o seu nome: ')).strip()
jogador = int(input('Pensei em um número de 1 a 10, tente adivinhar\n: '))
if jogador < computador:
    print('É mais')
    tentativa += 1
elif jogador > computador:
    print('É menos!')
    tentativa += 1
while jogador != computador:
    tentativa += 1
    jogador = int(input())
    if jogador < computador:
        print('É mais!')
    elif jogador > computador:
        print('É menos!')
print('-='*20)
print('Parabéns {}, você adivinhou!\nTentativas {}'.format(nJogador, tentativa))
print('-='*20)
