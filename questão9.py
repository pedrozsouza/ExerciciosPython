valorTotal = float(input("Informe o valor total da conta R$:"))

rachar = valorTotal // 3
centavos = (valorTotal % rachar) / 3

if centavos > 0.30:
    print("Carlos pagara:R${}".format(rachar + round(centavos,2)))
    print("Andre pagara:R${}".format(rachar + round(centavos,2)))
    print("Felipe pagara:R${}".format(rachar + round(centavos,2)))
else :
    centavos = (valorTotal % rachar)
    print("Carlos pagara:R${}".format(rachar))
    print("Andre pagara:R${}".format(rachar))
    print("Felipe pagara:R${}".format(rachar + round(centavos, 2)))