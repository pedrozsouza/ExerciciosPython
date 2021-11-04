operacao = str(input("Informe a operação desejada [+,-,*,/]:"))
x = int(input("Informe o numero para ver sua tabuada:"))
if operacao != '+,-,*,/':
    print("Operação digitada ({}) incorreta".format(operacao))
cont = 0

if operacao == '+':
    for c in range(0, 9):
        soma = x + (cont + 1)
        cont += 1
        print("\t\t{} + {} = {}".format(x, cont, soma))
if operacao == '-':
    for c in range(0, 9):
        subt = x - (cont+1)
        cont += 1
        print("\t\t{} - {} = {}".format(x, cont, subt))
if operacao == '*':
    for c in range(0, 9):
        multi = x * (cont+1)
        cont += 1
        print("\t\t{} * {} = {}".format(x, cont, multi))
if operacao == '/':
    for c in range(0, 9):
        div = x / (cont+1)
        cont += 1
        print("\t\t{} - {} = {}".format(x, cont, round(div,2)))
