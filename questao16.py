num = int(input("Digite um numero de ate 4 digitos:"))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

if 9999 < num or num < 0:
    print("Numero invalido")

NumStr = str(num)
qtdeNumero = len(NumStr)

if qtdeNumero == 4:
    print("Milhares:{}".format(milhar))
    print("Centenas:{}".format(centena))
    print("Dezenas:{}".format(dezena))
    print("Unidades:{}".format(unidade))
if qtdeNumero == 3:
    print("Centenas:{}".format(centena))
    print("Dezenas:{}".format(dezena))
    print("Unidades:{}".format(unidade))
if qtdeNumero == 2:
    print("Dezenas:{}".format(dezena))
    print("Unidades:{}".format(unidade))
if qtdeNumero == 1:
    print("Unidades:{}".format(unidade))