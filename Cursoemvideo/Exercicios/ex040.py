print('Desafio 040')
"""Crie um programa que leia duas notas de uma aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

-Média abaixo de 5: Reprovado
-Média entre 5 e 6.9: Recuperação
-Média 7 ou superior: Aprovado"""

n1 = float(input('Qual é a primeira nota? '))
n2 = float(input('Qual é a segunda nota? '))
media = (n1 + n2)/2

if media < 5:
    print('Sua média é {:.1f} e está abaixo de 5. Você está REPROVADO.'.format(media))
elif 5 <= media < 7:
    print('Sua média é {:.1f} e está entre 6 e 7. Você está de RECUPERAÇÂO'.format(media))
else:
    print('Sua média é {:.1f} e é maior ou igual a 7. Você está APROVADO.'.format(media))
