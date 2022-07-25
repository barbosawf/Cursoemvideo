print('Desafio 044')
"""
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
quant = float(input('Quanto você gastou em compras? R$ '))
print("""
Como você quer pagar?
[1] À vista dinheiro/cheque: 10% de desconto.
[2] À vista no cartão: 5% de desconto.
[3] Em até 2x no cartão: preço normal.
[4] 3x ou mais no cartão: 20% de juros.
""")
op = int(input('Digite a opção: '))

if op == 1:
    print('Você tem 10% de desconto e deve pagar R$ {:.2f}.'.format(quant - 0.1 * quant))
elif op == 2:
    print('Você tem 5% de desconto e deve pagar R$ {:.2f}.'.format(quant - 0.05 * quant))
elif op == 3:
    parc = quant / 2
    print('Você não tem desconto e deve pagar duas parcelas de R$ {:.2f}, totalizando R$ {:.2f}.'.format(parc, quant))
elif op == 4:
    quant_j = quant + 0.2 * quant
    vezes = int(input('Em quantas vezes você quer pagar? '))
    parc = quant_j / vezes
    print('Você pagará {} parcelas de R$ {:.2f}, ou seja, R$ {:.2f} no total.'.format(vezes, parc, quant_j))
else:
    print('OPÇÃO INVÁLIDA! ')