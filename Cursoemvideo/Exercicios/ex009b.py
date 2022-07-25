flag = True;
while flag:
    número   = int(input("Entre com o número da tabuada: "))
    operação = str(input("Entre coma operação: [+,-,*,/]: "))
    print("{}".format(15*"="))

    if operação == "+":
        for item in range(1,11):
            print("{} + {} = {}".format(número, item, (número + item)))
    elif operação == "-":
        aux = número
        for item in range(1,11):
            número += 1
            print("{} - {} = {}".format(número, aux, (número - aux)))
    elif operação == "*":
        for item in range(1,11):
            print("{} * {} = {}".format(número, item, (número * item)))
    elif operação == "/":
        aux = número
        for item in range(1,11):
            print("{} / {} = {}".format(número,aux ,(número / aux)))
            número += aux
    else:
        print("Operação inválida!")

    print("{}".format(15 * "="))

    cont = input("Deseja continuar? [Sim/Não]")
    if cont == "Sim":
        flag = True
    elif cont == "Não":
        flag = False
    else:
        print("Valor inválido!")

else:
    print("Programa encerrado!")