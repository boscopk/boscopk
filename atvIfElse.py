#AtvIfElse
#atv1
numero = float(input("Informe seu número: "))
if (numero > 0):
    print("seu número é positivo")

elif (numero == 0):
    print("seu número é neutro")

elif (numero < 0):
    print("seu número é negativo")

#atv2
numero = float(input("Informe seu número: "))
if (numero /2 and numero % 2 == 0):
    print("seu número é par")

else: 
    print("seu número é ímpar")

#atv3
numero1 = float(input("Informe seu primeiro número: "))
numero2 = float(input("Informe seu segundo número: "))
numero3 = float(input("Informe seu terceiro número: "))
if (numero1 > numero2 > numero3 or numero1 > numero3 > numero2):
    print("O número", numero1,"é maior")

elif (numero2 > numero1 > numero3 or numero2 > numero3 > numero1):
    print("O número",numero2,"é maior")

elif (numero3 > numero2 > numero1 or numero3 > numero1 > numero2):
    print("O número",numero3,"é maior")

#atv4
bolsaCouro = 180
bolsaTecido = 100
relogioMetal = 215
relogioCouro = 150

pedido = str(input("Seu produto: "))
tipoDoProduto = str(input("Qual material? "))
