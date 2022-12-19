#Atv1
IPVA = int(input("Qual o valor do IPVA?"))
IPVADesconto = IPVA - (IPVA * 0.05)

taxTransito = int(input("Qual o valor da taxa?"))

valorPagoAnt = IPVADesconto + taxTransito
print("Valor total a ser pago: RS", valorPagoAnt)
#Atv2
#Regras do Negócio
valorConsConvenio = 70
valorConsParticular = 100

#Entrada
quantConsConvenio = int(input("Quantas consultas convenio?"))
quantConsParticular = int(input("Quantas particulares?"))

#Processamento
totalConvenio =  quantConsConvenio * valorConsConvenio
totalParticular = quantConsParticular * valorConsParticular
totalRecebido = totalConvenio + totalParticular

#Saída
print("valor recebido: R$",totalRecebido)

#Atv3
expDiario = 480
minutosProcesso = float(input("Quantos minutos leva o processo? "))
processo = expDiario/minutosProcesso
totalProcessos = processo
print("Quantidade de processos feitos: ", processo)

#Atv4
convidados = int(input("São quantas pessoas?  "))

precoDoRodizio = int(input('qual o preço do rodizio? '))

descontoRodizio = convidados // 10

precoTotal = precoDoRodizio * (convidados - descontoRodizio)
print(f"{precoTotal:.2f}")
print("{:.2f}".format(precoTotal))
print("%.2f"%precoTotal)

#Atv5
totalRevistas = int(input("Qual o total de revistas? "))
quantAmigos = int(input("Qual a quantidade de amigos? "))
total = totalRevistas/quantAmigos
resto = totalRevistas%quantAmigos
print ("Quantidade para cada amigo: ", total , "Revistas restantes: ", resto)

