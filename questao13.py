qtdefrango = int(input("Digite a QTDE de frangos:"))
chipAlimentacao = float(input("Digite o valor do chip de alimentacao R$:"))
chipIdentificacao = float(input("Digite o valor do chip de indentificacao R$:"))

maior = 0
menor = 0
adicional = 0

contaIndent = chipIdentificacao * qtdefrango
contaAlimen = (chipAlimentacao * 2) * qtdefrango

if chipAlimentacao > chipIdentificacao:
        maior = chipAlimentacao
        menor = chipIdentificacao
        adicional = (0.2 * contaIndent)
else:
        maior = chipIdentificacao
        menor = chipAlimentacao
        adicional = (0.2 * contaAlimen)

print("\nChip alimentacao = R${}".format(contaAlimen))
print("Chip indentificacao = R${}".format(contaIndent))

if abs(chipAlimentacao - chipIdentificacao) <= (0.2 * maior):
    print("\nAdicional 20% = R${}".format(adicional))
    print("Valor total = R${}".format(contaAlimen + contaIndent + adicional))
else :
    print("Valor total = R${}".format(contaAlimen + contaIndent))