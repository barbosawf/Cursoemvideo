"""Listas (Parte 2)"""

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # faz uma cópia
teste[0] = 'Maria'
teste[1] = 22
print(teste)
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(' ')
for p in galera:
    print(p)

print(' ')
for p in galera:
    print(p[0])

print(' ')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print(' ')
print('='*50)
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # se não colocar [:] para gerar uma cópia, o comando clear limpa tudo, pois estão ligados.
    dado.clear()
    print('='*50)

totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} e {totmen} de idade.')


