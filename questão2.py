salarioMinimo = float(input("Informe o valor do salario minimo :"))
salarioFuncionario = float(input("Informe o valor do salario do funcionario :"))

resultado = salarioFuncionario / salarioMinimo

if salarioFuncionario < salarioMinimo:
    print("O funcionario ganha menos que um salario minimo!")
if salarioFuncionario > salarioMinimo :
    print("O funcionario recebe {} salarios minimos!".format(round(resultado,1)))