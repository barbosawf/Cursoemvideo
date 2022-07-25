from Cursoemvideo.ex107 import moeda

# ou import moeda

# ou from moeda import aumentar, dobro

preco = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {preco} é R$ {moeda.aumentar(preco)}.')
print(f'O dobro de R$ {preco} é R$ {moeda.dobro(preco)}.')
print(f'Amentando 10% de R$ {preco}, temos R$ {moeda.aumentar(preco)}.')
print(f'Diminuindo 20% de R$ {preco}, temos R$ {moeda.diminuir(preco, 20)}.')


print(moeda.formatar(3.50))
