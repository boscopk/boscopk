Artistas = [["Bom balanço", "banda", 8000, "Guarabira"],
            ["Violet Blue", "Cantora", 5500, "Areia"],
            ["Beto Bolivia", "Cantor", 4700, "Cacimba de Dentro"],
            ["João", "Cantor", 4700, "Rio Tinto"],
            ["Faz isso comigo", "Cantor", 4700, "MamanGuape"],
            ["Não te tiro da cabeça", "Banda", 4700, "Mataraca"],
            ["Na minha mente", "Cantor", 15000, "Campina grande"],
            ["Dentro de você", "Cantora", 15000, "Peroba"]]

cont = len(Artistas)
n = 0
contCantora = 0
ListaBandas = []
cacheMedio = 0
listaAbsurdo = []


while (n < cont):
    if(((Artistas[n][3]).upper() == "MAMANGUAPE" or (Artistas[n][3]).upper() == "RIO TINTO" or (Artistas[n][3]).upper() == "MATARACA") and (Artistas[n][2] < 5000)):
        if ((Artistas[n][1]).upper()) == "BANDA":
            ListaBandas.append(Artistas[n][0])
    if((Artistas[n][1]).upper() == "CANTORA"):
        cacheMedio += Artistas[n][2]
        contCantora += 1
    if((Artistas[n][2] > 10000) and ((Artistas[n][1]).upper() == "CANTORA" or (Artistas[n][1]).upper() == "CANTOR")):
        if (Artistas[n][3]).upper() not in listaAbsurdo:
            listaAbsurdo.append(Artistas[n][0])
    n = n + 1


print("Nome de todas as bandas das cidades de Rio tinto, Mataraca e Mamanguape que são um cachê menor que 5000: ", ListaBandas)

print("A média de Cachê cobrado pelas cantoras: ", (cacheMedio/contCantora))

print("Nome de todas as cidades que tem cantores cobrando mais de 10000 em cachê: ", listaAbsurdo)