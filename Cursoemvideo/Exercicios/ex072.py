"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
     'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

while num not in range(0, 21):
    if num in range(0, 21):
        num = int(input('Digite um número entre 0 e 20: '))
    else:
        num = int(input('Tente novamente! Digite um número entre 0 e 20: '))

print(f'Você digitou o número {a[num]}.\n')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM!')

