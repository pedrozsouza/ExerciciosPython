ltssuco = int(input("Digite a QTDE de litros de suco necessaria:"))
percentAgua = int(input("Digite o percentual de concentracao de agua:"))
percentSuco = int(input("Digite o percentual de concentracao de suco:"))
decisao =""
if percentAgua + percentSuco == 100:
    porcAgua = (percentAgua * (ltssuco/100))
    porcSuco = (percentSuco * (ltssuco/100))
    print("\nSera necessario para fazer {} lts de suco de maracuja:".format(ltssuco))
    print("\n{} lts de agua".format(porcAgua))
    print("{} lts de suco".format(porcSuco))

else:
    print("Os valores de concentracao nao totalizam 100%")
    decisao = str(input("Deseja enquadrar os valores em escala de 100%? [s/n]"))
if decisao == "s":
    x = (percentAgua / (percentAgua + percentSuco)) * 100
    y = percentSuco / ((percentAgua + percentSuco)) * 100
    print("\nNovo percentual do suco: {}".format(round(y,2)))
    print("Novo percentual de agua : {}".format(round(x,2)))
    porcAgua = (x * (ltssuco / 100))
    porcSuco = (y * (ltssuco / 100))
    print("\nSera necessario para fazer {} lts de suco de maracuja:".format(ltssuco))
    print("\n{} lts de agua".format(round(porcAgua,2)))
    print("{} lts de suco".format(round(porcSuco,2)))
elif decisao == 'n':
    print("\nValores de concentracao incorretos.Processo finalizado")