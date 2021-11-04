peso = float(input("Informe o peso em KG: "))

engorde15 = peso * 0.15
engorde20 = peso * 0.20

if (engorde20 - engorde15) >= 4.5:
    print("Caso a pessoa engorde 15% ficara com:{} KG".format(engorde15 + peso))
    print("Caso a pessoa engorde 20% ficara com:{} KG".format(peso + engorde20))
    print("Voce deve procurar uma nutricionista!")
else :
    print("Caso a pessoa engorde 15% ficara com:{} KG".format(engorde15 + peso))
    print("Caso a pessoa engorde 20% ficara com:{} KG".format(peso + engorde20))