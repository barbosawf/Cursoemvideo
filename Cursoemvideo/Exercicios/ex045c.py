from termcolor import colored
from time import sleep
import random
print(colored('-=-', 'blue') * 17)
print(colored("""Seja muito bem-vindo \033[4;33m\033[1;33mPy Rock Paper Scissors 0.1!\033[0;32m
Com este código, você será capaz de jogar o famoso 
jokenpô com o nosso querido computador!""", 'green'))
print(colored('-=-', 'blue') * 17)
print(colored("""\033[4;32m\033[1;32mRegras do Jokenpô:\033[0;32m
Pedra - Ganha da Tesoura e perde para o Papel
Papel - Ganha da Pedra e perde para a Tesoura
Tesoura - Ganha do Papel e perde para a Pedra""", 'green'))
print(colored('-=-', 'blue') * 17)
print(colored('Sair - Termina de executar o código', 'green'))
print(colored('-=-', 'blue') * 17)
lista = ['Pedra', 'Papel', 'Tesoura']
escolhas = random.choice(lista)
escolha = str(input(colored('Deseja escolher o que? ', 'yellow')).title().strip())
sleep(1)
if escolhas == 'Pedra' and escolha == 'Papel':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Parabéns! Você venceu!', 'green'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == 'Pedra' and escolha == 'Tesoura':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Que pena! Você perdeu!', 'red'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == 'Papel' and escolha == 'Tesoura':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Parabéns! Você venceu!', 'green'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == 'Papel' and escolha == 'Pedra':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Que pena! Você perdeu!', 'red'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == 'Tesoura' and escolha == 'Pedra':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Parabéns! Você venceu!', 'green'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == 'Tesoura' and escolha == 'Papel':
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Que pena! Você perdeu!', 'red'))
    print(colored('-=-', 'blue') * 17)
elif escolhas == escolha:
    print(colored('Verificando os resultados...', 'magenta'))
    sleep(2)
    print(colored('-=-', 'blue') * 17)
    print(colored('O computador escolheu \033[1;33m{}!'.format(escolhas), 'yellow'))
    print(colored('E você escolheu \033[1;33m{}!'.format(escolha), 'yellow'))
    print(colored('Empate! Ambos escolheram a mesma opção!', 'yellow'))
    print(colored('-=-', 'blue') * 17)
elif escolha == 'Sair':
    print(colored('Saindo...', 'magenta'))
    sleep(2)
    exit()
elif escolha != 'Papel' or 'Pedra' or 'Tesoura':
    print(colored('-=-', 'blue') * 17)
    print(colored("""Essa opção é inválida! Por favor, reinicie
o código e tente novamente!""", 'red'))
    print(colored('-=-', 'blue') * 17)
