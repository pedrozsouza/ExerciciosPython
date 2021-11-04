diaFinal = int(input("Digite o dia final:"))
mesFinal = int(input("Digite o mes final:"))

janeiro = 31
fevereiro = 28
marco = 31
abril = 30
maio = 31
junho = 30
julho = 31
agosto = 31
setembro = 30
outubro = 31
novembro = 30
dezembro = 31
dia = 0

if diaFinal > 31 or mesFinal > 12:
    print("Impossivel realizar o calculo. Anos e/ou meses inconsistentes")
elif mesFinal == 1:
    dia = diaFinal + 0
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 2:
    dia = diaFinal + janeiro
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 3:
    dia = diaFinal + janeiro + fevereiro
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 4:
    dia = diaFinal + janeiro + fevereiro + marco
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 5:
    dia = diaFinal + janeiro + fevereiro + marco + abril
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 6:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 7:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 8:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho + julho
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 9:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho + julho + agosto
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 10:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 11:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro + outubro
    print("Quantidade de dias: {}".format(dia))
elif mesFinal == 12:
    dia = diaFinal + janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro + outubro + novembro
    print("Quantidade de dias: {}".format(dia))
