# Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 > n3:
    print('{} é o maior valor e {} é o menor valor.'.format(n1, n3))
else:
    if n1 > n3 > n2:
        print('{} é o maior valor e {} é o menor valor.'.format(n1, n2))
    else:
        if n2 > n1 > n3:
            print('{} é o maior valor e {} é o menor valor.'.format(n2, n3))
        else:
            if n2 > n3 > n1:
                print('{} é o maior valor e {} é o menor valor.'.format(n2, n1))
            else:
                if n3 > n2 > n1:
                    print('{} é o maior valor e {} é o menor valor.'.format(n3, n1))
                else:
                    print('{} é o maior valor e {} é o menor valor.'.format(n3, n2))

print('')
print('Resolução do Guanabara')
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o menor valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{} é o maior valor e {} é o menor valor.'.format(maior, menor))
