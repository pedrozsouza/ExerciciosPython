faturamentoAtual = float(input("Digite o valor do faturamento anterior:"))
print("=== Codigo dos Produtos===")
print("Produto 1 = 101")
print("Produto 2 = 122")
print("Produto 3 = 163")
codigo = int(input("\nDigite o codigo do produto que se deseja bater a meta:"))

produto1 = 150
produto2 = 220
produto3 = 97

if codigo != 101 and codigo != 122 and codigo != 163:
    print("\nCodigo de produto nao encontrado")

elif codigo == 101:
    faturamentoFuturo = faturamentoAtual + (0.20 * faturamentoAtual)
    vendaProduto = (0.20 * faturamentoAtual) / produto1
    produto = "Produto 1"
    print("\nA meta do proximo mes e R$ {}".format(round(faturamentoFuturo,2)))
    print("Um aumento de: R$ {}".format(0.20 * faturamentoAtual))
    print("Quantidade de pecas a serem vendidas para atingirmos a meta: {} : {} pecas".format(produto,round(vendaProduto,2)))

elif codigo == 122:
    faturamentoFuturo = faturamentoAtual + (0.20 * faturamentoAtual)
    vendaProduto = (0.20 * faturamentoAtual) / produto2
    produto = "Produto 2"
    print("\nA meta do proximo mes e R$ {}".format(round(faturamentoFuturo,2)))
    print("Um aumento de: R$ {}".format(0.20 * faturamentoAtual))
    print("Quantidade de pecas a serem vendidas para atingirmos a meta: {} : {} pecas".format(produto,round(vendaProduto,2)))

elif codigo == 163:
    faturamentoFuturo = faturamentoAtual + (0.20 * faturamentoAtual)
    vendaProduto = (0.20 * faturamentoAtual) / produto3
    produto = "Produto 3"
    print("\nA meta do proximo mes e R$ {}".format(round(faturamentoFuturo,2)))
    print("Um aumento de: R$ {}".format(0.20 * faturamentoAtual))
    print("Quantidade de pecas a serem vendidas para atingirmos a meta: {} : {} pecas".format(produto,round(vendaProduto,2)))
