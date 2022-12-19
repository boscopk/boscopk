Brinquedos = [["Estela e bebê", 26.90], ["Bola", 15.80],
              ["Alquimia", 31.20], ["Quebra-cabeça", 47.00]]


def calculaValor(Brinquedos):
    quantBrin = 0
    for k in Brinquedos:
        if(k[0][0].upper() != "A" and k[0][0].upper() != "E" and k[0][0].upper() != "I" and k[0][0].upper() != "O" and k[0][0].upper() != "U"):
            if(k[1] > 30.0):
                quantBrin += 1

    return quantBrin


print(calculaValor(Brinquedos))