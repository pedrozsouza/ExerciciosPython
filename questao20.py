qtdePaes = int(input("Digite a quantidade de paes vendidos:"))
qtdeBroas = int(input("Digite a quantidade de broas vendidas:"))
valorReforma = float(input("Digite o valor da reforma:"))

pao = 0.12 * qtdePaes
broa = 1.50 * qtdeBroas
arrecadou = pao + broa
poupanca = (0.10 * arrecadou)
reforma = valorReforma // poupanca
print("\nFaturamento com a venda de broas: {}".format(round(broa,2)))
print("Faturamento com a venda de paes: {}".format(round(pao,2)))
print("Faturamento diario(paes + broas): {}".format(round(arrecadou,2)))
print("\nValor do deposito na poupanca: {}".format(round(poupanca,2)))
print("Para pagar a reforma serao necessarios: {} dias".format(round(reforma)))

if reforma > 120:
    valorFinal = valorReforma // 120
    print("\nPara realizar a reforma em 120 dias sera necessario depositar diariamente R$ {}".format(valorFinal))
