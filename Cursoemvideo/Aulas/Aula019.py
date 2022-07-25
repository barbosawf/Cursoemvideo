dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}.')

locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}.')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'

for k, v in pessoas.items():
    print(f'{k} = {v}.')

pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}.')

brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['UF'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Não se utiliza [:], não dá para fazer fatiamento em dicionários.

for e in brasil:
    print(e)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print('')
