cavalos = int(input("Informe a quantidade de cavalos: "))
valor = float(input("Informe o valor de cada ferradura:"))

quantFerraduras = cavalos * 4
valorTotal = valor * quantFerraduras
resultado = 0
if 20000.00 > valorTotal > 15000.01:
    resultado = valorTotal -(0.10 * valorTotal)
elif 25000.00 > valorTotal > 20000.01:
    resultado = valorTotal -(0.12 * valorTotal)
elif 30000.00 > valorTotal > 25000.01:
    resultado = valorTotal -(0.15 * valorTotal)
elif valorTotal > 30000.01:
    resultado = valorTotal -(0.20 * valorTotal)
else:
    resultado = valorTotal
print("Quantidade de ferraduras necessarias:",quantFerraduras)
print("Valor total para compra das ferraduras: R$",round(resultado,2))