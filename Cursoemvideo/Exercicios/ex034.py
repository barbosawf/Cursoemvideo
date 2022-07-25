# Desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais o aumento é de 15%.
sal = float(input('Qual é o seu salário? '))
if sal > 1250:
    aumento = 0.1 * sal
else:
    aumento = 0.15 * sal
print('O aumento no seu salário será de R$ {:.2f}, portanto, você receberá no total R$ {:.2f}.'
      .format(aumento, sal + aumento))
