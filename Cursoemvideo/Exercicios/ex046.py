"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep

b = {'preto': '\033[40m',
     'vermelho': '\033[41m',
     'verde': '\033[42m',
     'amarelo': '\033[43m',
     'azul': '\033[44m',
     'lilas': '\033[45m',
     'cyan': '\033[46m',
     'cinza': '\033[47m',
     'branco': '\033[97m',
     'vermelho_claro': '\033[101m',
     'verde_claro': '\033[102m',
     'amarelo_claro' :'\033[103m',
     'azul_claro': '\033[104m',
     'magenta_claro': '\033[102m'
     }

print(f'{b["preto"]}Desafio 046\n')
"""
cor = ['\033[41m', '\033[42m', '\033[43m',
       '\033[44m', '\033[45m', '\033[46m', '\033[47m',
       '\033[97m', '\033[101m', '\033[103m',
       '\033[104m', '\033[102m', '\033[m']

cont = 10
for c in range(0, 11):
    print('{}{}{}'.format(cor[cont], cont, cor[12]))
    cont = cont - 1
    sleep(1)
print("{}BOOM!{}".format(cor[11], cor[12]))


print('')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("{}BOOM! BOOM! BOOM!{}".format(cor[5], cor[12]))
"""


cor = {'Preto': '\033[40m',
'Vermelho': '\033[41m',
'Verde': '\033[42m',
'Amarelo': '\033[43m',
'Azul': '\033[44m',
'Magenta': '\033[45m',
'Cyan': '\033[46m',
'Cinza_Claro': '\033[47m',
'Cinza_Escuro':	'\033[100m',
'Vermelho_Claro': '\033[101m',
'Verde_Claro': '\033[102m',
'Amarelo_Claro': '\033[103m',
'Azul_Claro': '\033[104m',
'Magenta_Claro': '\033[105m',
'Cyan_Claro': '\033[106m',
'Branco': '\033[107m',
'Nenhum': '\33[0m'}

print(f'{cor["Branco"]}fdsadaf{cor["Nenhum"]}')