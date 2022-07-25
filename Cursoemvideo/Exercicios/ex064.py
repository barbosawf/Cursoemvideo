""""
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""""

n = 0
a = ''
print()
c = 0
s = 0
while n != 999:
    n = int(input('Digite um  [999 para PARAR]: '))
    b = str(n)
    if n != 999:
        a = a + b + ' '
        s += n
        c += 1
print('\nOs números digitados foram:')
print(a)
print(f'{c} números foram digitados.')
print(f'A soma entre os números vale {s}.')

print('')
n = 0
a = ''
print()
c = 0
s = 0
n = int(input('Digite um número [999 papa PARAR]: '))
while n != 999:
    b = str(n)
    a = a + b + ' '
    s += n
    c += 1
    n = int(input('Digite um número [999 papa PARAR: '))
print('\nOs números digitados foram:')
print(a)
print(f'{c} números foram digitados.')
print(f'A soma entre os números vale {s}.')
