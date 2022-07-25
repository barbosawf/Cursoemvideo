tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Já passou da hora de trocar seu carro!')
print('Fim!\n')

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro Velho!' if tempo > 3 else 'Carro novo!')

print('')
nome = str(input('Qual é seu nome? '))
if nome.strip().upper() == 'WAGNER':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
