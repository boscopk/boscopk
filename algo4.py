#Entrada

quantLojas = 80
lojas = []
somaFuncionarios = 0
for i in range (quantLojas):
    nome = str(input('Qual é o nome da loja? '))
    tipoProduto = str.upper(input('Qual é o tipo do produto vendido na loja? '))
    quantFuncionarios = float(input('Qual é a quantidade de funcionários nas 80 lojas? '))

    somaFuncionarios += quantFuncionarios
    produtos = [nome, tipoProduto, quantFuncionarios]
    lojas.append(produtos)


if(tipoProduto == 'ROUPA' and quantFuncionarios < 20):
    print(nome)

if(tipoProduto == 'SAPATOS'):
    print(somaFuncionarios)

print(lojas)