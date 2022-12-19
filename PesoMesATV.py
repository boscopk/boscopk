DiarioSaude = [ [2, "abril", 90.5, False], [7, "JUNHO", 88.3, True], [20, "Setembro", 84, False] ]


def MaiorPesoMes(DiarioSaude, nome):
    maiorPeso = ""
    diaDoMes = 0
    for i in range(len(DiarioSaude)):
        if (DiarioSaude[i][1].upper() == nome.upper()):
            if (maiorPeso == ""):
                maiorPeso = DiarioSaude[i][2]
                diaDoMes = DiarioSaude[i][0]
            else:
                if (DiarioSaude[i][2] >= maiorPeso):
                    maiorPeso = DiarioSaude[i][2]
                    diaDoMes = diaDoMes = DiarioSaude[i][0]
                else:
                    pass

    return diaDoMes