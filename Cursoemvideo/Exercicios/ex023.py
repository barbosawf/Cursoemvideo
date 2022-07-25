# Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
# Exemplo: 1895
# Unidade: 5
# Dezena = 9
# Centena = 8
# Milhar = 1


num = str(input('Digite um número de 0 a 9999: ')).strip()
print('A unidade do número é {}.'.format(num[3]))
if len(num) > 1:
   print('A dezena do número é {}.'.format(num[2]))
if len(num) > 2:
    print('A centena do número é {}.'.format(num[1]))
if len(num) > 3:
    print('O milhar do número é {}.'.format(num[0]))
print('')

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.'.format(num))
print('Unidade {}.'.format(u))
print('Dezena {}.'.format(d))
print('Centena {}.'.format(c))
print('Milhar {}.'.format(m))
print(f'{num//1}')
print(f'{num//10}')
