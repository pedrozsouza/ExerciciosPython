nota1 = float(input("Informe a nota 1 do aluno :"))
nota2 = float(input("Informe a nota 2 do aluno :"))
nota3 = float(input("Informe a nota 3 do aluno :"))

media = ((nota1 * 1) + (nota2 * 2) + (nota3 * 3)) / 6

print("A media ponderada das notas",nota1,nota2,nota3,"e",round(media,2))

if (nota2 * 2) < (nota3 * 3) > (nota1 * 1):
    print("A nota 3({}) e a maior nota apos o calculo do peso 3({})".format(nota3,nota3*3))
elif (nota3 * 3) == (nota2 * 2) and (nota3 * 3) == (nota1 * 1):
    print("As tres notas foram iguais")
elif (nota3 * 3) < (nota2 * 2) > (nota1 * 1):
    print("A nota 2({}) e a maior nota apos o calculo do peso 2({})".format(nota2, nota2 * 2))
elif (nota1 * 1) > (nota2 * 2) and (nota1 * 1) > (nota3 * 3):
    print("A nota 1({}) e a maior nota apos o calculo do peso 1({})".format(nota1, nota1 * 1))
elif (nota2 * 2) == (nota1 * 1):
    print("As notas 1({}) e 2({}) foram as maiores nota apos o calculo do peso 1({}) e peso 2({})".format(nota1,nota2,nota1*1,nota2*2))
elif (nota2 * 2) == (nota3 * 3):
    print("As notas 2({}) e 3({}) foram as maiores nota apos o calculo do peso 2({}) e peso 3({})".format(nota2, nota3,nota2 * 2,nota3 * 3))
elif (nota1 * 1) == (nota3 * 3):
    print("As notas 1({}) e 3({}) foram as maiores nota apos o calculo do peso 1({}) e peso 3({})".format(nota1, nota3,nota1 * 1,nota3 * 3))

