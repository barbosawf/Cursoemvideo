print('Desafio 036')
"""
Escreva um programa para aprovar o empréstimo bancário para compra 
de uma casa. O programa vai perguntar o valor da casa, o salário do 
comprador e quantos anos ele vai pagar.
Calcule o valor da prestação sabendo que ela não pode exceder 
30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
tempo = int(input('Em quantos anos você quer pagar? '))

prestacao = casa/(tempo * 12)
if prestacao > (sal * 0.3):
    print('Seu empréstimo não foi aprovado.')
else:
    print('Seu empréstimo foi aprovado! Sua prestação será de R$ {:.2f}/mês.'.format(prestacao))
    print('R$ {:.2f} x {} meses = R$ {:.2f}'.format(prestacao, 12 * tempo, 12 * tempo * prestacao))
