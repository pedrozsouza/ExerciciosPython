qtdeSandu = int(input("Digite a quantidade de sanduiches:"))

queijo = ((50 * 2) * qtdeSandu)
presunto = 50 * qtdeSandu
hamburguer = 120 * qtdeSandu
qtdeInteira = 0
qtdeMortadela = 0
restante = 0
print("Para produzir {} sanduiches serao necessarios:".format(qtdeSandu))
print("{} kgs de mussarela".format(queijo))
print("{} kgs de presunto".format(presunto))
print("{} kgs de hamburguer\n".format(hamburguer))

presuntoDisponivel = int(input("Qual a quantidade em Kgs disponivel de presunto?"))
if presuntoDisponivel >= presunto:
    print()
else:
    qtdeInteira = presuntoDisponivel // 50
    restante = qtdeSandu - qtdeInteira
    qtdeMortadela = restante * 0.07
    print("\nSera possivel produzir apenas {} sanduiches com presunto".format(qtdeInteira))
    print(("Sera necessario {} kgs de mortadela para produzir {} sanduiches restantes".format(round(qtdeMortadela,3),restante)))
    print("Da quantidade de presunto disponivel sobrara {} kgs".format((presuntoDisponivel%qtdeInteira)/1000))