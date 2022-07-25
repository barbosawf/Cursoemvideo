from Cursoemvideo.ex108 import moeda

# ou import moeda

# ou from moeda import aumentar, dobro

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Amentando 10% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.aumentar(p))}.')
print(f'Diminuindo 20% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.diminuir(p, 20))}.')

print()
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda2(p)} é {moeda.moeda2(moeda.aumentar(p))}.')
print(f'O dobro de {moeda.moeda2(p)} é {moeda.moeda2(moeda.dobro(p))}.')
print(f'Amentando 10% de {moeda.moeda2(p)}, temos {moeda.moeda2(moeda.aumentar(p))}.')
print(f'Diminuindo 20% de {moeda.moeda2(p)}, temos {moeda.moeda2(moeda.diminuir(p, 20))}.')

