print("Area do trapezio")
baseMaior = float(input("Informe o valor da base maior:"))
baseMenor = float(input("Informe o valor da base menor:"))
altura = float(input("Informe o valor da altura"))

areaTrapezio = ((baseMaior + baseMenor) * altura) / 2

print("\nArea do quadrado:")
lado = float(input("Informe o valor de um dos lados:"))

areaQuadrado = lado * lado

print("\nArea do retangulo:")
largura = float(input("Informe o valor da largura:"))
alturaRetangulo = float(input("Informe o valor da altura:"))

areaRetangulo = largura * alturaRetangulo

print("\nArea do circulo:")
raio = float(input("Informe o valor do raio:"))

areaCirculo = 3.14*raio*raio

print("\nArea do triangulo:")
base = float(input("Informe o valor da base:"))
alturaTriangulo = float(input("Informe o valor da altura:"))

areaTriangulo = (base * alturaTriangulo) / 2

print("\nA area do trapezio e:{} ".format(round(areaTrapezio,2)))
print("A area do quadrado e:{} ".format(round(areaQuadrado,2)))
print("A area do retangulo e:{} ".format(round(areaRetangulo,2)))
print("A area do circulo e:{} ".format(round(areaCirculo,2)))
print("A area do triangulo e:{} ".format(round(areaTriangulo,2)))

maior = areaTrapezio
x = ""
if (areaQuadrado > maior):
        maior = areaQuadrado
        x = "Quadrado"
if (areaRetangulo > maior):
        maior = areaRetangulo
        x = "Retangulo"
if (areaCirculo > maior):
        maior = areaCirculo
        x = "Circulo"
if (areaTriangulo > maior):
        maior = areaTriangulo
        x = "Triangulo"

print('\nO objeto com a maior area é o {} com {} de area '.format(x,round(maior,2)))