"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
dicionario = {}
print('='*50)
dicionario['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
while True:
    dicionario['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dicionario['Carteira'] < 0:
        del dicionario['Carteira']
    elif dicionario['Carteira'] >= 0:
        break
dicionario['Idade'] = date.today().year - nasc

if dicionario['Carteira'] > 0:
    dicionario['Contrato'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = float(input('Salário: R$ '))
    dicionario['Aposentadoria'] = dicionario['Contrato'] - date.today().year + dicionario['Idade'] + 35

print('='*50)
for k, v in dicionario.items():
    print(f'   - {k} = {v}')
print('='*50)



