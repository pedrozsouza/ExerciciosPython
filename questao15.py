lata = int(input("Digite a quantidade de latas de 350ml:"))
garrafa600 = int(input("Digite a quantidade de garrafas de 600ml:"))
garrafa2l = int(input("Digite a quantidade de garrafas de 2lts:"))

totalLitros = (lata * 0.35) + (garrafa600 * 0.6) + (garrafa2l * 2)
print("\nA quantidade total de litros e:{}".format(totalLitros))

lucroLata = lata * 0.15
lucroGarrafa = garrafa600 * 0.09

if lucroGarrafa >= lucroLata:
    subt = (lata * 0.35) / 0.6
    print("Considere substituir a compra de {} latas de 350ml por {} garrafas de 600ml e oferecer uma promocao".format(lata,round(subt,2)))
