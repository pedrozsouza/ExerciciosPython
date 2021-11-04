horaNormal = int(input("Digite a quantidade total de horas normais:"))
horaExtra = int(input("Digite a quantidade total de horas extras:"))
dependentes = int(input("Digite a quantidade total de dependentes:"))

salarioHora = horaNormal * 10.00
salarioExtra = horaExtra * 15.00
salarioDepen = dependentes * 90

if dependentes > 3 :
    salarioLiquido = salarioHora - (0.11 * salarioHora)
    salarioDepen = 90 * 3
    salarioFinal = salarioLiquido + salarioExtra + salarioDepen
    print("\nHoras normais: R${}".format(salarioHora))
    print("Adicional de horas extras: R${}".format(salarioExtra))
    print("Adicional de dependentes: R${}".format(salarioDepen))
    print("Salario liquido(Hrs normais - Descontos): R${}".format(salarioLiquido))
    print("Salario Final: R${}".format(salarioFinal))
    print("\nSalario calculado para apenas 3 dependentes\nOs demais {} dependentes nao receberao o auxilio".format(dependentes - 3))
else:
    salarioDepen = dependentes * 90
    salarioLiquido = salarioHora - (0.11 * salarioHora)
    salarioFinal = salarioLiquido + salarioExtra + salarioDepen
    print("\nHoras normais: R${}".format(salarioHora))
    print("Adicional de horas extras: R${}".format(salarioExtra))
    print("Adicional de dependentes: R${}".format(salarioDepen))
    print("Salario liquido(Hrs normais - Descontos): R${}".format(salarioLiquido))
    print("Salario Final: R${}".format(salarioFinal))