salarioInicial = float(input("Informe o salario: "))

salarioReajustado = (salarioInicial * 0.05) + salarioInicial

descontoInss = (salarioReajustado * 0.11)
descontoFgts = (salarioReajustado * 0.08)
descontoIR = 0

if salarioReajustado <= 1903.98:
    descontoIR = 0.0 * salarioReajustado
elif 1903.99 <= salarioReajustado <= 2826.65:
    descontoIR = 0.075 * salarioReajustado
elif 2826.66 <= salarioReajustado <= 3751.05:
    descontoIR = 0.15 * salarioReajustado
elif 3751.06 <= salarioReajustado <= 4664.68:
    descontoIR = 22.5/100 * salarioReajustado
elif salarioReajustado > 4664.68:
    descontoIR = 27.5/100 * salarioReajustado

totalDescontos = descontoFgts + descontoInss + descontoIR

salarioFinal = salarioReajustado - descontoInss - descontoFgts - descontoIR

print("Salario Inicial: ",round(salarioInicial, 2))
print("Salario Reajustado: ",round(salarioReajustado, 2))
print("Desconto de 11% INSS: ",round(descontoInss,2))
print("Desconto de 8% FGTS: ",round(descontoFgts,2))
print("Desconto IR: ",(round(descontoIR,2)))
print("Total Descontos INSS + FGTS + IR: ",round(totalDescontos, 2))
print("Salario Final: ",round(salarioFinal,2))

if salarioInicial > salarioFinal:
    print("O novo salario final e menor do que o salario antes do aumento")