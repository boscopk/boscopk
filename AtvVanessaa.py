valorTotal = 0
totalHoras = 0
mes = 10
cont = input("Tipo de contratante : ").upper()

while (mes >= 1):
    mes = int(input("Número do mês: "))
    if(mes < 1):
        break
    tHoras = float(input("Duração: "))
    if(mes <= 6 ):
        totalHoras += tHoras
    if(cont == "PESSOA FÍSICA"):
        if(mes <= 6):
            valorTotal += 150 * tHoras
        else: valorTotal += 210 * tHoras
    else:
        if(mes <= 6): 
           valorTotal += 190 * tHoras
        else:
            valorTotal += 270 * tHoras
        
    print("Duração total do primeiro semestre: %i"%totalHoras)
    print("Valor total a receber: R$ ", valorTotal)        