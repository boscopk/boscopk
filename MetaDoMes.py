DiarioSaude = [ [2, "abril", 90.5, False], [7, "JUNHO", 88.3, True], [20, "Setembro", 84, False] ]

def MetaMes(DiarioSaude, nome, peso):
    meta = peso
    lista_dias = []
    for i in range(len(DiarioSaude)):
        if (DiarioSaude[i][1].upper() == nome.upper()):
            if (DiarioSaude[i][2] <= meta):
                lista_dias.append(DiarioSaude[i][0])
            else:
                pass

    return lista_dias