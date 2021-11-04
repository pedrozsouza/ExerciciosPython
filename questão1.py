frente = float(input("Quantos metros o terreno possui de frente:"))
lateral = float(input("Quantos metros o terreno possui de lateral:"))
valorMetro = float(input("Informe o valor do metro quadrado: R$ "))
areaTotal = frente * lateral
conta = areaTotal * valorMetro
contaFinal = 0

if (frente - lateral) < (0.1 * frente):
    contaFinal = conta + (conta * 0.22)
    print("Area total do terreno de {} mts de frente com {} mts de lateral e: {}".format(frente, lateral,round(areaTotal, 2)))
    print("O terreno recebeu um acrescimo de 22% e custara: R$ {}".format(round(contaFinal,2)))
elif (0.4 * lateral) > frente:
    contaFinal = conta - (0.12 * conta)
    print("Area total do terreno de {} mts de frente com {} mts de lateral e: {}".format(frente, lateral,
                                                                                         round(areaTotal, 2)))
    print("O terreno recebeu um decrescimo de 12% e custara: R$ {}".format(round(contaFinal, 2)))

elif frente > (0.7 * lateral):
    contaFinal = conta - (conta * 0.15)
    print("Area total do terreno de {} mts de frente com {} mts de lateral e: {}".format(frente, lateral,round(areaTotal, 2)))
    print("O terreno recebeu um decrescimo de 15% e custara: R$ {}".format(round(contaFinal, 2)))

else:
    contaFinal = conta
    print("Area total do terreno de {} mts de frente com {} mts de lateral e: {}".format(frente, lateral,round(areaTotal, 2)))
    print("O terreno não recebeu nenhuma alteração e custara: R$ {}".format(round(contaFinal,2)))