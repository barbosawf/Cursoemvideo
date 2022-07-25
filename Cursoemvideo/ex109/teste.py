from Cursoemvideo.ex109 import moeda

# ou import moeda

# ou from moeda import aumentar, dobro

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda2(p)} é {moeda.aumentar(p, True)}.')
print(f'O dobro de {moeda.moeda2(p)} é {moeda.dobro(p, True)}.')
print(f'Amentando 10% de {moeda.moeda2(p)}, temos {moeda.aumentar(p, True)}.')
print(f'Diminuindo 20% de {moeda.moeda2(p)}, temos {moeda.diminuir(p, 20, True)}.')

